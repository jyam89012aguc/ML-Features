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


def _roc(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _logret(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


# ===== folder domain primitives (share-count dilution / issuance / buyback) =====
def _f29_dilution(shares, w):
    # share-count growth = dilution over w days (positive => dilutive)
    return shares / shares.shift(w).replace(0, np.nan) - 1.0


def _f29_logdilution(shares, w):
    return np.log(shares.replace(0, np.nan) / shares.shift(w).replace(0, np.nan))


def _f29_dilution_streak(shares):
    # consecutive periods of rising share count (dilution streak), length normalized
    d = shares.diff()
    up = (d > 0).astype(float)
    grp = (up != up.shift(1)).cumsum()
    run = up.groupby(grp).cumsum()
    return run * up


def _f29_cum_dilution(shares, w):
    # cumulative ISSUANCE churn = summed positive daily share growth over window
    # (counts only dilutive moves; differs from net ratio when there are pullbacks)
    pc = shares.pct_change().clip(lower=0)
    return pc.rolling(w, min_periods=max(1, w // 2)).sum()


def _f29_dilbasic_spread(dil, basic, w):
    # diluted-share creep: shareswadil vs shareswa
    return dil / basic.replace(0, np.nan) - 1.0


def _f29_issuance(ncfcommon):
    # net issuance (raise) = -ncfcommon ; positive => capital raised via equity
    return -ncfcommon


# ============================================================
# 1y basic-share dilution (share-count growth)
def f29sc_f29_share_count_dynamics_dilbas_252d_base_v001_signal(sharesbas):
    b = _f29_dilution(sharesbas, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 2y basic-share dilution
def f29sc_f29_share_count_dynamics_dilbas_504d_base_v002_signal(sharesbas):
    b = _f29_dilution(sharesbas, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quarter basic-share dilution (sequential issuance pace)
def f29sc_f29_share_count_dynamics_dilbas_63d_base_v003_signal(sharesbas):
    b = _f29_dilution(sharesbas, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 1y log dilution of weighted-average shares
def f29sc_f29_share_count_dynamics_dilwa_252d_base_v004_signal(shareswa):
    b = _f29_logdilution(shareswa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 2y log dilution of weighted-average shares
def f29sc_f29_share_count_dynamics_dilwa_504d_base_v005_signal(shareswa):
    b = _f29_logdilution(shareswa, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-vs-basic growth amplification: how much faster diluted shares grow than basic
# (>1 => option/RSU pool expanding faster than the float = building overhang)
def f29sc_f29_share_count_dynamics_dildil_252d_base_v006_signal(shareswadil, shareswa):
    dd = _f29_logdilution(shareswadil, 252)
    db = _f29_logdilution(shareswa, 252)
    b = dd / db.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-vs-basic creep level (shareswadil / shareswa - 1)
def f29sc_f29_share_count_dynamics_dilcreep_base_v007_signal(shareswadil, shareswa):
    b = _f29_dilbasic_spread(shareswadil, shareswa, 0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in diluted-vs-basic creep over a year (option/RSU overhang building)
def f29sc_f29_share_count_dynamics_dilcreepchg_252d_base_v008_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    b = sp - sp.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net equity issuance (raise) = -ncfcommon, normalized by its own 252d scale
def f29sc_f29_share_count_dynamics_issuance_252d_base_v009_signal(ncfcommon):
    raise_ = _f29_issuance(ncfcommon)
    scale = raise_.abs().rolling(252, min_periods=63).mean()
    b = raise_ / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback intensity = ncfcommon-positive-side (return of capital), normalized
def f29sc_f29_share_count_dynamics_buyback_252d_base_v010_signal(ncfcommon):
    buyback = ncfcommon.clip(lower=0)
    scale = ncfcommon.abs().rolling(252, min_periods=63).mean()
    b = buyback / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution streak length (consecutive rises in basic share count)
def f29sc_f29_share_count_dynamics_dilstreak_base_v011_signal(sharesbas):
    b = _f29_dilution_streak(sharesbas) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution concentration over 252d: Herfindahl of monthly share-growth contributions
# (lumpy single-offering issuance -> high; steady drip -> low). Distinct from net level.
def f29sc_f29_share_count_dynamics_cumdil_252d_base_v012_signal(sharesbas):
    g = _f29_dilution(sharesbas, 21).clip(lower=0)
    tot = g.rolling(252, min_periods=126).sum()
    sq = (g * g).rolling(252, min_periods=126).sum()
    b = sq / (tot * tot).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution concentration over 504d (Herfindahl of share-growth contributions)
def f29sc_f29_share_count_dynamics_cumdil_504d_base_v013_signal(sharesbas):
    g = _f29_dilution(sharesbas, 21).clip(lower=0)
    tot = g.rolling(504, min_periods=252).sum()
    sq = (g * g).rolling(504, min_periods=252).sum()
    b = sq / (tot * tot).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution acceleration-as-level: 1y dilution minus prior-1y dilution
def f29sc_f29_share_count_dynamics_dilaccel_252d_base_v014_signal(sharesbas):
    d = _f29_dilution(sharesbas, 252)
    b = d - d.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution z-score vs own 504d history (extremity of issuance pace)
def f29sc_f29_share_count_dynamics_dilz_252d_base_v015_signal(sharesbas):
    d = _f29_dilution(sharesbas, 252)
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-issuance vs buyback regime sign (issuer vs returner of capital)
def f29sc_f29_share_count_dynamics_capdir_252d_base_v016_signal(ncfcommon):
    sm = ncfcommon.rolling(252, min_periods=63).sum()
    scale = ncfcommon.abs().rolling(252, min_periods=63).sum()
    b = -sm / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year with rising share count (dilution-quarter tally, count-friendly)
def f29sc_f29_share_count_dynamics_diltally_252d_base_v017_signal(sharesbas):
    up = (sharesbas.diff() > 0).astype(float)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic-vs-weighted-avg lag: sharesbas relative to shareswa (point-in-time vs averaged)
def f29sc_f29_share_count_dynamics_basvswa_base_v018_signal(sharesbas, shareswa):
    b = sharesbas / shareswa.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in basic-vs-weighted lag over a quarter (issuance leading the average)
def f29sc_f29_share_count_dynamics_basvswachg_63d_base_v019_signal(sharesbas, shareswa):
    sp = sharesbas / shareswa.replace(0, np.nan) - 1.0
    b = sp - sp.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year diluted-share dilution
def f29sc_f29_share_count_dynamics_dildil_126d_base_v020_signal(shareswadil):
    b = _f29_logdilution(shareswadil, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average option-drag overhang: mean diluted-minus-basic share gap over 252d, float-scaled
# (the persistent size of the dilutive pool, a level/area measure, not a growth difference)
def f29sc_f29_share_count_dynamics_dildrag_252d_base_v021_signal(shareswadil, shareswa):
    gap = (shareswadil - shareswa) / shareswa.replace(0, np.nan)
    b = gap.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5y cumulative dilution (long-horizon share growth)
def f29sc_f29_share_count_dynamics_dilbas_1260d_base_v022_signal(sharesbas):
    b = _f29_logdilution(sharesbas, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance burst: largest 21d raise within the last year scaled by share base
def f29sc_f29_share_count_dynamics_issburst_252d_base_v023_signal(ncfcommon, sharesbas):
    raise21 = _f29_issuance(ncfcommon).rolling(21, min_periods=5).sum()
    peak = raise21.rolling(252, min_periods=63).max()
    b = peak / sharesbas.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution dispersion: std of quarterly share-growth over a year (lumpy issuance)
def f29sc_f29_share_count_dynamics_dildisp_252d_base_v024_signal(sharesbas):
    q = _f29_dilution(sharesbas, 63)
    b = q.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-issuance smoothed (EMA of -ncfcommon, scaled)
def f29sc_f29_share_count_dynamics_issema_base_v025_signal(ncfcommon):
    raise_ = _f29_issuance(ncfcommon)
    ema = raise_.ewm(span=63, min_periods=21).mean()
    scale = raise_.abs().rolling(252, min_periods=63).mean()
    b = ema / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution momentum: quarter dilution minus half-year-ago quarter dilution
def f29sc_f29_share_count_dynamics_dilmom_63d_base_v026_signal(sharesbas):
    d = _f29_dilution(sharesbas, 63)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-share creep percentile-ranked vs its own 504d history
def f29sc_f29_share_count_dynamics_creeprank_504d_base_v027_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    b = sp.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count drawup pace: cumulative issuance vs time elapsed since the 504d minimum
# (how fast the float has expanded off its trough, not just how far)
def f29sc_f29_share_count_dynamics_drawup_504d_base_v028_signal(sharesbas):
    w = 504
    lo = sharesbas.rolling(w, min_periods=126).min()
    draw = sharesbas / lo.replace(0, np.nan) - 1.0

    def _dsince_min(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))

    age = sharesbas.rolling(w, min_periods=126).apply(_dsince_min, raw=True)
    b = draw / age.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback vs issuance net flow over 2y, share-base scaled
def f29sc_f29_share_count_dynamics_netflow_504d_base_v029_signal(ncfcommon, sharesbas):
    raise_ = _f29_issuance(ncfcommon).rolling(504, min_periods=126).sum()
    b = raise_ / (sharesbas * sharesbas.rolling(504, min_periods=126).mean().replace(0, np.nan) ** 0).replace(0, np.nan)
    b = _f29_issuance(ncfcommon).rolling(504, min_periods=126).sum() / sharesbas.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# is share count near its all-time (504d) high? proximity to peak dilution
def f29sc_f29_share_count_dynamics_peakprox_504d_base_v030_signal(sharesbas):
    hi = sharesbas.rolling(504, min_periods=126).max()
    b = sharesbas / hi.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-avg share dilution z vs own 252d (de-trended issuance pace)
def f29sc_f29_share_count_dynamics_dilwaz_126d_base_v031_signal(shareswa):
    d = _f29_logdilution(shareswa, 126)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-creep velocity (change over a quarter)
def f29sc_f29_share_count_dynamics_creepvel_63d_base_v032_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    b = sp - sp.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive buyback streak (periods of ncfcommon > 0 = repurchase), normalized
def f29sc_f29_share_count_dynamics_bbstreak_base_v033_signal(ncfcommon):
    bb = (ncfcommon > 0).astype(float)
    grp = (bb != bb.shift(1)).cumsum()
    run = bb.groupby(grp).cumsum()
    b = (run * bb) / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-vs-buyback tug: 252d share growth minus normalized buyback intensity
def f29sc_f29_share_count_dynamics_tug_252d_base_v034_signal(sharesbas, ncfcommon):
    dil = _f29_dilution(sharesbas, 252)
    bb = ncfcommon.clip(lower=0).rolling(252, min_periods=63).sum()
    scale = ncfcommon.abs().rolling(252, min_periods=63).sum()
    b = dil - bb / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log share growth tanh-squashed momentum (bounded issuance shock)
def f29sc_f29_share_count_dynamics_diltanh_63d_base_v035_signal(sharesbas):
    chg = _f29_logdilution(sharesbas, 63)
    b = np.tanh(20.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dominant capital event: sign x magnitude of the single largest |ncfcommon| in 252d
# (one big secondary offering or buyback dwarfing the rest), float-independent
def f29sc_f29_share_count_dynamics_signmag_252d_base_v036_signal(ncfcommon):
    raise_ = _f29_issuance(ncfcommon)
    scale = raise_.abs().rolling(252, min_periods=63).mean()
    rr = raise_ / scale.replace(0, np.nan)
    amax = rr.rolling(252, min_periods=63).max()
    amin = rr.rolling(252, min_periods=63).min()
    dom = np.where(amax.abs() >= amin.abs(), amax, amin)
    dom = pd.Series(dom, index=ncfcommon.index)
    b = np.sign(dom) * (dom.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep-driven share of 504d diluted growth: fraction of diluted-share growth coming
# from option-pool expansion rather than basic-float issuance
def f29sc_f29_share_count_dynamics_dildil_504d_base_v037_signal(shareswadil, shareswa):
    dd = _f29_logdilution(shareswadil, 504)
    db = _f29_logdilution(shareswa, 504)
    b = (dd - db) / dd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance intensity relative to basic share base (raise per share outstanding)
def f29sc_f29_share_count_dynamics_isspershare_252d_base_v038_signal(ncfcommon, sharesbas):
    raise_ = _f29_issuance(ncfcommon).rolling(252, min_periods=63).sum()
    b = raise_ / sharesbas.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution stability: 1 / (1 + std of monthly share growth) -- steadiness of issuance
def f29sc_f29_share_count_dynamics_dilstab_252d_base_v039_signal(sharesbas):
    m = _f29_dilution(sharesbas, 21)
    sd = m.rolling(252, min_periods=126).std()
    b = 1.0 / (1.0 + sd.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic vs diluted growth divergence z (option exercise pressure)
def f29sc_f29_share_count_dynamics_divz_252d_base_v040_signal(shareswadil, shareswa):
    dd = _f29_logdilution(shareswadil, 252)
    db = _f29_logdilution(shareswa, 252)
    b = _z(dd - db, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count new-high frequency over the last quarter (persistent dilution regime)
def f29sc_f29_share_count_dynamics_newhifreq_252d_base_v041_signal(sharesbas):
    hi = sharesbas.rolling(252, min_periods=126).max()
    is_high = (sharesbas >= hi * 0.99999).astype(float)
    b = is_high.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-avg dilution ranked vs cross-time history
def f29sc_f29_share_count_dynamics_dilwarank_504d_base_v042_signal(shareswa):
    d = _f29_logdilution(shareswa, 252)
    b = d.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance-burst intensity: magnitude-weighted excess of monthly jumps over 2% in last year
def f29sc_f29_share_count_dynamics_burstcount_252d_base_v043_signal(sharesbas):
    m = _f29_dilution(sharesbas, 21)
    excess = (m - 0.02).clip(lower=0)
    cnt = (m > 0.02).astype(float).rolling(252, min_periods=126).sum()
    b = cnt + 50.0 * excess.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback magnitude per share base (shrink rate via repurchase)
def f29sc_f29_share_count_dynamics_bbpershare_252d_base_v044_signal(ncfcommon, sharesbas):
    bb = ncfcommon.clip(lower=0).rolling(252, min_periods=63).sum()
    b = bb / sharesbas.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-creep oscillator: creep level minus its slow EMA (overhang building vs easing)
def f29sc_f29_share_count_dynamics_creepema_base_v045_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    b = sp - sp.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share growth confirmed by cash raised: dilution x normalized net issuance flow
# (dilution that is backed by actual equity raises, not just option creep)
def f29sc_f29_share_count_dynamics_confirm_252d_base_v046_signal(sharesbas, ncfcommon):
    dil = _f29_dilution(sharesbas, 252)
    flow = _f29_issuance(ncfcommon).rolling(252, min_periods=63).sum()
    scale = _f29_issuance(ncfcommon).abs().rolling(252, min_periods=63).sum()
    rn = (flow / scale.replace(0, np.nan)).clip(-1.0, 1.0)
    b = dil * np.tanh(2.0 * rn)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shift toward lumpier issuance: YoY change in dilution concentration (Herfindahl)
# (positive => issuance becoming more offering-driven vs steady drip)
def f29sc_f29_share_count_dynamics_cumdilyoy_base_v047_signal(sharesbas):
    g = _f29_dilution(sharesbas, 21).clip(lower=0)
    tot = g.rolling(252, min_periods=126).sum()
    sq = (g * g).rolling(252, min_periods=126).sum()
    hhi = sq / (tot * tot).replace(0, np.nan)
    b = hhi - hhi.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count amplitude: 504d max/min spread relative to current (issuance range)
def f29sc_f29_share_count_dynamics_amplitude_504d_base_v048_signal(sharesbas):
    hi = sharesbas.rolling(504, min_periods=126).max()
    lo = sharesbas.rolling(504, min_periods=126).min()
    b = (hi - lo) / sharesbas.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net capital flow EMA-displacement (acceleration of issuance vs trend)
def f29sc_f29_share_count_dynamics_flowdisp_base_v049_signal(ncfcommon):
    raise_ = _f29_issuance(ncfcommon)
    scale = raise_.abs().rolling(252, min_periods=63).mean()
    r = raise_ / scale.replace(0, np.nan)
    b = r.ewm(span=21, min_periods=10).mean() - r.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted dilution stretched above 252d average diluted dilution (creep extension)
def f29sc_f29_share_count_dynamics_dildilext_252d_base_v050_signal(shareswadil):
    d = _f29_logdilution(shareswadil, 63)
    mn = d.rolling(252, min_periods=126).mean()
    b = d - mn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 2y share count spent in upper third of its range (high-dilution time)
def f29sc_f29_share_count_dynamics_uppertime_504d_base_v051_signal(sharesbas):
    hi = sharesbas.rolling(504, min_periods=126).max()
    lo = sharesbas.rolling(504, min_periods=126).min()
    pos = (sharesbas - lo) / (hi - lo).replace(0, np.nan)
    upper = (pos >= 0.6667).astype(float)
    b = upper.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance-to-buyback ratio asymmetry over 504d (one-sided capital activity)
def f29sc_f29_share_count_dynamics_asym_504d_base_v052_signal(ncfcommon):
    issue = _f29_issuance(ncfcommon).clip(lower=0).rolling(504, min_periods=126).sum()
    bb = ncfcommon.clip(lower=0).rolling(504, min_periods=126).sum()
    b = (issue - bb) / (issue + bb).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quarter-over-quarter diluted-creep acceleration
def f29sc_f29_share_count_dynamics_creepaccel_63d_base_v053_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    v = sp - sp.shift(63)
    b = v - v.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shareswa vs shareswadil mid position trend (option dilution drift)
def f29sc_f29_share_count_dynamics_dilmidtrend_252d_base_v054_signal(shareswadil, shareswa):
    gap = shareswadil - shareswa
    b = _logret(gap.clip(lower=1.0), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted issuance pace: quarter share growth per unit of monthly-growth volatility
# (steady fast dilution scores high; choppy/lumpy dilution is discounted)
def f29sc_f29_share_count_dynamics_issrate_63d_base_v055_signal(sharesbas):
    g63 = _f29_dilution(sharesbas, 63)
    vol = _f29_dilution(sharesbas, 21).rolling(252, min_periods=63).std()
    b = g63 / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution drag z (diluted minus basic growth, de-trended over 504d)
def f29sc_f29_share_count_dynamics_dragz_504d_base_v056_signal(shareswadil, shareswa):
    dd = _f29_logdilution(shareswadil, 126)
    db = _f29_logdilution(shareswa, 126)
    b = _z(dd - db, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count log level vs its 252d EMA (recent issuance displacement)
def f29sc_f29_share_count_dynamics_lvldisp_252d_base_v057_signal(sharesbas):
    ls = np.log(sharesbas.replace(0, np.nan))
    b = ls - ls.ewm(span=252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise-funded dilution: issuance(-ncfcommon) interacted with diluted creep
def f29sc_f29_share_count_dynamics_raisecreep_252d_base_v058_signal(ncfcommon, shareswadil, shareswa):
    raise_n = _f29_issuance(ncfcommon).rolling(252, min_periods=63).sum()
    scale = ncfcommon.abs().rolling(252, min_periods=63).sum()
    rn = raise_n / scale.replace(0, np.nan)
    creep = shareswadil / shareswa.replace(0, np.nan) - 1.0
    b = rn * creep
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution deceleration flag-weighted: depth of slowdown in share growth
def f29sc_f29_share_count_dynamics_dildecel_252d_base_v059_signal(sharesbas):
    d = _f29_dilution(sharesbas, 252)
    slow = (d < d.shift(63)).astype(float)
    depth = (d.shift(63) - d).clip(lower=0)
    b = slow * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon dilution disagreement (63/252/504 share growth dispersion)
def f29sc_f29_share_count_dynamics_dildisp_multi_base_v060_signal(sharesbas):
    d1 = _f29_dilution(sharesbas, 63)
    d2 = _f29_dilution(sharesbas, 252)
    d3 = _f29_dilution(sharesbas, 504)
    b = pd.concat([d1, d2, d3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-avg share growth half-life: 126d dilution relative to 504d dilution
def f29sc_f29_share_count_dynamics_dilterm_base_v061_signal(shareswa):
    s = _f29_logdilution(shareswa, 126)
    l = _f29_logdilution(shareswa, 504)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback efficiency: shrink in share count during buyback periods
def f29sc_f29_share_count_dynamics_bbshrink_252d_base_v062_signal(sharesbas, ncfcommon):
    is_bb = (ncfcommon.rolling(63, min_periods=21).sum() > 0).astype(float)
    shrink = (-_f29_dilution(sharesbas, 63)).clip(lower=0)
    b = (is_bb * shrink).rolling(252, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-trough staleness: fraction of the 504d window since the share-count minimum
# (how long the float has been at/above its trough = entrenched dilution regime)
def f29sc_f29_share_count_dynamics_rangepos_504d_base_v063_signal(sharesbas):
    def _dsince_min(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))

    b = sharesbas.rolling(504, min_periods=126).apply(_dsince_min, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance-shock skew: skewness of monthly capital flows over a year
def f29sc_f29_share_count_dynamics_flowskew_252d_base_v064_signal(ncfcommon):
    flow = _f29_issuance(ncfcommon)
    scale = flow.abs().rolling(252, min_periods=63).mean()
    r = flow / scale.replace(0, np.nan)
    b = r.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-share dilution acceleration (252d dil minus prior-year 252d dil)
def f29sc_f29_share_count_dynamics_dildilaccel_base_v065_signal(shareswadil):
    d = _f29_logdilution(shareswadil, 252)
    b = d - d.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net dilution including buyback offset: share growth net of repurchase intensity
def f29sc_f29_share_count_dynamics_netdil_252d_base_v066_signal(sharesbas, ncfcommon):
    dil = _f29_logdilution(sharesbas, 252)
    bbflag = (ncfcommon.clip(lower=0).rolling(252, min_periods=63).sum()
              / ncfcommon.abs().rolling(252, min_periods=63).sum().replace(0, np.nan))
    b = dil * (1.0 - bbflag)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count quarterly growth smoothness (autocorr-like persistence proxy)
def f29sc_f29_share_count_dynamics_dilpersist_base_v067_signal(sharesbas):
    g = sharesbas.pct_change(21)
    up = (g > 0).astype(float)
    b = up.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compound overhang pressure: basic dilution interacted with the LEVEL of diluted creep
# (fast float growth while option overhang is already high = severe paper-share pressure)
def f29sc_f29_share_count_dynamics_compound_252d_base_v068_signal(shareswa, shareswadil):
    dwa = _f29_logdilution(shareswa, 252)
    creep = shareswadil / shareswa.replace(0, np.nan) - 1.0
    creep_z = _z(creep, 252)
    b = np.sign(dwa) * (dwa.abs() ** 0.5) * creep_z
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance recency: days since last share-count increase, normalized
def f29sc_f29_share_count_dynamics_issrecency_252d_base_v069_signal(sharesbas):
    up = (sharesbas.diff() > 0).astype(float)

    def _dsince(a):
        idx = np.where(a > 0)[0]
        if len(idx) == 0:
            return 1.0
        return (len(a) - 1 - idx[-1]) / float(len(a))

    b = up.rolling(252, min_periods=126).apply(_dsince, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-flow trend: slope sign of cumulative -ncfcommon over 252d
def f29sc_f29_share_count_dynamics_flowtrend_252d_base_v070_signal(ncfcommon):
    cum = _f29_issuance(ncfcommon).cumsum()
    b = cum - cum.rolling(252, min_periods=63).mean()
    scale = _f29_issuance(ncfcommon).abs().rolling(252, min_periods=63).sum()
    b = b / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted creep dispersion over 504d (volatility of option overhang)
def f29sc_f29_share_count_dynamics_creepdisp_504d_base_v071_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    b = sp.rolling(504, min_periods=252).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-base step detection: max single-day jump over last quarter scaled by base
def f29sc_f29_share_count_dynamics_maxstep_63d_base_v072_signal(sharesbas):
    step = sharesbas.pct_change()
    b = step.rolling(63, min_periods=21).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-avg vs basic growth lead-lag spread (averaging-window dilution lag)
def f29sc_f29_share_count_dynamics_leadlag_252d_base_v073_signal(sharesbas, shareswa):
    db = _f29_logdilution(sharesbas, 252)
    dw = _f29_logdilution(shareswa, 252)
    b = db - dw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raising-pace acceleration: how the trailing 252d raise compares to the prior 252d raise
# (ramping up vs winding down equity financing), share-base scaled
def f29sc_f29_share_count_dynamics_raisestock_504d_base_v074_signal(ncfcommon, sharesbas):
    raise_ = _f29_issuance(ncfcommon)
    recent = raise_.rolling(252, min_periods=63).sum()
    prior = raise_.shift(252).rolling(252, min_periods=63).sum()
    b = (recent - prior) / sharesbas.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution regime distance: current 252d dilution minus its 504d median
def f29sc_f29_share_count_dynamics_regimedist_base_v075_signal(sharesbas):
    d = _f29_dilution(sharesbas, 252)
    med = d.rolling(504, min_periods=126).median()
    b = d - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29sc_f29_share_count_dynamics_dilbas_252d_base_v001_signal,
    f29sc_f29_share_count_dynamics_dilbas_504d_base_v002_signal,
    f29sc_f29_share_count_dynamics_dilbas_63d_base_v003_signal,
    f29sc_f29_share_count_dynamics_dilwa_252d_base_v004_signal,
    f29sc_f29_share_count_dynamics_dilwa_504d_base_v005_signal,
    f29sc_f29_share_count_dynamics_dildil_252d_base_v006_signal,
    f29sc_f29_share_count_dynamics_dilcreep_base_v007_signal,
    f29sc_f29_share_count_dynamics_dilcreepchg_252d_base_v008_signal,
    f29sc_f29_share_count_dynamics_issuance_252d_base_v009_signal,
    f29sc_f29_share_count_dynamics_buyback_252d_base_v010_signal,
    f29sc_f29_share_count_dynamics_dilstreak_base_v011_signal,
    f29sc_f29_share_count_dynamics_cumdil_252d_base_v012_signal,
    f29sc_f29_share_count_dynamics_cumdil_504d_base_v013_signal,
    f29sc_f29_share_count_dynamics_dilaccel_252d_base_v014_signal,
    f29sc_f29_share_count_dynamics_dilz_252d_base_v015_signal,
    f29sc_f29_share_count_dynamics_capdir_252d_base_v016_signal,
    f29sc_f29_share_count_dynamics_diltally_252d_base_v017_signal,
    f29sc_f29_share_count_dynamics_basvswa_base_v018_signal,
    f29sc_f29_share_count_dynamics_basvswachg_63d_base_v019_signal,
    f29sc_f29_share_count_dynamics_dildil_126d_base_v020_signal,
    f29sc_f29_share_count_dynamics_dildrag_252d_base_v021_signal,
    f29sc_f29_share_count_dynamics_dilbas_1260d_base_v022_signal,
    f29sc_f29_share_count_dynamics_issburst_252d_base_v023_signal,
    f29sc_f29_share_count_dynamics_dildisp_252d_base_v024_signal,
    f29sc_f29_share_count_dynamics_issema_base_v025_signal,
    f29sc_f29_share_count_dynamics_dilmom_63d_base_v026_signal,
    f29sc_f29_share_count_dynamics_creeprank_504d_base_v027_signal,
    f29sc_f29_share_count_dynamics_drawup_504d_base_v028_signal,
    f29sc_f29_share_count_dynamics_netflow_504d_base_v029_signal,
    f29sc_f29_share_count_dynamics_peakprox_504d_base_v030_signal,
    f29sc_f29_share_count_dynamics_dilwaz_126d_base_v031_signal,
    f29sc_f29_share_count_dynamics_creepvel_63d_base_v032_signal,
    f29sc_f29_share_count_dynamics_bbstreak_base_v033_signal,
    f29sc_f29_share_count_dynamics_tug_252d_base_v034_signal,
    f29sc_f29_share_count_dynamics_diltanh_63d_base_v035_signal,
    f29sc_f29_share_count_dynamics_signmag_252d_base_v036_signal,
    f29sc_f29_share_count_dynamics_dildil_504d_base_v037_signal,
    f29sc_f29_share_count_dynamics_isspershare_252d_base_v038_signal,
    f29sc_f29_share_count_dynamics_dilstab_252d_base_v039_signal,
    f29sc_f29_share_count_dynamics_divz_252d_base_v040_signal,
    f29sc_f29_share_count_dynamics_newhifreq_252d_base_v041_signal,
    f29sc_f29_share_count_dynamics_dilwarank_504d_base_v042_signal,
    f29sc_f29_share_count_dynamics_burstcount_252d_base_v043_signal,
    f29sc_f29_share_count_dynamics_bbpershare_252d_base_v044_signal,
    f29sc_f29_share_count_dynamics_creepema_base_v045_signal,
    f29sc_f29_share_count_dynamics_confirm_252d_base_v046_signal,
    f29sc_f29_share_count_dynamics_cumdilyoy_base_v047_signal,
    f29sc_f29_share_count_dynamics_amplitude_504d_base_v048_signal,
    f29sc_f29_share_count_dynamics_flowdisp_base_v049_signal,
    f29sc_f29_share_count_dynamics_dildilext_252d_base_v050_signal,
    f29sc_f29_share_count_dynamics_uppertime_504d_base_v051_signal,
    f29sc_f29_share_count_dynamics_asym_504d_base_v052_signal,
    f29sc_f29_share_count_dynamics_creepaccel_63d_base_v053_signal,
    f29sc_f29_share_count_dynamics_dilmidtrend_252d_base_v054_signal,
    f29sc_f29_share_count_dynamics_issrate_63d_base_v055_signal,
    f29sc_f29_share_count_dynamics_dragz_504d_base_v056_signal,
    f29sc_f29_share_count_dynamics_lvldisp_252d_base_v057_signal,
    f29sc_f29_share_count_dynamics_raisecreep_252d_base_v058_signal,
    f29sc_f29_share_count_dynamics_dildecel_252d_base_v059_signal,
    f29sc_f29_share_count_dynamics_dildisp_multi_base_v060_signal,
    f29sc_f29_share_count_dynamics_dilterm_base_v061_signal,
    f29sc_f29_share_count_dynamics_bbshrink_252d_base_v062_signal,
    f29sc_f29_share_count_dynamics_rangepos_504d_base_v063_signal,
    f29sc_f29_share_count_dynamics_flowskew_252d_base_v064_signal,
    f29sc_f29_share_count_dynamics_dildilaccel_base_v065_signal,
    f29sc_f29_share_count_dynamics_netdil_252d_base_v066_signal,
    f29sc_f29_share_count_dynamics_dilpersist_base_v067_signal,
    f29sc_f29_share_count_dynamics_compound_252d_base_v068_signal,
    f29sc_f29_share_count_dynamics_issrecency_252d_base_v069_signal,
    f29sc_f29_share_count_dynamics_flowtrend_252d_base_v070_signal,
    f29sc_f29_share_count_dynamics_creepdisp_504d_base_v071_signal,
    f29sc_f29_share_count_dynamics_maxstep_63d_base_v072_signal,
    f29sc_f29_share_count_dynamics_leadlag_252d_base_v073_signal,
    f29sc_f29_share_count_dynamics_raisestock_504d_base_v074_signal,
    f29sc_f29_share_count_dynamics_regimedist_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_SHARE_COUNT_DYNAMICS_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

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

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    # share count: smooth drift PLUS occasional discrete issuance jumps (offerings/RSU vest)
    _sb = np.random.default_rng(101)
    _drift = np.repeat(_sb.normal(0.02, 0.06, n // 63 + 1), 63)[:n] / 63.0
    _jumps = np.zeros(n)
    _jidx = _sb.choice(np.arange(63, n), size=34, replace=False)
    _jumps[_jidx] = _sb.uniform(0.008, 0.06, size=34)
    sharesbas = pd.Series(1.2e8 * np.exp(np.cumsum(_drift + _jumps)),
                          name="sharesbas")
    # weighted-average shares lag the basic count (averaging window smoothing)
    shareswa = sharesbas.rolling(63, min_periods=1).mean().rename("shareswa")
    # diluted creep (option/RSU overhang) wanders between ~2% and ~9% over time
    _cr = np.random.default_rng(103)
    _creep = 0.05 + 0.03 * np.sin(np.linspace(0, 7.0, n)) + np.cumsum(
        _cr.normal(0, 0.0015, n))
    _creep = np.clip(_creep, 0.005, 0.20)
    shareswadil = (shareswa * (1.0 + _creep)).rename("shareswadil")
    # ncfcommon oscillates in sign (issuance vs buyback quarters) -- step every 63d
    _g = np.random.default_rng(104)
    _steps = np.repeat(_g.normal(0.0, 1.0, n // 63 + 1), 63)[:n]
    _mag = _fund(105, base=4e6, drift=0.0, vol=0.25)
    ncfcommon = pd.Series(_steps * _mag.values, name="ncfcommon")

    cols = {
        "sharesbas": sharesbas, "shareswa": shareswa,
        "shareswadil": shareswadil, "ncfcommon": ncfcommon,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "BADCOL %s: %s" % (name, meta["inputs"])
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

    print("OK f29_share_count_dynamics_base_001_075_claude: %d features pass" % n_features)
