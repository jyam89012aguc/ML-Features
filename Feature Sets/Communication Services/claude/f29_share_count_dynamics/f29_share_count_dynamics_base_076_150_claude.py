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
    return shares / shares.shift(w).replace(0, np.nan) - 1.0


def _f29_logdilution(shares, w):
    return np.log(shares.replace(0, np.nan) / shares.shift(w).replace(0, np.nan))


def _f29_issuance(ncfcommon):
    # raise = -ncfcommon (positive when company nets equity inflow); buyback = +ncfcommon
    return -ncfcommon


def _f29_buyback(ncfcommon):
    return ncfcommon.clip(lower=0)


def _f29_raise_pos(ncfcommon):
    return _f29_issuance(ncfcommon).clip(lower=0)


# ============================================================
# half-year basic dilution z-scored vs own 504d history (de-trended issuance pace)
def f29sc_f29_share_count_dynamics_dilbasz_126d_base_v076_signal(sharesbas):
    d = _f29_logdilution(sharesbas, 126)
    b = _z(d, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# monthly dilution percentile-ranked vs 252d history (relative issuance burst)
def f29sc_f29_share_count_dynamics_dilrank_21d_base_v077_signal(sharesbas):
    d = _f29_dilution(sharesbas, 21)
    b = d.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net capital flow EMA over 126d, scaled (smoothed issuance/buyback regime)
def f29sc_f29_share_count_dynamics_flowema_126d_base_v078_signal(ncfcommon):
    raise_ = _f29_issuance(ncfcommon)
    ema = raise_.ewm(span=126, min_periods=42).mean()
    scale = raise_.abs().rolling(252, min_periods=63).mean()
    b = ema / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 2y diluted-share dilution z-scored vs own 252d (long overhang extremity)
def f29sc_f29_share_count_dynamics_dildilz_504d_base_v079_signal(shareswadil):
    d = _f29_logdilution(shareswadil, 504)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback persistence: fraction of last year in net-repurchase quarters
def f29sc_f29_share_count_dynamics_bbpersist_252d_base_v080_signal(ncfcommon):
    bb = (ncfcommon.rolling(63, min_periods=21).sum() > 0).astype(float)
    b = bb.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# meaningful-raise frequency: fraction of last year with quarterly raises above the
# trailing typical raise size (only sizeable equity raises count, not noise)
def f29sc_f29_share_count_dynamics_isspersist_252d_base_v081_signal(ncfcommon):
    qraise = _f29_issuance(ncfcommon).rolling(63, min_periods=21).sum()
    thr = qraise.abs().rolling(252, min_periods=126).median()
    big = (qraise > thr).astype(float)
    b = big.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count log-level slope over 252d (trend of float expansion)
def f29sc_f29_share_count_dynamics_lvlslope_252d_base_v082_signal(sharesbas):
    ls = np.log(sharesbas.replace(0, np.nan))
    b = (ls - ls.shift(252)) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted creep relative to 504d mean creep (overhang vs typical)
def f29sc_f29_share_count_dynamics_creepdist_504d_base_v083_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    b = sp - sp.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-to-creep coupling: do float and option pool grow together? (63d corr)
def f29sc_f29_share_count_dynamics_couple_252d_base_v084_signal(sharesbas, shareswadil):
    db = _f29_dilution(sharesbas, 21)
    dd = _f29_dilution(shareswadil, 21)
    b = db.rolling(252, min_periods=126).corr(dd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net issuance per share base over 126d (semiannual raise intensity)
def f29sc_f29_share_count_dynamics_isspershare_126d_base_v085_signal(ncfcommon, sharesbas):
    raise_ = _f29_issuance(ncfcommon).rolling(126, min_periods=42).sum()
    b = raise_ / sharesbas.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution streak depth: consecutive-rise length x average rise magnitude
def f29sc_f29_share_count_dynamics_streakmag_base_v086_signal(sharesbas):
    d = sharesbas.diff()
    up = (d > 0).astype(float)
    grp = (up != up.shift(1)).cumsum()
    run = up.groupby(grp).cumsum() * up
    mag = sharesbas.pct_change().clip(lower=0).rolling(21, min_periods=5).mean()
    b = (run / 252.0) * mag * 100.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5y dilution trajectory: 1260d weighted-avg dilution minus its value a year ago
# (is the multi-year dilution pace itself accelerating or fading?)
def f29sc_f29_share_count_dynamics_dilwa_1260d_base_v087_signal(shareswa):
    d = _f29_logdilution(shareswa, 1008)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-flow regime distance: 252d net flow minus its 504d median, scaled
def f29sc_f29_share_count_dynamics_flowregime_base_v088_signal(ncfcommon):
    flow = _f29_issuance(ncfcommon).rolling(252, min_periods=63).sum()
    scale = _f29_issuance(ncfcommon).abs().rolling(252, min_periods=63).sum()
    r = flow / scale.replace(0, np.nan)
    b = r - r.rolling(504, min_periods=126).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution skew: skewness of monthly share-growth over a year (offering lumpiness)
def f29sc_f29_share_count_dynamics_dilskew_252d_base_v089_signal(sharesbas):
    m = _f29_dilution(sharesbas, 21)
    b = m.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution kurtosis: tail-heaviness of monthly share growth (event-driven issuance)
def f29sc_f29_share_count_dynamics_dilkurt_252d_base_v090_signal(sharesbas):
    m = _f29_dilution(sharesbas, 21)
    b = m.rolling(252, min_periods=126).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback dominance over 504d: repurchase dollars as a share of total capital activity
# (mature return-of-capital posture vs raising), float-independent
def f29sc_f29_share_count_dynamics_bbpershare_504d_base_v091_signal(ncfcommon):
    bb = _f29_buyback(ncfcommon).rolling(504, min_periods=126).sum()
    gross = ncfcommon.abs().rolling(504, min_periods=126).sum()
    b = bb / gross.replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# creep momentum: change in diluted creep over a half-year
def f29sc_f29_share_count_dynamics_creepmom_126d_base_v092_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    b = sp - sp.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-growth efficiency ratio: net 252d dilution vs total path traveled (directedness)
def f29sc_f29_share_count_dynamics_dileff_252d_base_v093_signal(sharesbas):
    net = (sharesbas - sharesbas.shift(252)).abs()
    path = sharesbas.diff().abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net dilution adjusted for buybacks: 252d float growth minus normalized buyback
def f29sc_f29_share_count_dynamics_netdilbb_252d_base_v094_signal(sharesbas, ncfcommon):
    dil = _f29_dilution(sharesbas, 252)
    bb = _f29_buyback(ncfcommon).rolling(252, min_periods=63).sum()
    base = sharesbas.rolling(252, min_periods=63).mean()
    b = dil - bb / (base * 10.0).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted dilution minus 2x basic dilution (option-pool over-expansion flag, magnitude)
def f29sc_f29_share_count_dynamics_overexp_252d_base_v095_signal(shareswadil, shareswa):
    dd = _f29_logdilution(shareswadil, 252)
    db = _f29_logdilution(shareswa, 252)
    b = dd - 2.0 * db
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance burst magnitude: max 21d raise within 252d scaled by mean raise
def f29sc_f29_share_count_dynamics_issburstmag_252d_base_v096_signal(ncfcommon):
    raise21 = _f29_issuance(ncfcommon).rolling(21, min_periods=5).sum()
    peak = raise21.rolling(252, min_periods=63).max()
    scale = _f29_issuance(ncfcommon).abs().rolling(252, min_periods=63).mean()
    b = peak / (scale * 21.0).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# float-expansion curvature: log-level second difference across three 84d nodes
# (is the cumulative-dilution curve bending up = accelerating issuance, or flattening?)
def f29sc_f29_share_count_dynamics_dilconvex_base_v097_signal(sharesbas):
    ls = np.log(sharesbas.replace(0, np.nan))
    b = ls - 2.0 * ls.shift(84) + ls.shift(168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-avg vs diluted growth gap percentile-ranked (relative overhang build)
def f29sc_f29_share_count_dynamics_draprank_252d_base_v098_signal(shareswadil, shareswa):
    dd = _f29_logdilution(shareswadil, 126)
    db = _f29_logdilution(shareswa, 126)
    gap = dd - db
    b = gap.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash raised per unit of cumulative dilution over 1260d (capital efficiency of dilution)
# high => each new share fetched lots of cash; low => cheap/heavy paper dilution
def f29sc_f29_share_count_dynamics_raisestock_1260d_base_v099_signal(ncfcommon, sharesbas):
    raise_ = _f29_raise_pos(ncfcommon).rolling(1260, min_periods=252).sum()
    dil = _f29_logdilution(sharesbas, 1260).clip(lower=0)
    scale = _f29_issuance(ncfcommon).abs().rolling(1260, min_periods=252).mean()
    b = (raise_ / scale.replace(0, np.nan)) / (dil * 1000.0 + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution drawup vs 252d trough scaled by elapsed time (issuance velocity off trough)
def f29sc_f29_share_count_dynamics_drawvel_252d_base_v100_signal(sharesbas):
    lo = sharesbas.rolling(252, min_periods=63).min()
    draw = sharesbas / lo.replace(0, np.nan) - 1.0

    def _dsince_min(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a)) + 1e-6

    age = sharesbas.rolling(252, min_periods=63).apply(_dsince_min, raw=True)
    b = draw / age
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 2y the float made a new 252d high (relentless-dilution regime)
def f29sc_f29_share_count_dynamics_relentless_504d_base_v101_signal(sharesbas):
    hi = sharesbas.shift(1).rolling(252, min_periods=63).max()
    newhi = (sharesbas > hi).astype(float)
    b = newhi.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-issuance flow trend slope over 252d (financing direction tilt)
def f29sc_f29_share_count_dynamics_flowslope_252d_base_v102_signal(ncfcommon):
    flow = _f29_issuance(ncfcommon)
    scale = flow.abs().rolling(252, min_periods=63).mean()
    r = (flow / scale.replace(0, np.nan))
    b = r.ewm(span=42, min_periods=21).mean() - r.ewm(span=189, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-creep z-score vs own 504d history (overhang extremity)
def f29sc_f29_share_count_dynamics_creepz_504d_base_v103_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    b = _z(sp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# typical-month capital posture over 504d: median normalized monthly net flow (robust)
# distinct from magnitude-weighted sums -- captures the central tendency, not the tails
def f29sc_f29_share_count_dynamics_netregime_504d_base_v104_signal(ncfcommon):
    flow = _f29_issuance(ncfcommon)
    scale = flow.abs().rolling(252, min_periods=63).mean()
    r = flow / scale.replace(0, np.nan)
    b = r.rolling(504, min_periods=126).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count quarterly growth dispersion vs annual mean (instability of issuance)
def f29sc_f29_share_count_dynamics_dilinstab_252d_base_v105_signal(sharesbas):
    q = _f29_dilution(sharesbas, 63)
    sd = q.rolling(252, min_periods=126).std()
    mn = q.rolling(252, min_periods=126).mean().abs()
    b = sd / (mn + 1e-6)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# standardized overhang wedge: diluted-share growth z minus basic-share growth z (126d)
# normalizes each leg by its own variability before differencing (de-scaled drag)
def f29sc_f29_share_count_dynamics_dilshortdrag_126d_base_v106_signal(shareswadil, shareswa):
    dd = _z(_f29_logdilution(shareswadil, 126), 252)
    db = _z(_f29_logdilution(shareswa, 126), 252)
    b = dd - db
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance recency intensity: time-decayed sum of raises over 252d (recent raises weigh more)
def f29sc_f29_share_count_dynamics_issdecay_252d_base_v107_signal(ncfcommon, sharesbas):
    raise_ = _f29_raise_pos(ncfcommon)
    decayed = raise_.ewm(span=63, min_periods=21).mean()
    b = decayed / sharesbas.replace(0, np.nan) * 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# float-vs-weighted divergence: sharesbas/shareswa ratio z-scored (point-in-time issuance lead)
def f29sc_f29_share_count_dynamics_basvswaz_252d_base_v108_signal(sharesbas, shareswa):
    sp = sharesbas / shareswa.replace(0, np.nan)
    b = _z(sp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution acceleration over 126d (half-year dilution minus prior half-year)
def f29sc_f29_share_count_dynamics_dilaccel_126d_base_v109_signal(sharesbas):
    d = _f29_dilution(sharesbas, 126)
    b = d - d.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net capital flow x dilution sign agreement (cash-backed dilution confirmation)
def f29sc_f29_share_count_dynamics_cashback_252d_base_v110_signal(sharesbas, ncfcommon):
    dil = _f29_dilution(sharesbas, 252)
    flow = _f29_issuance(ncfcommon).rolling(252, min_periods=63).sum()
    scale = _f29_issuance(ncfcommon).abs().rolling(252, min_periods=63).sum()
    rn = flow / scale.replace(0, np.nan)
    b = np.sign(dil) * np.sign(rn) * (dil.abs() * rn.abs()) ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count max single-quarter dilution within 504d (worst issuance episode)
def f29sc_f29_share_count_dynamics_worstdil_504d_base_v111_signal(sharesbas):
    q = _f29_dilution(sharesbas, 63)
    b = q.rolling(504, min_periods=126).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted creep convexity: 63d creep change vs half of 126d creep change
def f29sc_f29_share_count_dynamics_creepconvex_base_v112_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    c63 = sp - sp.shift(63)
    c126 = sp - sp.shift(126)
    b = c63 - 0.5 * c126
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback-funded shrink: net float change during buyback-heavy years (negative=shrink)
def f29sc_f29_share_count_dynamics_bbfundshrink_504d_base_v113_signal(sharesbas, ncfcommon):
    bbshare = (_f29_buyback(ncfcommon).rolling(504, min_periods=126).sum()
               / _f29_issuance(ncfcommon).abs().rolling(504, min_periods=126).sum().replace(0, np.nan))
    dil = _f29_logdilution(sharesbas, 504)
    b = dil * bbshare
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution regime persistence: longest run of rising-share months in 252d, normalized
def f29sc_f29_share_count_dynamics_maxstreak_252d_base_v114_signal(sharesbas):
    up = (_f29_dilution(sharesbas, 21) > 0).astype(float)
    grp = (up != up.shift(1)).cumsum()
    run = up.groupby(grp).cumsum() * up
    b = run.rolling(252, min_periods=126).max() / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-avg dilution minus 5y average dilution (long-run regime distance)
def f29sc_f29_share_count_dynamics_dillongdist_base_v115_signal(shareswa):
    d = _f29_logdilution(shareswa, 252)
    b = d - d.rolling(1260, min_periods=504).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance vs buyback turnover: total absolute capital flow / |net| (churn vs direction)
def f29sc_f29_share_count_dynamics_flowchurn_252d_base_v116_signal(ncfcommon):
    gross = ncfcommon.abs().rolling(252, min_periods=63).sum()
    net = ncfcommon.rolling(252, min_periods=63).sum().abs()
    b = gross / (net + 1e-3 * gross).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-creep slope over 252d (rate of overhang build)
def f29sc_f29_share_count_dynamics_creepslope_252d_base_v117_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    b = (sp - sp.shift(252)) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# float-level percentile within 504d (how high current share count ranks historically)
def f29sc_f29_share_count_dynamics_lvlmeddist_504d_base_v118_signal(sharesbas):
    b = sharesbas.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise intensity dispersion: std of monthly raises over a year (lumpy financing)
def f29sc_f29_share_count_dynamics_issdisp_252d_base_v119_signal(ncfcommon):
    raise_ = _f29_issuance(ncfcommon)
    scale = raise_.abs().rolling(252, min_periods=63).mean()
    r = raise_ / scale.replace(0, np.nan)
    b = r.rolling(252, min_periods=126).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net dilution per dollar raised: float growth divided by normalized cash raised (price of dilution)
def f29sc_f29_share_count_dynamics_dilperdollar_252d_base_v120_signal(sharesbas, ncfcommon):
    dil = _f29_dilution(sharesbas, 252)
    raise_ = _f29_raise_pos(ncfcommon).rolling(252, min_periods=63).sum()
    scale = _f29_issuance(ncfcommon).abs().rolling(252, min_periods=63).sum()
    rn = raise_ / scale.replace(0, np.nan)
    b = dil / (rn + 0.05)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-share new-high frequency over a quarter (option-pool relentlessly expanding)
def f29sc_f29_share_count_dynamics_dilnewhi_63d_base_v121_signal(shareswadil):
    hi = shareswadil.rolling(252, min_periods=126).max()
    ish = (shareswadil >= hi * 0.99999).astype(float)
    b = ish.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance shock recency: months since last >2% monthly float jump, normalized
def f29sc_f29_share_count_dynamics_shockrecency_252d_base_v122_signal(sharesbas):
    big = (_f29_dilution(sharesbas, 21) > 0.02).astype(float)

    def _dsince(a):
        idx = np.where(a > 0)[0]
        if len(idx) == 0:
            return 1.0
        return (len(a) - 1 - idx[-1]) / float(len(a))

    b = big.rolling(252, min_periods=126).apply(_dsince, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted vs basic creep change z-scored (overhang-build extremity)
def f29sc_f29_share_count_dynamics_creepchgz_base_v123_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    chg = sp - sp.shift(126)
    b = _z(chg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-base 504d log-growth minus 252d log-growth (long minus short dilution wedge)
def f29sc_f29_share_count_dynamics_dilwedge_base_v124_signal(sharesbas):
    d504 = _f29_logdilution(sharesbas, 504)
    d252 = _f29_logdilution(sharesbas, 252)
    b = d504 - d252
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# buyback magnitude smoothed vs issuance magnitude smoothed (net capital posture EMA)
def f29sc_f29_share_count_dynamics_posture_base_v125_signal(ncfcommon):
    bb = _f29_buyback(ncfcommon).ewm(span=126, min_periods=42).mean()
    iss = _f29_raise_pos(ncfcommon).ewm(span=126, min_periods=42).mean()
    b = (bb - iss) / (bb + iss).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution acceleration z-scored (issuance pace inflection extremity)
def f29sc_f29_share_count_dynamics_dilaccelz_base_v126_signal(sharesbas):
    d = _f29_dilution(sharesbas, 252)
    acc = d - d.shift(126)
    b = _z(acc, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count autocorrelation of monthly growth (issuance momentum vs mean-revert)
def f29sc_f29_share_count_dynamics_dilautocorr_base_v127_signal(sharesbas):
    g = _f29_dilution(sharesbas, 21)
    b = g.rolling(252, min_periods=126).corr(g.shift(21))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise-funded dilution share: float growth attributable to cash-raise quarters
def f29sc_f29_share_count_dynamics_raisefund_252d_base_v128_signal(sharesbas, ncfcommon):
    issshare = (_f29_raise_pos(ncfcommon).rolling(252, min_periods=63).sum()
                / _f29_issuance(ncfcommon).abs().rolling(252, min_periods=63).sum().replace(0, np.nan))
    dil = _f29_logdilution(sharesbas, 252)
    b = dil * issshare
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-creep range over 504d (max minus min overhang span)
def f29sc_f29_share_count_dynamics_creeprange_504d_base_v129_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    b = sp.rolling(504, min_periods=252).max() - sp.rolling(504, min_periods=252).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# float-growth quarter momentum minus annual mean (sequential vs trailing pace)
def f29sc_f29_share_count_dynamics_seqgap_63d_base_v130_signal(sharesbas):
    q = _f29_dilution(sharesbas, 63)
    a = _f29_dilution(sharesbas, 252) / 4.0
    b = q - a
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-avg share dilution percentile vs 1260d history (long relative dilution)
def f29sc_f29_share_count_dynamics_dilwaprank_1260d_base_v131_signal(shareswa):
    d = _f29_logdilution(shareswa, 252)
    b = d.rolling(1260, min_periods=504).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net capital flow cumulative-vs-trend gap over 504d (financing drift)
def f29sc_f29_share_count_dynamics_flowdrift_504d_base_v132_signal(ncfcommon):
    cum = _f29_issuance(ncfcommon).cumsum()
    trend = cum.rolling(504, min_periods=126).mean()
    scale = _f29_issuance(ncfcommon).abs().rolling(504, min_periods=126).sum()
    b = (cum - trend) / scale.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-deceleration depth: how far below its 126d peak the dilution pace has fallen
def f29sc_f29_share_count_dynamics_dilcooldown_base_v133_signal(sharesbas):
    d = _f29_dilution(sharesbas, 63)
    peak = d.rolling(126, min_periods=42).max()
    b = (peak - d).clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined overhang severity: diluted creep level x basic-dilution pace
def f29sc_f29_share_count_dynamics_severity_252d_base_v134_signal(shareswadil, shareswa, sharesbas):
    creep = shareswadil / shareswa.replace(0, np.nan) - 1.0
    pace = _f29_dilution(sharesbas, 252).clip(lower=0)
    b = creep * pace * 10.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance burst entry count weighted by depth (offering events in last 2y)
def f29sc_f29_share_count_dynamics_offerings_504d_base_v135_signal(sharesbas):
    big = (_f29_dilution(sharesbas, 21) > 0.025).astype(float)
    entries = ((big == 1) & (big.shift(1) == 0)).astype(float)
    depth = (_f29_dilution(sharesbas, 21) - 0.025).clip(lower=0)
    b = entries.rolling(504, min_periods=252).sum() + 40.0 * depth.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted growth vs basic growth ratio over 504d (sustained amplification factor)
def f29sc_f29_share_count_dynamics_amplify_504d_base_v136_signal(shareswadil, shareswa):
    dd = _f29_logdilution(shareswadil, 504)
    db = _f29_logdilution(shareswa, 504)
    b = dd / db.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net buyback intensity z-scored vs own 504d history (repurchase extremity)
def f29sc_f29_share_count_dynamics_bbz_504d_base_v137_signal(ncfcommon):
    bb = _f29_buyback(ncfcommon).rolling(252, min_periods=63).sum()
    scale = ncfcommon.abs().rolling(252, min_periods=63).sum()
    r = bb / scale.replace(0, np.nan)
    b = _z(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-count drawdown from peak (rare buyback-driven shrink below 504d high)
def f29sc_f29_share_count_dynamics_floatshrink_504d_base_v138_signal(sharesbas):
    hi = sharesbas.rolling(504, min_periods=126).max()
    b = sharesbas / hi.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted creep tanh-bounded momentum (overhang-build shock)
def f29sc_f29_share_count_dynamics_creeptanh_base_v139_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    chg = sp - sp.shift(63)
    b = np.tanh(50.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-growth sign-balance over a year (net dilution direction breadth)
def f29sc_f29_share_count_dynamics_dilbalance_252d_base_v140_signal(sharesbas):
    d = sharesbas.diff()
    up = (d > 0).astype(float)
    dn = (d < 0).astype(float)
    b = (up.rolling(252, min_periods=126).sum() - dn.rolling(252, min_periods=126).sum()) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capital-raise dependence: cumulative 504d raise relative to float scale, ranked
def f29sc_f29_share_count_dynamics_raiserank_504d_base_v141_signal(ncfcommon, sharesbas):
    raise_ = _f29_raise_pos(ncfcommon).rolling(504, min_periods=126).sum()
    r = raise_ / sharesbas.replace(0, np.nan)
    b = r.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-vs-basic gap acceleration (overhang build second difference)
def f29sc_f29_share_count_dynamics_gapaccel_base_v142_signal(shareswadil, shareswa):
    gap = (shareswadil - shareswa) / shareswa.replace(0, np.nan)
    v = gap - gap.shift(126)
    b = v - v.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short vs long dilution term-structure ratio (63d vs 252d float growth)
def f29sc_f29_share_count_dynamics_dilterm_63v252_base_v143_signal(sharesbas):
    s = _f29_logdilution(sharesbas, 63)
    l = _f29_logdilution(sharesbas, 252)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net flow regime distance over 252d minus 1260d typical (multi-year financing distance)
def f29sc_f29_share_count_dynamics_flowmydist_base_v144_signal(ncfcommon):
    flow = _f29_issuance(ncfcommon).rolling(252, min_periods=63).sum()
    scale = _f29_issuance(ncfcommon).abs().rolling(252, min_periods=63).sum()
    r = flow / scale.replace(0, np.nan)
    b = r - r.rolling(1260, min_periods=504).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted-creep stability: inverse of 252d creep-change volatility (steady overhang)
def f29sc_f29_share_count_dynamics_creepstab_252d_base_v145_signal(shareswadil, shareswa):
    sp = shareswadil / shareswa.replace(0, np.nan) - 1.0
    ch = sp.diff(21)
    sd = ch.rolling(252, min_periods=126).std()
    b = 1.0 / (1.0 + 1000.0 * sd.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative buyback minus cumulative raise over 1260d, share-scaled (long net return)
def f29sc_f29_share_count_dynamics_netreturn_1260d_base_v146_signal(ncfcommon, sharesbas):
    bb = _f29_buyback(ncfcommon).rolling(1260, min_periods=252).sum()
    iss = _f29_raise_pos(ncfcommon).rolling(1260, min_periods=252).sum()
    b = (bb - iss) / sharesbas.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# float-growth jerk-as-level: change in 126d dilution acceleration (issuance impulse)
def f29sc_f29_share_count_dynamics_dilimpulse_base_v147_signal(sharesbas):
    d = _f29_dilution(sharesbas, 63)
    acc = d - d.shift(63)
    b = acc - acc.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# diluted creep vs basic-dilution sign divergence (overhang building while float flat)
def f29sc_f29_share_count_dynamics_silentcreep_252d_base_v148_signal(shareswadil, shareswa, sharesbas):
    creep_chg = (shareswadil / shareswa.replace(0, np.nan) - 1.0)
    creep_chg = creep_chg - creep_chg.shift(252)
    floatgrow = _f29_dilution(sharesbas, 252)
    b = creep_chg * (1.0 - np.tanh(50.0 * floatgrow.abs()))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net dilution rank vs 1260d history (where current float-growth sits long-run)
def f29sc_f29_share_count_dynamics_dilmyrank_base_v149_signal(sharesbas):
    d = _f29_logdilution(sharesbas, 252)
    b = d.rolling(1260, min_periods=504).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite share-count pressure: net flow posture x diluted creep level x float pace
def f29sc_f29_share_count_dynamics_composite_252d_base_v150_signal(ncfcommon, shareswadil, shareswa, sharesbas):
    flow = _f29_issuance(ncfcommon).rolling(252, min_periods=63).sum()
    scale = _f29_issuance(ncfcommon).abs().rolling(252, min_periods=63).sum()
    rn = np.tanh(2.0 * flow / scale.replace(0, np.nan))
    creep = _z(shareswadil / shareswa.replace(0, np.nan) - 1.0, 252)
    pace = _z(_f29_dilution(sharesbas, 252), 252)
    b = (rn + creep + pace) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f29sc_f29_share_count_dynamics_dilbasz_126d_base_v076_signal,
    f29sc_f29_share_count_dynamics_dilrank_21d_base_v077_signal,
    f29sc_f29_share_count_dynamics_flowema_126d_base_v078_signal,
    f29sc_f29_share_count_dynamics_dildilz_504d_base_v079_signal,
    f29sc_f29_share_count_dynamics_bbpersist_252d_base_v080_signal,
    f29sc_f29_share_count_dynamics_isspersist_252d_base_v081_signal,
    f29sc_f29_share_count_dynamics_lvlslope_252d_base_v082_signal,
    f29sc_f29_share_count_dynamics_creepdist_504d_base_v083_signal,
    f29sc_f29_share_count_dynamics_couple_252d_base_v084_signal,
    f29sc_f29_share_count_dynamics_isspershare_126d_base_v085_signal,
    f29sc_f29_share_count_dynamics_streakmag_base_v086_signal,
    f29sc_f29_share_count_dynamics_dilwa_1260d_base_v087_signal,
    f29sc_f29_share_count_dynamics_flowregime_base_v088_signal,
    f29sc_f29_share_count_dynamics_dilskew_252d_base_v089_signal,
    f29sc_f29_share_count_dynamics_dilkurt_252d_base_v090_signal,
    f29sc_f29_share_count_dynamics_bbpershare_504d_base_v091_signal,
    f29sc_f29_share_count_dynamics_creepmom_126d_base_v092_signal,
    f29sc_f29_share_count_dynamics_dileff_252d_base_v093_signal,
    f29sc_f29_share_count_dynamics_netdilbb_252d_base_v094_signal,
    f29sc_f29_share_count_dynamics_overexp_252d_base_v095_signal,
    f29sc_f29_share_count_dynamics_issburstmag_252d_base_v096_signal,
    f29sc_f29_share_count_dynamics_dilconvex_base_v097_signal,
    f29sc_f29_share_count_dynamics_draprank_252d_base_v098_signal,
    f29sc_f29_share_count_dynamics_raisestock_1260d_base_v099_signal,
    f29sc_f29_share_count_dynamics_drawvel_252d_base_v100_signal,
    f29sc_f29_share_count_dynamics_relentless_504d_base_v101_signal,
    f29sc_f29_share_count_dynamics_flowslope_252d_base_v102_signal,
    f29sc_f29_share_count_dynamics_creepz_504d_base_v103_signal,
    f29sc_f29_share_count_dynamics_netregime_504d_base_v104_signal,
    f29sc_f29_share_count_dynamics_dilinstab_252d_base_v105_signal,
    f29sc_f29_share_count_dynamics_dilshortdrag_126d_base_v106_signal,
    f29sc_f29_share_count_dynamics_issdecay_252d_base_v107_signal,
    f29sc_f29_share_count_dynamics_basvswaz_252d_base_v108_signal,
    f29sc_f29_share_count_dynamics_dilaccel_126d_base_v109_signal,
    f29sc_f29_share_count_dynamics_cashback_252d_base_v110_signal,
    f29sc_f29_share_count_dynamics_worstdil_504d_base_v111_signal,
    f29sc_f29_share_count_dynamics_creepconvex_base_v112_signal,
    f29sc_f29_share_count_dynamics_bbfundshrink_504d_base_v113_signal,
    f29sc_f29_share_count_dynamics_maxstreak_252d_base_v114_signal,
    f29sc_f29_share_count_dynamics_dillongdist_base_v115_signal,
    f29sc_f29_share_count_dynamics_flowchurn_252d_base_v116_signal,
    f29sc_f29_share_count_dynamics_creepslope_252d_base_v117_signal,
    f29sc_f29_share_count_dynamics_lvlmeddist_504d_base_v118_signal,
    f29sc_f29_share_count_dynamics_issdisp_252d_base_v119_signal,
    f29sc_f29_share_count_dynamics_dilperdollar_252d_base_v120_signal,
    f29sc_f29_share_count_dynamics_dilnewhi_63d_base_v121_signal,
    f29sc_f29_share_count_dynamics_shockrecency_252d_base_v122_signal,
    f29sc_f29_share_count_dynamics_creepchgz_base_v123_signal,
    f29sc_f29_share_count_dynamics_dilwedge_base_v124_signal,
    f29sc_f29_share_count_dynamics_posture_base_v125_signal,
    f29sc_f29_share_count_dynamics_dilaccelz_base_v126_signal,
    f29sc_f29_share_count_dynamics_dilautocorr_base_v127_signal,
    f29sc_f29_share_count_dynamics_raisefund_252d_base_v128_signal,
    f29sc_f29_share_count_dynamics_creeprange_504d_base_v129_signal,
    f29sc_f29_share_count_dynamics_seqgap_63d_base_v130_signal,
    f29sc_f29_share_count_dynamics_dilwaprank_1260d_base_v131_signal,
    f29sc_f29_share_count_dynamics_flowdrift_504d_base_v132_signal,
    f29sc_f29_share_count_dynamics_dilcooldown_base_v133_signal,
    f29sc_f29_share_count_dynamics_severity_252d_base_v134_signal,
    f29sc_f29_share_count_dynamics_offerings_504d_base_v135_signal,
    f29sc_f29_share_count_dynamics_amplify_504d_base_v136_signal,
    f29sc_f29_share_count_dynamics_bbz_504d_base_v137_signal,
    f29sc_f29_share_count_dynamics_floatshrink_504d_base_v138_signal,
    f29sc_f29_share_count_dynamics_creeptanh_base_v139_signal,
    f29sc_f29_share_count_dynamics_dilbalance_252d_base_v140_signal,
    f29sc_f29_share_count_dynamics_raiserank_504d_base_v141_signal,
    f29sc_f29_share_count_dynamics_gapaccel_base_v142_signal,
    f29sc_f29_share_count_dynamics_dilterm_63v252_base_v143_signal,
    f29sc_f29_share_count_dynamics_flowmydist_base_v144_signal,
    f29sc_f29_share_count_dynamics_creepstab_252d_base_v145_signal,
    f29sc_f29_share_count_dynamics_netreturn_1260d_base_v146_signal,
    f29sc_f29_share_count_dynamics_dilimpulse_base_v147_signal,
    f29sc_f29_share_count_dynamics_silentcreep_252d_base_v148_signal,
    f29sc_f29_share_count_dynamics_dilmyrank_base_v149_signal,
    f29sc_f29_share_count_dynamics_composite_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F29_SHARE_COUNT_DYNAMICS_REGISTRY_076_150 = REGISTRY


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

    _sb = np.random.default_rng(101)
    _drift = np.repeat(_sb.normal(0.02, 0.06, n // 63 + 1), 63)[:n] / 63.0
    _jumps = np.zeros(n)
    _jidx = _sb.choice(np.arange(63, n), size=34, replace=False)
    _jumps[_jidx] = _sb.uniform(0.008, 0.06, size=34)
    sharesbas = pd.Series(1.2e8 * np.exp(np.cumsum(_drift + _jumps)), name="sharesbas")
    shareswa = sharesbas.rolling(63, min_periods=1).mean().rename("shareswa")

    _cr = np.random.default_rng(103)
    _creep = 0.05 + 0.03 * np.sin(np.linspace(0, 7.0, n)) + np.cumsum(
        _cr.normal(0, 0.0015, n))
    _creep = np.clip(_creep, 0.005, 0.20)
    shareswadil = (shareswa * (1.0 + _creep)).rename("shareswadil")

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

    print("OK f29_share_count_dynamics_base_076_150_claude: %d features pass" % n_features)
