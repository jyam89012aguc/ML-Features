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
    # log share-count growth over w days = dilution intensity
    return np.log(shares.replace(0, np.nan) / shares.shift(w).replace(0, np.nan))


def _f19_dil_rate(shares, w):
    # simple pct dilution over window
    return shares / shares.shift(w).replace(0, np.nan) - 1.0


def _f19_creep(shareswadil, shareswa):
    # diluted-share creep: how much the diluted count exceeds basic weighted
    return shareswadil / shareswa.replace(0, np.nan) - 1.0


def _f19_issuance(ncfcommon):
    # net issuance proxy: -ncfcommon (cash raised from issuing stock is a positive raise)
    return -ncfcommon


def _f19_streak(cond):
    # length of current consecutive True streak (in rows)
    grp = (~cond).cumsum()
    return cond.groupby(grp).cumsum()


# ============================================================
# core annual basic-share dilution (252d log growth of shares outstanding)
def f19di_f19_dilution_intensity_basgrow_252d_base_v001_signal(sharesbas):
    b = _f19_growth(sharesbas, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quarterly basic-share dilution rate
def f19di_f19_dilution_intensity_basgrow_63d_base_v002_signal(sharesbas):
    b = _f19_dil_rate(sharesbas, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year basic-share dilution, z-scored vs its own 252d history
def f19di_f19_dilution_intensity_basgrowz_126d_base_v003_signal(sharesbas):
    g = _f19_growth(sharesbas, 126)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# two-year cumulative dilution over the cycle (504d log growth)
def f19di_f19_dilution_intensity_basgrow_504d_base_v004_signal(sharesbas):
    b = _f19_growth(sharesbas, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# five-year multi-cycle dilution (1260d log growth)
def f19di_f19_dilution_intensity_basgrow_1260d_base_v005_signal(sharesbas):
    b = _f19_growth(sharesbas, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-average share dilution (annual, shareswa) — operational share creep
def f19di_f19_dilution_intensity_wagrow_252d_base_v006_signal(shareswa):
    b = _f19_growth(shareswa, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted weighted-average share growth (annual) — full dilution incl options/warrants
def f19di_f19_dilution_intensity_dilgrow_252d_base_v007_signal(shareswadil):
    b = _f19_growth(shareswadil, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-share creep: shareswadil vs shareswa overhang level
def f19di_f19_dilution_intensity_creep_base_v008_signal(shareswadil, shareswa):
    b = _f19_creep(shareswadil, shareswa)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in diluted-share creep over a year (overhang expanding/contracting)
def f19di_f19_dilution_intensity_creepchg_252d_base_v009_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    b = c - c.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net issuance proxy (-ncfcommon) scaled by basic share count (raise per share)
def f19di_f19_dilution_intensity_issperhsh_base_v010_signal(ncfcommon, sharesbas):
    iss = _f19_issuance(ncfcommon)
    b = iss / sharesbas.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trailing-year cumulative net issuance (sum of -ncfcommon over 252d)
def f19di_f19_dilution_intensity_isscum_252d_base_v011_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    b = _rsum(iss, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net issuance z-scored vs its own 504d history (abnormal raise)
def f19di_f19_dilution_intensity_issz_504d_base_v012_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    b = _z(iss, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution acceleration: 63d dilution annualized vs 252d dilution rate
def f19di_f19_dilution_intensity_dilaccel_base_v013_signal(sharesbas):
    short = _f19_dil_rate(sharesbas, 63) * 4.0
    long = _f19_dil_rate(sharesbas, 252)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution streak: fraction of last year with rising share count
def f19di_f19_dilution_intensity_dilstreak_252d_base_v014_signal(sharesbas):
    up = (sharesbas > sharesbas.shift(21)).astype(float)
    b = up.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive-month dilution streak length (rank-normalized)
def f19di_f19_dilution_intensity_dilstreaklen_base_v015_signal(sharesbas):
    up = sharesbas > sharesbas.shift(21)
    streak = _f19_streak(up)
    b = streak.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance intensity acceleration: this year's issuance/share vs last year's (ramping raises)
def f19di_f19_dilution_intensity_issintens_252d_base_v016_signal(ncfcommon, sharesbas):
    iss = _rsum(_f19_issuance(ncfcommon), 252) / sharesbas.replace(0, np.nan)
    b = iss - iss.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution dispersion: volatility of monthly dilution rate over a year
def f19di_f19_dilution_intensity_dildisp_252d_base_v017_signal(sharesbas):
    rate = sharesbas.pct_change(21)
    b = _std(rate, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-rate stability: 504d std of quarterly dilution scaled by its mean (erratic vs steady)
def f19di_f19_dilution_intensity_basvsmin_504d_base_v018_signal(sharesbas):
    qd = sharesbas.pct_change(63)
    sd = _std(qd, 504)
    mu = _mean(qd, 504)
    b = sd / mu.abs().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cycle-relative dilution pace: recent annual dilution vs the 5y average annual dilution
def f19di_f19_dilution_intensity_basvsmin_1260d_base_v019_signal(sharesbas):
    annual = _f19_growth(sharesbas, 252)
    longavg = annual.rolling(1260, min_periods=504).mean()
    b = annual - longavg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted share-base vs its own 504d minimum (overhang-inclusive dilution multiple)
def f19di_f19_dilution_intensity_dilvsmin_504d_base_v020_signal(shareswadil):
    mn = _rmin(shareswadil, 504)
    b = shareswadil / mn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance recency: position of the largest issuance in the past year (staleness)
def f19di_f19_dilution_intensity_issrecency_252d_base_v021_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)

    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))

    b = iss.rolling(252, min_periods=126).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution momentum: change in 252d dilution growth over a quarter
def f19di_f19_dilution_intensity_dilmom_252d_base_v022_signal(sharesbas):
    g = _f19_growth(sharesbas, 252)
    b = g - g.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-vs-weighted growth spread, ranked vs its own 504d history (overhang-pace regime)
def f19di_f19_dilution_intensity_growspr_252d_base_v023_signal(shareswadil, shareswa):
    gd = _f19_growth(shareswadil, 63)
    gw = _f19_growth(shareswa, 63)
    spr = gd - gw
    b = _rank(spr, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic vs weighted-avg share gap (period-end issuance not yet weighted in)
def f19di_f19_dilution_intensity_baswagap_base_v024_signal(sharesbas, shareswa):
    b = sharesbas / shareswa.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance burst persistence: fraction of last quarter with above-median issuance
def f19di_f19_dilution_intensity_issburst_63d_base_v025_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    med = iss.rolling(252, min_periods=126).median()
    hot = (iss > med).astype(float)
    b = hot.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net issuance relative to its own trailing-year magnitude (normalized raise)
def f19di_f19_dilution_intensity_issnorm_252d_base_v026_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    scale = iss.abs().rolling(252, min_periods=126).mean()
    b = iss / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution rank: where current 252d dilution sits vs its own 504d history
def f19di_f19_dilution_intensity_dilrank_252d_base_v027_signal(sharesbas):
    g = _f19_growth(sharesbas, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution EMA crossover: fast vs slow exponential of the monthly dilution rate
def f19di_f19_dilution_intensity_dilema_base_v028_signal(sharesbas):
    rate = sharesbas.pct_change(21)
    fast = rate.ewm(span=21, min_periods=10).mean()
    slow = rate.ewm(span=126, min_periods=42).mean()
    b = fast - slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution displacement: monthly dilution minus its own slow EMA
def f19di_f19_dilution_intensity_dildisp2_base_v029_signal(sharesbas):
    rate = sharesbas.pct_change(21)
    b = rate - rate.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative issuance vs gross flow (issuance directionality over a year)
def f19di_f19_dilution_intensity_issdir_252d_base_v030_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    net = _rsum(iss, 252)
    gross = _rsum(iss.abs(), 252)
    b = net / gross.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-share creep z-scored (abnormal option/warrant overhang)
def f19di_f19_dilution_intensity_creepz_252d_base_v031_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    b = _z(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of dilution-event months in past year (share count up > 1% over a month)
def f19di_f19_dilution_intensity_dilevents_252d_base_v032_signal(sharesbas):
    big = (sharesbas / sharesbas.shift(21).replace(0, np.nan) - 1.0 > 0.01).astype(float)
    b = big.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recency-weighted recent dilution (recent dilution counts more)
def f19di_f19_dilution_intensity_dilrecent_base_v033_signal(sharesbas):
    rate = sharesbas.pct_change(21).clip(lower=0)
    w = np.arange(1, 64)
    b = rate.rolling(63, min_periods=21).apply(
        lambda a: np.average(a, weights=w[-len(a):]) if len(a) > 0 else np.nan, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-pace surprise: half-year annualized dilution vs its own trailing 504d expectation
def f19di_f19_dilution_intensity_dilpace_base_v034_signal(sharesbas):
    pace = _f19_growth(sharesbas, 126) * 2.0
    expect = pace.rolling(504, min_periods=252).median()
    sd = pace.rolling(504, min_periods=252).std()
    b = (pace - expect) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share raise momentum: change in trailing-quarter issuance/share over a quarter
def f19di_f19_dilution_intensity_isspershz_base_v035_signal(ncfcommon, sharesbas):
    ips = _rsum(_f19_issuance(ncfcommon), 63) / sharesbas.replace(0, np.nan)
    b = ips - ips.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution convexity proxy: sign x sqrt-magnitude of annual dilution
def f19di_f19_dilution_intensity_dilsignmag_base_v036_signal(sharesbas):
    g = _f19_growth(sharesbas, 252)
    b = np.sign(g) * (g.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-bounded quarterly dilution momentum
def f19di_f19_dilution_intensity_diltanh_base_v037_signal(sharesbas):
    g = _f19_growth(sharesbas, 63)
    chg = g - g.shift(21)
    b = np.tanh(50.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-count annual dilution rank vs 504d history
def f19di_f19_dilution_intensity_dilrank2_base_v038_signal(shareswadil):
    g = _f19_growth(shareswadil, 252)
    b = _rank(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative dilution over the cycle: log(sharesbas / 1260d trailing mean)
def f19di_f19_dilution_intensity_cumdil_1260d_base_v039_signal(sharesbas):
    mn = _mean(sharesbas, 1260)
    b = np.log(sharesbas.replace(0, np.nan) / mn.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance coverage z: cash raised per new share created, z-scored (price-per-raise regime)
def f19di_f19_dilution_intensity_isscover_base_v040_signal(ncfcommon, sharesbas):
    iss = _rsum(_f19_issuance(ncfcommon), 252)
    addshares = (sharesbas - sharesbas.shift(252)).clip(lower=1.0)
    perraise = iss / addshares
    b = _z(perraise, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest dilution-free gap in past year (max consecutive flat/declining months)
def f19di_f19_dilution_intensity_quietstreak_252d_base_v041_signal(sharesbas):
    quiet = sharesbas <= sharesbas.shift(21) * 1.0005
    streak = _f19_streak(quiet)
    b = streak.rolling(252, min_periods=126).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic-share growth curvature: second difference of 126d growth
def f19di_f19_dilution_intensity_dilcurv_base_v042_signal(sharesbas):
    g = _f19_growth(sharesbas, 126)
    b = g - 2.0 * g.shift(63) + g.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest single-month dilution jump in past year (max issuance shock)
def f19di_f19_dilution_intensity_maxdiljump_252d_base_v043_signal(sharesbas):
    jump = sharesbas / sharesbas.shift(21).replace(0, np.nan) - 1.0
    b = _rmax(jump, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance burstiness: ratio of max monthly issuance to mean (lumpy raises)
def f19di_f19_dilution_intensity_issburstiness_base_v044_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon).clip(lower=0)
    mx = _rmax(iss, 252)
    mn = _mean(iss, 252)
    b = mx / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-avg dilution velocity (change in 252d wa-growth over a month)
def f19di_f19_dilution_intensity_wavel_base_v045_signal(shareswa):
    g = _f19_growth(shareswa, 252)
    b = g - g.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-to-issuance sign agreement over a year (raises coincide with dilution)
def f19di_f19_dilution_intensity_dilissagree_base_v046_signal(sharesbas, ncfcommon):
    dil = (sharesbas.pct_change(21) > 0).astype(float)
    iss = (_f19_issuance(ncfcommon) > 0).astype(float)
    agree = (dil == iss).astype(float)
    b = agree.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance momentum reversal: trailing-quarter issuance now vs a quarter ago (raise pulse)
def f19di_f19_dilution_intensity_isstrend_126d_base_v047_signal(ncfcommon):
    q = _rsum(_f19_issuance(ncfcommon), 63)
    chg = q - q.shift(63)
    scale = q.abs().rolling(252, min_periods=63).mean()
    b = chg / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-creep momentum over a quarter
def f19di_f19_dilution_intensity_creepmom_63d_base_v048_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    b = c - c.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution pause depth: how far below its 252d share-count high (issuance halt proxy)
def f19di_f19_dilution_intensity_basnewhi_252d_base_v049_signal(sharesbas):
    hi = sharesbas.rolling(252, min_periods=126).max()
    gap = sharesbas / hi.replace(0, np.nan) - 1.0
    b = gap.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance-into-dilution efficiency: per-share raise vs the diluted-share creep it added
def f19di_f19_dilution_intensity_basfreshhi_504d_base_v050_signal(ncfcommon, shareswadil):
    raise_per = _rsum(_f19_issuance(ncfcommon), 252) / shareswadil.replace(0, np.nan)
    creepadd = (shareswadil / shareswadil.shift(252).replace(0, np.nan) - 1.0)
    ratio = raise_per / (creepadd.abs() + 1e-9)
    b = _rank(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution intensity scaled by its own dispersion (risk-adjusted dilution)
def f19di_f19_dilution_intensity_dilriskadj_base_v051_signal(sharesbas):
    g = _f19_growth(sharesbas, 126)
    vol = _std(sharesbas.pct_change(21), 252)
    b = g / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance per-share cumulative over two years (deep dilution drag)
def f19di_f19_dilution_intensity_isspersh_504d_base_v052_signal(ncfcommon, sharesbas):
    iss = _rsum(_f19_issuance(ncfcommon), 504)
    b = iss / sharesbas.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution turning point: 2nd difference of the 63d dilution rate (cycle inflection)
def f19di_f19_dilution_intensity_dilyoy_base_v053_signal(sharesbas):
    rate = sharesbas.pct_change(63)
    b = rate - 2.0 * rate.shift(63) + rate.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted overhang vs its own two-year max creep (overhang stress)
def f19di_f19_dilution_intensity_creepstress_base_v054_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    mx = _rmax(c, 504)
    b = c - mx
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise-episode count + magnitude: entries into net-issuance regime weighted by raise size
def f19di_f19_dilution_intensity_raisequarters_base_v055_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    qsum = _rsum(iss, 63)
    raised = (qsum > 0).astype(float)
    entries = ((raised == 1) & (raised.shift(1) == 0)).astype(float)
    cnt = entries.rolling(252, min_periods=126).sum()
    scale = iss.abs().rolling(252, min_periods=126).mean()
    intensity = (qsum.clip(lower=0) / scale.replace(0, np.nan)).rolling(252, min_periods=126).mean()
    b = cnt + intensity
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution acceleration via second difference of share log-level
def f19di_f19_dilution_intensity_basaccel_base_v056_signal(sharesbas):
    lvl = np.log(sharesbas.replace(0, np.nan))
    b = lvl - 2.0 * lvl.shift(63) + lvl.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-issuance vs share-growth divergence (cash raised but few new shares)
def f19di_f19_dilution_intensity_isssharediv_base_v057_signal(ncfcommon, sharesbas):
    issz = _z(_rsum(_f19_issuance(ncfcommon), 63), 252)
    dilz = _z(sharesbas.pct_change(63), 252)
    b = issz * dilz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted share-count drawup from 1260d trough (max cumulative dilution multiple)
def f19di_f19_dilution_intensity_dildrawup_1260d_base_v058_signal(shareswadil):
    g = _f19_growth(shareswadil, 252)
    longavg = g.rolling(1260, min_periods=504).mean()
    sd = g.rolling(1260, min_periods=504).std()
    b = (g - longavg) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution streak length weighted by intensity (sustained heavy dilution)
def f19di_f19_dilution_intensity_streakmag_base_v059_signal(sharesbas):
    up = sharesbas > sharesbas.shift(21)
    streak = _f19_streak(up)
    mag = sharesbas.pct_change(21).clip(lower=0)
    raw = streak * mag
    b = _rank(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance regime distance: current trailing-year issuance vs its 504d median
def f19di_f19_dilution_intensity_issregime_base_v060_signal(ncfcommon):
    cum = _rsum(_f19_issuance(ncfcommon), 252)
    med = cum.rolling(504, min_periods=252).median()
    scale = cum.abs().rolling(504, min_periods=126).mean()
    b = (cum - med) / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-avg share dilution dispersion over two years (erratic issuance)
def f19di_f19_dilution_intensity_wadisp_504d_base_v061_signal(shareswa):
    rate = shareswa.pct_change(63)
    b = _std(rate, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted vs basic level ratio percentile-ranked (overhang regime)
def f19di_f19_dilution_intensity_overhangrank_base_v062_signal(shareswadil, sharesbas):
    ratio = shareswadil / sharesbas.replace(0, np.nan)
    b = _rank(ratio, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# annual dilution minus its smoothed baseline (dilution surprise)
def f19di_f19_dilution_intensity_dilsurprise_base_v063_signal(sharesbas):
    g = _f19_growth(sharesbas, 252)
    base = g.ewm(span=126, min_periods=42).mean()
    b = g - base
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative net-issuance gap from peak (issuance fatigue / stopped raising)
def f19di_f19_dilution_intensity_isspeakgap_base_v064_signal(ncfcommon):
    cum = _f19_issuance(ncfcommon).cumsum()
    peak = cum.rolling(504, min_periods=126).max()
    scale = cum.abs().rolling(504, min_periods=126).mean()
    b = (cum - peak) / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon dilution term structure: annualized short pace minus annualized long pace
def f19di_f19_dilution_intensity_dilterm_base_v065_signal(sharesbas):
    fast = _f19_growth(sharesbas, 63) * 4.0
    slow = _f19_growth(sharesbas, 504) * 0.5
    b = (fast - slow) / (fast.abs() + slow.abs() + 1e-9)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-creep dispersion (volatile overhang)
def f19di_f19_dilution_intensity_creepdisp_base_v066_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    b = _std(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net issuance vs basic dilution interaction (raise effectiveness)
def f19di_f19_dilution_intensity_issdilinter_base_v067_signal(ncfcommon, sharesbas):
    iss = _z(_rsum(_f19_issuance(ncfcommon), 252), 504)
    dil = _z(_f19_growth(sharesbas, 252), 504)
    b = iss * dil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-base growth tail: 95th-pct monthly dilution over a year (worst-case dilution)
def f19di_f19_dilution_intensity_diltail_base_v068_signal(sharesbas):
    rate = sharesbas.pct_change(21)
    b = rate.rolling(252, min_periods=126).quantile(0.95)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-count five-year cumulative dilution log-growth
def f19di_f19_dilution_intensity_dilgrow_1260d_base_v069_signal(shareswadil):
    b = _f19_growth(shareswadil, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance smoothness: mean issuance over its volatility (steady vs lumpy raises)
def f19di_f19_dilution_intensity_isssmooth_base_v070_signal(ncfcommon):
    iss = _f19_issuance(ncfcommon)
    mu = _mean(iss, 252)
    sd = _std(iss, 252)
    b = mu / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-adjusted issuance: cash raised per new share created, z-scored
def f19di_f19_dilution_intensity_issperaddsh_base_v071_signal(ncfcommon, sharesbas):
    iss = _f19_issuance(ncfcommon)
    add = (sharesbas - sharesbas.shift(63)).clip(lower=0)
    raw = _rsum(iss, 63) / add.replace(0, np.nan)
    b = _z(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic-vs-diluted dilution-pace divergence (which share count is accelerating faster)
def f19di_f19_dilution_intensity_dilspeed_base_v072_signal(sharesbas, shareswadil):
    gb = sharesbas.pct_change(63)
    gd = shareswadil.pct_change(63)
    div = gd - gb
    b = _z(div, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# basic vs weighted-avg share spread momentum (issuance timing within period)
def f19di_f19_dilution_intensity_waspread_mom_base_v073_signal(sharesbas, shareswa):
    spr = sharesbas / shareswa.replace(0, np.nan) - 1.0
    b = spr - spr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution lumpiness: Herfindahl concentration of monthly dilution over 2y
def f19di_f19_dilution_intensity_dildrag_504d_base_v074_signal(sharesbas):
    md = sharesbas.pct_change(21).clip(lower=0)
    tot = md.rolling(504, min_periods=252).sum()
    share = md / tot.replace(0, np.nan)
    b = (share ** 2).rolling(504, min_periods=252).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhang acceleration: change in diluted-vs-weighted creep growth (warrant strike pull-in)
def f19di_f19_dilution_intensity_overhangdil_base_v075_signal(shareswadil, shareswa):
    c = _f19_creep(shareswadil, shareswa)
    accel = c - 2.0 * c.shift(63) + c.shift(126)
    b = np.tanh(40.0 * accel)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19di_f19_dilution_intensity_basgrow_252d_base_v001_signal,
    f19di_f19_dilution_intensity_basgrow_63d_base_v002_signal,
    f19di_f19_dilution_intensity_basgrowz_126d_base_v003_signal,
    f19di_f19_dilution_intensity_basgrow_504d_base_v004_signal,
    f19di_f19_dilution_intensity_basgrow_1260d_base_v005_signal,
    f19di_f19_dilution_intensity_wagrow_252d_base_v006_signal,
    f19di_f19_dilution_intensity_dilgrow_252d_base_v007_signal,
    f19di_f19_dilution_intensity_creep_base_v008_signal,
    f19di_f19_dilution_intensity_creepchg_252d_base_v009_signal,
    f19di_f19_dilution_intensity_issperhsh_base_v010_signal,
    f19di_f19_dilution_intensity_isscum_252d_base_v011_signal,
    f19di_f19_dilution_intensity_issz_504d_base_v012_signal,
    f19di_f19_dilution_intensity_dilaccel_base_v013_signal,
    f19di_f19_dilution_intensity_dilstreak_252d_base_v014_signal,
    f19di_f19_dilution_intensity_dilstreaklen_base_v015_signal,
    f19di_f19_dilution_intensity_issintens_252d_base_v016_signal,
    f19di_f19_dilution_intensity_dildisp_252d_base_v017_signal,
    f19di_f19_dilution_intensity_basvsmin_504d_base_v018_signal,
    f19di_f19_dilution_intensity_basvsmin_1260d_base_v019_signal,
    f19di_f19_dilution_intensity_dilvsmin_504d_base_v020_signal,
    f19di_f19_dilution_intensity_issrecency_252d_base_v021_signal,
    f19di_f19_dilution_intensity_dilmom_252d_base_v022_signal,
    f19di_f19_dilution_intensity_growspr_252d_base_v023_signal,
    f19di_f19_dilution_intensity_baswagap_base_v024_signal,
    f19di_f19_dilution_intensity_issburst_63d_base_v025_signal,
    f19di_f19_dilution_intensity_issnorm_252d_base_v026_signal,
    f19di_f19_dilution_intensity_dilrank_252d_base_v027_signal,
    f19di_f19_dilution_intensity_dilema_base_v028_signal,
    f19di_f19_dilution_intensity_dildisp2_base_v029_signal,
    f19di_f19_dilution_intensity_issdir_252d_base_v030_signal,
    f19di_f19_dilution_intensity_creepz_252d_base_v031_signal,
    f19di_f19_dilution_intensity_dilevents_252d_base_v032_signal,
    f19di_f19_dilution_intensity_dilrecent_base_v033_signal,
    f19di_f19_dilution_intensity_dilpace_base_v034_signal,
    f19di_f19_dilution_intensity_isspershz_base_v035_signal,
    f19di_f19_dilution_intensity_dilsignmag_base_v036_signal,
    f19di_f19_dilution_intensity_diltanh_base_v037_signal,
    f19di_f19_dilution_intensity_dilrank2_base_v038_signal,
    f19di_f19_dilution_intensity_cumdil_1260d_base_v039_signal,
    f19di_f19_dilution_intensity_isscover_base_v040_signal,
    f19di_f19_dilution_intensity_quietstreak_252d_base_v041_signal,
    f19di_f19_dilution_intensity_dilcurv_base_v042_signal,
    f19di_f19_dilution_intensity_maxdiljump_252d_base_v043_signal,
    f19di_f19_dilution_intensity_issburstiness_base_v044_signal,
    f19di_f19_dilution_intensity_wavel_base_v045_signal,
    f19di_f19_dilution_intensity_dilissagree_base_v046_signal,
    f19di_f19_dilution_intensity_isstrend_126d_base_v047_signal,
    f19di_f19_dilution_intensity_creepmom_63d_base_v048_signal,
    f19di_f19_dilution_intensity_basnewhi_252d_base_v049_signal,
    f19di_f19_dilution_intensity_basfreshhi_504d_base_v050_signal,
    f19di_f19_dilution_intensity_dilriskadj_base_v051_signal,
    f19di_f19_dilution_intensity_isspersh_504d_base_v052_signal,
    f19di_f19_dilution_intensity_dilyoy_base_v053_signal,
    f19di_f19_dilution_intensity_creepstress_base_v054_signal,
    f19di_f19_dilution_intensity_raisequarters_base_v055_signal,
    f19di_f19_dilution_intensity_basaccel_base_v056_signal,
    f19di_f19_dilution_intensity_isssharediv_base_v057_signal,
    f19di_f19_dilution_intensity_dildrawup_1260d_base_v058_signal,
    f19di_f19_dilution_intensity_streakmag_base_v059_signal,
    f19di_f19_dilution_intensity_issregime_base_v060_signal,
    f19di_f19_dilution_intensity_wadisp_504d_base_v061_signal,
    f19di_f19_dilution_intensity_overhangrank_base_v062_signal,
    f19di_f19_dilution_intensity_dilsurprise_base_v063_signal,
    f19di_f19_dilution_intensity_isspeakgap_base_v064_signal,
    f19di_f19_dilution_intensity_dilterm_base_v065_signal,
    f19di_f19_dilution_intensity_creepdisp_base_v066_signal,
    f19di_f19_dilution_intensity_issdilinter_base_v067_signal,
    f19di_f19_dilution_intensity_diltail_base_v068_signal,
    f19di_f19_dilution_intensity_dilgrow_1260d_base_v069_signal,
    f19di_f19_dilution_intensity_isssmooth_base_v070_signal,
    f19di_f19_dilution_intensity_issperaddsh_base_v071_signal,
    f19di_f19_dilution_intensity_dilspeed_base_v072_signal,
    f19di_f19_dilution_intensity_waspread_mom_base_v073_signal,
    f19di_f19_dilution_intensity_dildrag_504d_base_v074_signal,
    f19di_f19_dilution_intensity_overhangdil_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_DILUTION_INTENSITY_REGISTRY_001_075 = REGISTRY


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
    # ncfcommon = net common cash flow (capital returned minus capital raised); swings sign.
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

    print("OK f19_dilution_intensity_base_001_075_claude: %d features pass" % n_features)
