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
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


# ===== f39 dilution-trap domain primitives =====
# price-strength driver
def _f39_mom(closeadj, w):
    # log momentum over w days
    return np.log(closeadj.replace(0, np.nan) / closeadj.shift(w).replace(0, np.nan))


def _f39_prox_high(closeadj, w):
    hi = closeadj.rolling(w, min_periods=max(1, w // 2)).max()
    return closeadj / hi.replace(0, np.nan)


def _f39_rngpos(closeadj, w):
    hi = closeadj.rolling(w, min_periods=max(1, w // 2)).max()
    lo = closeadj.rolling(w, min_periods=max(1, w // 2)).min()
    return (closeadj - lo) / (hi - lo).replace(0, np.nan)


def _f39_volz(volume, w):
    # volume surge z-score vs rolling baseline
    return _z(volume, w)


def _f39_volsurge(volume, wshort, wlong):
    a = volume.rolling(wshort, min_periods=max(1, wshort // 2)).mean()
    b = volume.rolling(wlong, min_periods=max(1, wlong // 2)).mean()
    return a / b.replace(0, np.nan)


def _f39_dollar_vol(closeadj, volume):
    return closeadj * volume


# fundamental dilution driver
def _f39_share_growth(sharesbas, w):
    # log share-count growth = dilution rate over w days
    return np.log(sharesbas.replace(0, np.nan) / sharesbas.shift(w).replace(0, np.nan))


def _f39_share_accel(sharesbas, w):
    g = np.log(sharesbas.replace(0, np.nan) / sharesbas.shift(w).replace(0, np.nan))
    return g - g.shift(w)


def _f39_issuance(ncfcommon):
    # equity raise proxy: net cash raised from common issuance (-ncfcommon convention
    # per family spec: -ncfcommon as raise).
    return -ncfcommon


def _f39_issue_intensity(ncfcommon, closeadj, volume, w):
    # raise scaled by traded dollar value (issuance into liquidity)
    raise_ = (-ncfcommon).rolling(w, min_periods=max(1, w // 2)).mean()
    dv = (closeadj * volume).rolling(w, min_periods=max(1, w // 2)).mean()
    return raise_ / dv.replace(0, np.nan)


# ============================================================
# CORE TRAP: share-growth into price strength (the canonical pump-and-dilute).
def f39dx_f39_dilution_trap_detector_trapcore_252d_base_v001_signal(sharesbas, closeadj):
    dil = _f39_share_growth(sharesbas, 252)
    strength = _f39_prox_high(closeadj, 252)
    b = dil * strength
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance-into-strength: equity raise magnitude gated by price momentum
def f39dx_f39_dilution_trap_detector_issuestr_126d_base_v002_signal(ncfcommon, closeadj):
    iss = _z(_f39_issuance(ncfcommon), 252)
    mom = _f39_mom(closeadj, 126)
    b = iss * mom.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap distance: how far price-strength and dilution are jointly elevated (z-product)
def f39dx_f39_dilution_trap_detector_trapdist_252d_base_v003_signal(sharesbas, closeadj):
    dz = _z(_f39_share_growth(sharesbas, 252), 252)
    pz = _z(_f39_mom(closeadj, 252), 252)
    b = dz * pz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-surge confirmed dilution: share growth weighted by volume surge
def f39dx_f39_dilution_trap_detector_volconfdil_63d_base_v004_signal(sharesbas, volume):
    dil = _f39_share_growth(sharesbas, 63)
    surge = _f39_volsurge(volume, 21, 126)
    b = dil * surge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pump-and-dilute coincidence: dilution rate times short-horizon price spike
def f39dx_f39_dilution_trap_detector_pumpdil_63d_base_v005_signal(sharesbas, closeadj):
    dil = _f39_share_growth(sharesbas, 63)
    spike = _f39_mom(closeadj, 21)
    b = dil * spike.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance into a 52w-high regime (raise when price near the high)
def f39dx_f39_dilution_trap_detector_issuehigh_252d_base_v006_signal(ncfcommon, closeadj):
    iss = _z(_f39_issuance(ncfcommon), 252)
    near_hi = _f39_prox_high(closeadj, 252)
    b = iss * near_hi
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise/dollar-volume intensity (issuance absorbed into traded liquidity)
def f39dx_f39_dilution_trap_detector_issintdv_126d_base_v007_signal(ncfcommon, closeadj, volume):
    b = _f39_issue_intensity(ncfcommon, closeadj, volume, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap interaction across three drivers: dilution x momentum x volume surge
def f39dx_f39_dilution_trap_detector_triple_63d_base_v008_signal(sharesbas, closeadj, volume):
    dil = _z(_f39_share_growth(sharesbas, 126), 252)
    mom = _z(_f39_mom(closeadj, 63), 126)
    vs = _z(_f39_volsurge(volume, 21, 126), 126)
    b = dil * mom * vs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution rank gated by range-position (high-in-range dilution)
def f39dx_f39_dilution_trap_detector_dilrankrng_252d_base_v009_signal(sharesbas, closeadj):
    dr = _rank(_f39_share_growth(sharesbas, 252), 504)
    rp = _f39_rngpos(closeadj, 252)
    b = dr * (rp - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-issuance acceleration meeting price acceleration
def f39dx_f39_dilution_trap_detector_accelmatch_126d_base_v010_signal(sharesbas, closeadj):
    sa = _f39_share_accel(sharesbas, 126)
    pa = _f39_mom(closeadj, 63) - _f39_mom(closeadj, 63).shift(63)
    b = sa * pa
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net issuance z (level) interacted with risk-adjusted momentum
def f39dx_f39_dilution_trap_detector_issriskmom_126d_base_v011_signal(ncfcommon, closeadj):
    iss = _z(_f39_issuance(ncfcommon), 252)
    mom = _f39_mom(closeadj, 126)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    ramom = mom / vol.replace(0, np.nan)
    b = iss * ramom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap streak: fraction of last year with simultaneous dilution + price strength
def f39dx_f39_dilution_trap_detector_trapstreak_252d_base_v012_signal(sharesbas, closeadj):
    dil = _f39_share_growth(sharesbas, 63)
    mom = _f39_mom(closeadj, 63)
    both = ((dil > 0) & (mom > 0)).astype(float)
    b = both.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution z minus momentum z (divergence: diluting while weak vs strong)
def f39dx_f39_dilution_trap_detector_dilmomspr_252d_base_v013_signal(sharesbas, closeadj):
    dz = _z(_f39_share_growth(sharesbas, 252), 252)
    pz = _z(_f39_mom(closeadj, 252), 252)
    b = dz - pz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance-into-strength flag weighted by raise size
def f39dx_f39_dilution_trap_detector_issflag_126d_base_v014_signal(ncfcommon, closeadj):
    raise_ = (-ncfcommon).rolling(63, min_periods=21).mean()
    raise_z = _z(raise_, 252)
    strong = (_f39_mom(closeadj, 63) > 0).astype(float)
    b = raise_z * strong
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share growth per unit of price momentum (dilution-to-pump ratio)
def f39dx_f39_dilution_trap_detector_dilperpump_126d_base_v015_signal(sharesbas, closeadj):
    dil = _f39_share_growth(sharesbas, 126)
    mom = _f39_mom(closeadj, 126).abs()
    b = dil / (mom + 0.05)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume surge during share issuance (liquidity-funded dilution)
def f39dx_f39_dilution_trap_detector_dvsurgeiss_63d_base_v016_signal(ncfcommon, closeadj, volume):
    dv = _f39_dollar_vol(closeadj, volume)
    dvz = _z(dv, 126)
    iss = _z(_f39_issuance(ncfcommon), 252)
    b = dvz * iss
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap distance using range-position instead of momentum
def f39dx_f39_dilution_trap_detector_trapdistrp_504d_base_v017_signal(sharesbas, closeadj):
    dz = _z(_f39_share_growth(sharesbas, 252), 252)
    rp = _f39_rngpos(closeadj, 504) - 0.5
    b = dz * rp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative dilution over the cycle weighted by being above the 252d mean
def f39dx_f39_dilution_trap_detector_cumdilhi_252d_base_v018_signal(sharesbas, closeadj):
    cumdil = _f39_share_growth(sharesbas, 252)
    above = (closeadj > _mean(closeadj, 252)).astype(float)
    b = cumdil * above
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance frequency: count of quarters with positive raise, weighted by strength
def f39dx_f39_dilution_trap_detector_issfreq_252d_base_v019_signal(ncfcommon, closeadj):
    raise_q = (-ncfcommon).rolling(63, min_periods=21).mean()
    pos = (raise_q > 0).astype(float)
    freq = pos.rolling(252, min_periods=126).mean()
    strong = _f39_prox_high(closeadj, 252)
    b = freq * strong
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted dilution surprise: dilution z scaled by current vol surge
def f39dx_f39_dilution_trap_detector_dilvolwt_126d_base_v020_signal(sharesbas, volume):
    dz = _z(_f39_share_growth(sharesbas, 126), 252)
    vs = _f39_volsurge(volume, 5, 63)
    b = dz * vs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price spike unaccompanied by dilution (clean strength) -> negative trap signal
def f39dx_f39_dilution_trap_detector_cleanstr_126d_base_v021_signal(sharesbas, closeadj):
    mom = _z(_f39_mom(closeadj, 126), 252)
    nodil = (-_z(_f39_share_growth(sharesbas, 126), 252)).clip(lower=0)
    b = mom * nodil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance into strength measured against trailing dilution baseline (excess dilution)
def f39dx_f39_dilution_trap_detector_exdil_252d_base_v022_signal(sharesbas, closeadj):
    g = _f39_share_growth(sharesbas, 63)
    base = g.rolling(252, min_periods=126).mean()
    excess = g - base
    strong = _f39_prox_high(closeadj, 252)
    b = excess * strong
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap magnitude: tanh-squashed product of dilution and momentum (bounded)
def f39dx_f39_dilution_trap_detector_traptanh_126d_base_v023_signal(sharesbas, closeadj):
    dz = _z(_f39_share_growth(sharesbas, 126), 252)
    pz = _z(_f39_mom(closeadj, 126), 252)
    b = np.tanh(dz * pz)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise-funded run: cumulative issuance vs cumulative return, ratio
def f39dx_f39_dilution_trap_detector_raisefund_252d_base_v024_signal(ncfcommon, closeadj):
    cumraise = (-ncfcommon).rolling(252, min_periods=126).sum()
    cumret = (closeadj / closeadj.shift(252).replace(0, np.nan) - 1.0)
    b = np.sign(cumret) * _z(cumraise, 504) * cumret.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution while making new highs (count of new-high days during share growth)
def f39dx_f39_dilution_trap_detector_newhidil_252d_base_v025_signal(sharesbas, closeadj):
    hi = closeadj.rolling(252, min_periods=126).max()
    new_hi = (closeadj >= hi * 0.999).astype(float)
    diluting = (_f39_share_growth(sharesbas, 21) > 0).astype(float)
    coincide = (new_hi * diluting).rolling(252, min_periods=126).sum()
    b = coincide
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance-into-strength persistence (EMA of the gated raise)
def f39dx_f39_dilution_trap_detector_isspersist_126d_base_v026_signal(ncfcommon, closeadj):
    iss = _z(_f39_issuance(ncfcommon), 252)
    strong = _f39_prox_high(closeadj, 126)
    gated = iss * strong
    b = gated.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-trap distance from a 'safe' baseline (low dilution + weak price)
def f39dx_f39_dilution_trap_detector_safedist_252d_base_v027_signal(sharesbas, closeadj):
    dz = _z(_f39_share_growth(sharesbas, 252), 252).clip(lower=0)
    pz = _z(_f39_mom(closeadj, 252), 252).clip(lower=0)
    b = np.sqrt(dz ** 2 + pz ** 2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume surge concentrated on issuance quarters (Herfindahl-like surge focus)
def f39dx_f39_dilution_trap_detector_surgefocus_63d_base_v028_signal(ncfcommon, volume):
    raise_ = (-ncfcommon)
    raisez = _z(raise_, 252).clip(lower=0)
    vs = _f39_volsurge(volume, 21, 126)
    b = raisez * (vs - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-growth slope sign times price slope sign (co-movement regime)
def f39dx_f39_dilution_trap_detector_comove_126d_base_v029_signal(sharesbas, closeadj):
    sg = _f39_share_growth(sharesbas, 63)
    pg = _f39_mom(closeadj, 63)
    co = np.sign(sg) * np.sign(pg)
    b = co.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap onset: rising dilution AND rising price over the same quarter
def f39dx_f39_dilution_trap_detector_onset_63d_base_v030_signal(sharesbas, closeadj):
    dil_now = _f39_share_growth(sharesbas, 63)
    dil_prev = _f39_share_growth(sharesbas, 63).shift(63)
    mom_now = _f39_mom(closeadj, 63)
    mom_prev = _f39_mom(closeadj, 63).shift(63)
    rising = ((dil_now > dil_prev).astype(float) * (mom_now > mom_prev).astype(float))
    b = rising * (dil_now + mom_now)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution intensity per dollar of market activity, ranked
def f39dx_f39_dilution_trap_detector_dilintrank_126d_base_v031_signal(sharesbas, closeadj, volume):
    dil = _f39_share_growth(sharesbas, 126)
    dv = _z(_f39_dollar_vol(closeadj, volume), 126)
    intensity = dil * dv
    b = _rank(intensity, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance-into-strength angle (atan2 of raise vs momentum)
def f39dx_f39_dilution_trap_detector_issangle_126d_base_v032_signal(ncfcommon, closeadj):
    iss = _z(_f39_issuance(ncfcommon), 252)
    mom = _z(_f39_mom(closeadj, 126), 252)
    b = np.arctan2(iss, mom.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution that survives a strong-price filter: only count growth while near highs
def f39dx_f39_dilution_trap_detector_dilnearhi_252d_base_v033_signal(sharesbas, closeadj):
    g = _f39_share_growth(sharesbas, 21)
    near = (_f39_prox_high(closeadj, 252) > 0.85).astype(float)
    filtered = (g * near).rolling(252, min_periods=126).sum()
    b = filtered
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise-to-momentum elasticity: change in shares vs change in price (slope-of-slopes)
def f39dx_f39_dilution_trap_detector_elastic_126d_base_v034_signal(sharesbas, closeadj):
    ds = _f39_share_growth(sharesbas, 21)
    dp = _f39_mom(closeadj, 21)
    cov = (ds * dp).rolling(126, min_periods=42).mean()
    var = (dp * dp).rolling(126, min_periods=42).mean()
    b = cov / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap z combining dilution-accel and volume-surge
def f39dx_f39_dilution_trap_detector_accelvol_126d_base_v035_signal(sharesbas, volume):
    sa = _z(_f39_share_accel(sharesbas, 63), 252)
    vs = _z(_f39_volsurge(volume, 21, 126), 126)
    b = sa * vs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of dollar-volume 'consumed' by issuance over the quarter
def f39dx_f39_dilution_trap_detector_dvconsume_63d_base_v036_signal(ncfcommon, closeadj, volume):
    raise_ = (-ncfcommon).rolling(63, min_periods=21).sum().clip(lower=0)
    dv = _f39_dollar_vol(closeadj, volume).rolling(63, min_periods=21).sum()
    b = raise_ / dv.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-trap composite score (weighted sum of standardized drivers)
def f39dx_f39_dilution_trap_detector_composite_252d_base_v037_signal(sharesbas, ncfcommon, closeadj):
    dz = _z(_f39_share_growth(sharesbas, 252), 252)
    iz = _z(_f39_issuance(ncfcommon), 252)
    pz = _z(_f39_mom(closeadj, 252), 252)
    b = 0.4 * dz + 0.3 * iz + 0.3 * pz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap with mean-reversion overlay: trap score minus its own quarter-ago value
def f39dx_f39_dilution_trap_detector_trapchg_252d_base_v038_signal(sharesbas, closeadj):
    trap = _z(_f39_share_growth(sharesbas, 252), 252) * _z(_f39_mom(closeadj, 126), 252)
    b = trap - trap.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance into strength, but penalized by subsequent weakness (trap confirmation)
def f39dx_f39_dilution_trap_detector_confirm_126d_base_v039_signal(ncfcommon, closeadj):
    iss = _z(_f39_issuance(ncfcommon), 252)
    fwd_proxy = -_f39_mom(closeadj, 21)  # recent reversal as trap confirmation
    b = iss.shift(21) * fwd_proxy
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-growth dispersion (lumpy raises) times price strength
def f39dx_f39_dilution_trap_detector_lumpy_126d_base_v040_signal(sharesbas, closeadj):
    g = _f39_share_growth(sharesbas, 21)
    disp = g.rolling(126, min_periods=42).std()
    strong = _f39_prox_high(closeadj, 126)
    b = disp * strong
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise gated by 52w-range-position rank (issue into upper-range)
def f39dx_f39_dilution_trap_detector_issrngrank_252d_base_v041_signal(ncfcommon, closeadj):
    iss = _rank(_f39_issuance(ncfcommon), 504)
    rp = _f39_rngpos(closeadj, 252)
    b = iss * (rp - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution acceleration during a price blowoff (vertical run)
def f39dx_f39_dilution_trap_detector_blowoffdil_63d_base_v042_signal(sharesbas, closeadj):
    sa = _f39_share_accel(sharesbas, 63)
    stretch = closeadj / _mean(closeadj, 21).replace(0, np.nan) - 1.0
    b = sa * stretch.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap intensity normalized by realized vol (trap per unit risk)
def f39dx_f39_dilution_trap_detector_traprisk_126d_base_v043_signal(sharesbas, closeadj):
    trap = _f39_share_growth(sharesbas, 126) * _f39_mom(closeadj, 126).clip(lower=0)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = trap / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of issuance-into-strength events over the year
def f39dx_f39_dilution_trap_detector_eventcount_252d_base_v044_signal(ncfcommon, closeadj):
    raise_pos = (-ncfcommon).rolling(21, min_periods=10).mean() > 0
    mom21 = _f39_mom(closeadj, 21)
    strong = mom21 > 0.05
    event = (raise_pos & strong).astype(float)
    entries = ((event == 1) & (event.shift(1) == 0)).astype(float)
    # magnitude-weight each onset by the strength at onset -> continuous
    weighted = (entries * mom21.clip(lower=0))
    b = weighted.rolling(252, min_periods=126).sum() + 0.01 * entries.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution share of dollar-volume z, smoothed
def f39dx_f39_dilution_trap_detector_dilshare_126d_base_v045_signal(sharesbas, closeadj, volume):
    dil = _f39_share_growth(sharesbas, 63)
    dvz = _z(_f39_dollar_vol(closeadj, volume), 252)
    raw = dil * dvz
    b = raw.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# price-strength minus dilution-adjusted strength (dilution drag on the run)
def f39dx_f39_dilution_trap_detector_dildrag_252d_base_v046_signal(sharesbas, closeadj):
    raw_mom = _f39_mom(closeadj, 252)
    dil = _f39_share_growth(sharesbas, 252)
    per_share_mom = raw_mom - dil  # value-per-share momentum after dilution
    b = raw_mom - per_share_mom  # equals dilution; weighted by sign of momentum
    b = b * np.sign(raw_mom)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance-into-strength rank product (both extreme high)
def f39dx_f39_dilution_trap_detector_rankprod_252d_base_v047_signal(ncfcommon, closeadj):
    ir = _rank(_f39_issuance(ncfcommon), 504) + 0.5
    pr = _rank(_f39_mom(closeadj, 252), 504) + 0.5
    b = ir * pr - 0.25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution into volume-surge regime (count of high-vol diluting days)
def f39dx_f39_dilution_trap_detector_volregdil_252d_base_v048_signal(sharesbas, volume):
    diluting = (_f39_share_growth(sharesbas, 21) > 0).astype(float)
    high_vol = (_f39_volz(volume, 63) > 1.0).astype(float)
    coincide = (diluting * high_vol).rolling(252, min_periods=126).mean()
    b = coincide
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap distance using long-horizon (504d) drivers
def f39dx_f39_dilution_trap_detector_trapdist_504b_base_v049_signal(sharesbas, closeadj):
    dz = _z(_f39_share_growth(sharesbas, 504), 504)
    pz = _z(_f39_mom(closeadj, 504), 504)
    b = dz * pz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise magnitude relative to share base growth (cash raised per new share)
def f39dx_f39_dilution_trap_detector_cashpershare_126d_base_v050_signal(ncfcommon, sharesbas):
    raise_ = (-ncfcommon).rolling(63, min_periods=21).mean()
    new_shares = sharesbas.diff(63).abs()
    eff = raise_ / new_shares.replace(0, np.nan)
    b = _z(eff, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap pressure: dilution z weighted by how stretched price is above 63d MA
def f39dx_f39_dilution_trap_detector_pressure_63d_base_v051_signal(sharesbas, closeadj):
    dz = _z(_f39_share_growth(sharesbas, 126), 252)
    stretch = closeadj / _mean(closeadj, 63).replace(0, np.nan) - 1.0
    b = dz * stretch
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance-into-strength with volume confirmation (triple-gate count)
def f39dx_f39_dilution_trap_detector_triplegate_252d_base_v052_signal(ncfcommon, closeadj, volume):
    raise_pos = (-ncfcommon).rolling(21, min_periods=10).mean() > 0
    strong = _f39_mom(closeadj, 21) > 0
    surge = _f39_volz(volume, 63) > 0.5
    gate = (raise_pos & strong & surge).astype(float)
    b = gate.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-trap z minus its long-run average (regime-relative trap)
def f39dx_f39_dilution_trap_detector_trapregime_504d_base_v053_signal(sharesbas, closeadj):
    trap = _f39_share_growth(sharesbas, 126) * _f39_mom(closeadj, 126)
    b = trap - trap.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share growth correlated with returns over rolling window (raise-on-rally beta)
def f39dx_f39_dilution_trap_detector_raisecorr_252d_base_v054_signal(sharesbas, closeadj):
    sg = _f39_share_growth(sharesbas, 21)
    ret = closeadj.pct_change(21)
    sgz = _z(sg, 252)
    retz = _z(ret, 252)
    b = (sgz * retz).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absolute issuance scaled by price level (dilution affordability proxy)
def f39dx_f39_dilution_trap_detector_issaffrd_126d_base_v055_signal(ncfcommon, closeadj):
    raise_ = (-ncfcommon).rolling(63, min_periods=21).mean()
    b = _z(raise_, 252) * np.log(closeadj.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap with prox-low context: diluting near lows is desperation, not a pump (sign flip)
def f39dx_f39_dilution_trap_detector_desperation_252d_base_v056_signal(sharesbas, closeadj):
    dil = _z(_f39_share_growth(sharesbas, 126), 252)
    rp = _f39_rngpos(closeadj, 252)
    # positive when diluting high (trap), negative when diluting low (desperation)
    b = dil * (2.0 * rp - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share growth vs volume surge divergence (dilution without volume = quiet dilution)
def f39dx_f39_dilution_trap_detector_quietdil_126d_base_v057_signal(sharesbas, volume):
    dz = _z(_f39_share_growth(sharesbas, 126), 252)
    vz = _z(_f39_volsurge(volume, 21, 126), 126)
    b = dz - vz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap acceleration: change in trapcore over a quarter
def f39dx_f39_dilution_trap_detector_trapaccel_252d_base_v058_signal(sharesbas, closeadj):
    trap = _f39_share_growth(sharesbas, 252) * _f39_prox_high(closeadj, 252)
    b = trap - trap.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise-into-strength normalized by issuance volatility (clean signal)
def f39dx_f39_dilution_trap_detector_issnorm_126d_base_v059_signal(ncfcommon, closeadj):
    raise_ = (-ncfcommon)
    raisez = (raise_ - raise_.rolling(252, min_periods=126).mean()) / \
        raise_.rolling(252, min_periods=126).std().replace(0, np.nan)
    strong = _f39_mom(closeadj, 63).clip(lower=0)
    b = raisez * strong
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of months where shares grew >2% while price up (aggressive-dilution tally)
def f39dx_f39_dilution_trap_detector_aggrcount_252d_base_v060_signal(sharesbas, closeadj):
    mg = _f39_share_growth(sharesbas, 21)
    up = _f39_mom(closeadj, 21) > 0
    aggressive = ((mg > 0.02) & up).astype(float)
    b = aggressive.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-adjusted momentum gap (raw momentum minus per-share momentum), ranked
def f39dx_f39_dilution_trap_detector_psgaprank_252d_base_v061_signal(sharesbas, closeadj):
    raw = _f39_mom(closeadj, 252)
    persh = raw - _f39_share_growth(sharesbas, 252)
    gap = raw - persh
    b = _rank(gap, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance pulse times short-term reversal (pump-then-fade trap)
def f39dx_f39_dilution_trap_detector_pumpfade_63d_base_v062_signal(ncfcommon, closeadj):
    pulse = _z((-ncfcommon).rolling(21, min_periods=10).mean(), 252)
    run = _f39_mom(closeadj, 63).clip(lower=0)
    fade = (-_f39_mom(closeadj, 5)).clip(lower=0)
    b = pulse * run * fade
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-trap distance scaled by volume concentration
def f39dx_f39_dilution_trap_detector_volconcdist_126d_base_v063_signal(sharesbas, closeadj, volume):
    dz = _z(_f39_share_growth(sharesbas, 126), 252)
    pz = _z(_f39_mom(closeadj, 126), 252)
    vol_share = volume / volume.rolling(126, min_periods=63).sum().replace(0, np.nan)
    b = dz * pz * (vol_share * 126.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap signature: high dilution-rank AND high momentum-rank both above 0.7
def f39dx_f39_dilution_trap_detector_dualextreme_252d_base_v064_signal(sharesbas, closeadj):
    dr = _rank(_f39_share_growth(sharesbas, 252), 504) + 0.5
    pr = _rank(_f39_mom(closeadj, 252), 504) + 0.5
    both = ((dr > 0.7) & (pr > 0.7)).astype(float)
    b = both.rolling(126, min_periods=63).mean() + 0.1 * dr * pr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance vs prior-year issuance change, gated by strength (escalating dilution)
def f39dx_f39_dilution_trap_detector_escalate_252d_base_v065_signal(ncfcommon, closeadj):
    raise_ = (-ncfcommon).rolling(63, min_periods=21).mean()
    escalation = raise_ - raise_.shift(252)
    strong = _f39_prox_high(closeadj, 252)
    b = _z(escalation, 252) * strong
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-growth times dollar-volume momentum (liquidity-pump dilution)
def f39dx_f39_dilution_trap_detector_dvmomdil_126d_base_v066_signal(sharesbas, closeadj, volume):
    dil = _z(_f39_share_growth(sharesbas, 126), 252)
    dv = _f39_dollar_vol(closeadj, volume)
    dvmom = np.log(dv.rolling(21, min_periods=10).mean().replace(0, np.nan) /
                   dv.rolling(126, min_periods=63).mean().replace(0, np.nan))
    b = dil * dvmom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap half-life proxy: time since last simultaneous dilution+strength peak
def f39dx_f39_dilution_trap_detector_traprecency_252d_base_v067_signal(sharesbas, closeadj):
    trap = (_f39_share_growth(sharesbas, 63) * _f39_mom(closeadj, 63)).clip(lower=0)

    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = trap.rolling(252, min_periods=126).apply(_dsh, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-issuance-funded price gain: cumret per cumulative dollar raised
def f39dx_f39_dilution_trap_detector_fundeff_252d_base_v068_signal(ncfcommon, closeadj):
    cumraise = (-ncfcommon).rolling(252, min_periods=126).sum().clip(lower=0)
    cumret = closeadj / closeadj.shift(252).replace(0, np.nan) - 1.0
    b = cumret / (_z(cumraise, 504).abs() + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution trap with volatility-expansion confirmation
def f39dx_f39_dilution_trap_detector_volexpdil_126d_base_v069_signal(sharesbas, closeadj):
    dz = _z(_f39_share_growth(sharesbas, 126), 252)
    volshort = closeadj.pct_change().rolling(21, min_periods=10).std()
    vollong = closeadj.pct_change().rolling(126, min_periods=63).std()
    expand = volshort / vollong.replace(0, np.nan)
    b = dz * (expand - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise-on-strength minus raise-on-weakness (issuance timing skew)
def f39dx_f39_dilution_trap_detector_timeskew_252d_base_v070_signal(ncfcommon, closeadj):
    raise_ = _z((-ncfcommon).rolling(21, min_periods=10).mean(), 252)
    up = (_f39_mom(closeadj, 21) > 0).astype(float)
    on_str = (raise_ * up).rolling(252, min_periods=126).mean()
    on_weak = (raise_ * (1 - up)).rolling(252, min_periods=126).mean()
    b = on_str - on_weak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap intensity: product of dilution-z, momentum-z, volume-z, squashed
def f39dx_f39_dilution_trap_detector_intensity_126d_base_v071_signal(sharesbas, closeadj, volume):
    dz = _z(_f39_share_growth(sharesbas, 126), 252)
    pz = _z(_f39_mom(closeadj, 63), 126)
    vz = _z(_f39_volsurge(volume, 21, 126), 126)
    raw = dz * pz * vz
    b = np.sign(raw) * np.log1p(raw.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-strength coincidence over multi-year (1260d trap distance)
def f39dx_f39_dilution_trap_detector_trapdist_1260d_base_v072_signal(sharesbas, closeadj):
    dz = _z(_f39_share_growth(sharesbas, 504), 504)
    pz = _z(_f39_mom(closeadj, 504), 504)
    b = (dz + pz) * np.sign(dz * pz)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance into strength relative to peers-of-self (self-rank of gated signal)
def f39dx_f39_dilution_trap_detector_selfrank_126d_base_v073_signal(ncfcommon, closeadj):
    iss = _z(_f39_issuance(ncfcommon), 252)
    strong = _f39_prox_high(closeadj, 126)
    gated = iss * strong
    b = _rank(gated, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap-vs-clean balance: (trap days - clean-strength days)/(total) over the year
def f39dx_f39_dilution_trap_detector_trapbalance_252d_base_v074_signal(sharesbas, closeadj):
    up = _f39_mom(closeadj, 21) > 0
    diluting = _f39_share_growth(sharesbas, 21) > 0
    trap_d = (up & diluting).astype(float).rolling(252, min_periods=126).sum()
    clean_d = (up & ~diluting).astype(float).rolling(252, min_periods=126).sum()
    b = (trap_d - clean_d) / (trap_d + clean_d).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative dilution-weighted overextension (trap exhaustion proxy)
def f39dx_f39_dilution_trap_detector_exhaust_252d_base_v075_signal(sharesbas, closeadj):
    cumdil = _f39_share_growth(sharesbas, 252)
    overext = (closeadj / _mean(closeadj, 252).replace(0, np.nan) - 1.0)
    b = cumdil * overext.clip(lower=0) * np.sign(cumdil)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f39dx_f39_dilution_trap_detector_trapcore_252d_base_v001_signal,
    f39dx_f39_dilution_trap_detector_issuestr_126d_base_v002_signal,
    f39dx_f39_dilution_trap_detector_trapdist_252d_base_v003_signal,
    f39dx_f39_dilution_trap_detector_volconfdil_63d_base_v004_signal,
    f39dx_f39_dilution_trap_detector_pumpdil_63d_base_v005_signal,
    f39dx_f39_dilution_trap_detector_issuehigh_252d_base_v006_signal,
    f39dx_f39_dilution_trap_detector_issintdv_126d_base_v007_signal,
    f39dx_f39_dilution_trap_detector_triple_63d_base_v008_signal,
    f39dx_f39_dilution_trap_detector_dilrankrng_252d_base_v009_signal,
    f39dx_f39_dilution_trap_detector_accelmatch_126d_base_v010_signal,
    f39dx_f39_dilution_trap_detector_issriskmom_126d_base_v011_signal,
    f39dx_f39_dilution_trap_detector_trapstreak_252d_base_v012_signal,
    f39dx_f39_dilution_trap_detector_dilmomspr_252d_base_v013_signal,
    f39dx_f39_dilution_trap_detector_issflag_126d_base_v014_signal,
    f39dx_f39_dilution_trap_detector_dilperpump_126d_base_v015_signal,
    f39dx_f39_dilution_trap_detector_dvsurgeiss_63d_base_v016_signal,
    f39dx_f39_dilution_trap_detector_trapdistrp_504d_base_v017_signal,
    f39dx_f39_dilution_trap_detector_cumdilhi_252d_base_v018_signal,
    f39dx_f39_dilution_trap_detector_issfreq_252d_base_v019_signal,
    f39dx_f39_dilution_trap_detector_dilvolwt_126d_base_v020_signal,
    f39dx_f39_dilution_trap_detector_cleanstr_126d_base_v021_signal,
    f39dx_f39_dilution_trap_detector_exdil_252d_base_v022_signal,
    f39dx_f39_dilution_trap_detector_traptanh_126d_base_v023_signal,
    f39dx_f39_dilution_trap_detector_raisefund_252d_base_v024_signal,
    f39dx_f39_dilution_trap_detector_newhidil_252d_base_v025_signal,
    f39dx_f39_dilution_trap_detector_isspersist_126d_base_v026_signal,
    f39dx_f39_dilution_trap_detector_safedist_252d_base_v027_signal,
    f39dx_f39_dilution_trap_detector_surgefocus_63d_base_v028_signal,
    f39dx_f39_dilution_trap_detector_comove_126d_base_v029_signal,
    f39dx_f39_dilution_trap_detector_onset_63d_base_v030_signal,
    f39dx_f39_dilution_trap_detector_dilintrank_126d_base_v031_signal,
    f39dx_f39_dilution_trap_detector_issangle_126d_base_v032_signal,
    f39dx_f39_dilution_trap_detector_dilnearhi_252d_base_v033_signal,
    f39dx_f39_dilution_trap_detector_elastic_126d_base_v034_signal,
    f39dx_f39_dilution_trap_detector_accelvol_126d_base_v035_signal,
    f39dx_f39_dilution_trap_detector_dvconsume_63d_base_v036_signal,
    f39dx_f39_dilution_trap_detector_composite_252d_base_v037_signal,
    f39dx_f39_dilution_trap_detector_trapchg_252d_base_v038_signal,
    f39dx_f39_dilution_trap_detector_confirm_126d_base_v039_signal,
    f39dx_f39_dilution_trap_detector_lumpy_126d_base_v040_signal,
    f39dx_f39_dilution_trap_detector_issrngrank_252d_base_v041_signal,
    f39dx_f39_dilution_trap_detector_blowoffdil_63d_base_v042_signal,
    f39dx_f39_dilution_trap_detector_traprisk_126d_base_v043_signal,
    f39dx_f39_dilution_trap_detector_eventcount_252d_base_v044_signal,
    f39dx_f39_dilution_trap_detector_dilshare_126d_base_v045_signal,
    f39dx_f39_dilution_trap_detector_dildrag_252d_base_v046_signal,
    f39dx_f39_dilution_trap_detector_rankprod_252d_base_v047_signal,
    f39dx_f39_dilution_trap_detector_volregdil_252d_base_v048_signal,
    f39dx_f39_dilution_trap_detector_trapdist_504b_base_v049_signal,
    f39dx_f39_dilution_trap_detector_cashpershare_126d_base_v050_signal,
    f39dx_f39_dilution_trap_detector_pressure_63d_base_v051_signal,
    f39dx_f39_dilution_trap_detector_triplegate_252d_base_v052_signal,
    f39dx_f39_dilution_trap_detector_trapregime_504d_base_v053_signal,
    f39dx_f39_dilution_trap_detector_raisecorr_252d_base_v054_signal,
    f39dx_f39_dilution_trap_detector_issaffrd_126d_base_v055_signal,
    f39dx_f39_dilution_trap_detector_desperation_252d_base_v056_signal,
    f39dx_f39_dilution_trap_detector_quietdil_126d_base_v057_signal,
    f39dx_f39_dilution_trap_detector_trapaccel_252d_base_v058_signal,
    f39dx_f39_dilution_trap_detector_issnorm_126d_base_v059_signal,
    f39dx_f39_dilution_trap_detector_aggrcount_252d_base_v060_signal,
    f39dx_f39_dilution_trap_detector_psgaprank_252d_base_v061_signal,
    f39dx_f39_dilution_trap_detector_pumpfade_63d_base_v062_signal,
    f39dx_f39_dilution_trap_detector_volconcdist_126d_base_v063_signal,
    f39dx_f39_dilution_trap_detector_dualextreme_252d_base_v064_signal,
    f39dx_f39_dilution_trap_detector_escalate_252d_base_v065_signal,
    f39dx_f39_dilution_trap_detector_dvmomdil_126d_base_v066_signal,
    f39dx_f39_dilution_trap_detector_traprecency_252d_base_v067_signal,
    f39dx_f39_dilution_trap_detector_fundeff_252d_base_v068_signal,
    f39dx_f39_dilution_trap_detector_volexpdil_126d_base_v069_signal,
    f39dx_f39_dilution_trap_detector_timeskew_252d_base_v070_signal,
    f39dx_f39_dilution_trap_detector_intensity_126d_base_v071_signal,
    f39dx_f39_dilution_trap_detector_trapdist_1260d_base_v072_signal,
    f39dx_f39_dilution_trap_detector_selfrank_126d_base_v073_signal,
    f39dx_f39_dilution_trap_detector_trapbalance_252d_base_v074_signal,
    f39dx_f39_dilution_trap_detector_exhaust_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F39_DILUTION_TRAP_DETECTOR_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

    def _fund(seed, base=1e8, drift=0.0, vol=0.08, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.5
        return pd.Series(s, name=None)

    # sharesbas: positive, growing (juniors dilute) -> upward drift
    sharesbas = _fund(101, base=5e7, drift=0.06, vol=0.10).rename("sharesbas")
    # ncfcommon: net cash from common; allow negative (raises = positive inflow,
    # buybacks/returns = negative). allow_neg=True per spec.
    ncfcommon = _fund(77, base=2e7, drift=0.0, vol=2.5, allow_neg=True).rename("ncfcommon")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume,
            "sharesbas": sharesbas, "ncfcommon": ncfcommon}

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

    print("OK f39_dilution_trap_detector_base_001_075_claude: %d features pass" % n_features)
