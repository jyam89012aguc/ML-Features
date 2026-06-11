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
def _f39_mom(closeadj, w):
    return np.log(closeadj.replace(0, np.nan) / closeadj.shift(w).replace(0, np.nan))


def _f39_prox_high(closeadj, w):
    hi = closeadj.rolling(w, min_periods=max(1, w // 2)).max()
    return closeadj / hi.replace(0, np.nan)


def _f39_rngpos(closeadj, w):
    hi = closeadj.rolling(w, min_periods=max(1, w // 2)).max()
    lo = closeadj.rolling(w, min_periods=max(1, w // 2)).min()
    return (closeadj - lo) / (hi - lo).replace(0, np.nan)


def _f39_volz(volume, w):
    return _z(volume, w)


def _f39_volsurge(volume, wshort, wlong):
    a = volume.rolling(wshort, min_periods=max(1, wshort // 2)).mean()
    b = volume.rolling(wlong, min_periods=max(1, wlong // 2)).mean()
    return a / b.replace(0, np.nan)


def _f39_dollar_vol(closeadj, volume):
    return closeadj * volume


def _f39_share_growth(sharesbas, w):
    return np.log(sharesbas.replace(0, np.nan) / sharesbas.shift(w).replace(0, np.nan))


def _f39_share_accel(sharesbas, w):
    g = np.log(sharesbas.replace(0, np.nan) / sharesbas.shift(w).replace(0, np.nan))
    return g - g.shift(w)


def _f39_issuance(ncfcommon):
    # equity raise proxy: -ncfcommon as raise (family spec convention)
    return -ncfcommon


# ============================================================
# trap core on a half-year horizon (price strength x dilution), z-product
def f39dx_f39_dilution_trap_detector_trapcore_126d_base_v076_signal(sharesbas, closeadj):
    dz = _z(_f39_share_growth(sharesbas, 126), 252)
    sz = _z(_f39_prox_high(closeadj, 126), 252)
    b = dz * sz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance into strength on a monthly horizon
def f39dx_f39_dilution_trap_detector_issuestr_21d_base_v077_signal(ncfcommon, closeadj):
    iss = _z(_f39_issuance(ncfcommon), 126)
    mom = _f39_mom(closeadj, 21)
    b = iss * mom.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-rate slope interacted with momentum sign (escalating dilution into rally)
def f39dx_f39_dilution_trap_detector_dilslopemom_126d_base_v078_signal(sharesbas, closeadj):
    g = _f39_share_growth(sharesbas, 63)
    slope = g - g.shift(63)
    momsign = np.sign(_f39_mom(closeadj, 63))
    b = slope * momsign
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap distance with a soft-floor (only positive-dilution, positive-momentum corner)
def f39dx_f39_dilution_trap_detector_corner_252d_base_v079_signal(sharesbas, closeadj):
    dz = _z(_f39_share_growth(sharesbas, 252), 252).clip(lower=0)
    pz = _z(_f39_mom(closeadj, 252), 252).clip(lower=0)
    b = dz * pz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-surge times dilution accel (news-pump dilution)
def f39dx_f39_dilution_trap_detector_newspumpdil_63d_base_v080_signal(sharesbas, volume):
    sa = _z(_f39_share_accel(sharesbas, 63), 252)
    vs = _f39_volsurge(volume, 5, 63)
    b = sa * (vs - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance into a fresh 504d high (anchor-fresh raise)
def f39dx_f39_dilution_trap_detector_freshhigh_504d_base_v081_signal(ncfcommon, closeadj):
    iss = _z(_f39_issuance(ncfcommon), 252)
    hi252 = _rmax(closeadj, 252)
    hi504 = _rmax(closeadj, 504)
    fresh = (hi252 / hi504.replace(0, np.nan))
    b = iss * fresh
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise per share-base, gated by range-position
def f39dx_f39_dilution_trap_detector_raisepershr_126d_base_v082_signal(ncfcommon, sharesbas, closeadj):
    raise_ = (-ncfcommon).rolling(63, min_periods=21).mean()
    per_shr = raise_ / sharesbas.replace(0, np.nan)
    rp = _f39_rngpos(closeadj, 126)
    b = _z(per_shr, 252) * (rp - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap triple on a long horizon (252d drivers)
def f39dx_f39_dilution_trap_detector_triple_252d_base_v083_signal(sharesbas, closeadj, volume):
    dz = _z(_f39_share_growth(sharesbas, 252), 504)
    pz = _z(_f39_mom(closeadj, 252), 504)
    vz = _z(_f39_volsurge(volume, 63, 252), 252)
    b = dz * pz * vz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-rank minus momentum-rank (which driver leads the trap)
def f39dx_f39_dilution_trap_detector_leadlag_252d_base_v084_signal(sharesbas, closeadj):
    dr = _rank(_f39_share_growth(sharesbas, 252), 504)
    pr = _rank(_f39_mom(closeadj, 252), 504)
    b = dr - pr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-accel meets volume-accel (joint surge)
def f39dx_f39_dilution_trap_detector_jointaccel_126d_base_v085_signal(sharesbas, volume):
    sa = _z(_f39_share_accel(sharesbas, 63), 252)
    va = _z(volume.rolling(21, min_periods=10).mean()
            - volume.rolling(21, min_periods=10).mean().shift(63), 126)
    b = sa * va
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance acceleration times downside-vol expansion (raise-pulse before a fall)
def f39dx_f39_dilution_trap_detector_issdown_126d_base_v086_signal(ncfcommon, closeadj):
    raise_ = (-ncfcommon).rolling(21, min_periods=10).mean()
    iss_pulse = raise_ - raise_.shift(63)  # change in raise pace, not level
    iss_pulse = _z(iss_pulse, 252)
    ret = closeadj.pct_change()
    dshort = ret.clip(upper=0).rolling(21, min_periods=10).std()
    dlong = ret.clip(upper=0).rolling(126, min_periods=63).std()
    downexp = dshort / dlong.replace(0, np.nan) - 1.0
    b = iss_pulse * downexp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap streak on a 126d window (recent persistence)
def f39dx_f39_dilution_trap_detector_trapstreak_126d_base_v087_signal(sharesbas, closeadj):
    dil = _f39_share_growth(sharesbas, 21)
    mom = _f39_mom(closeadj, 21)
    both = ((dil > 0) & (mom > 0)).astype(float)
    raw = both.rolling(126, min_periods=63).mean()
    depth = (dil.clip(lower=0) * mom.clip(lower=0)).rolling(63, min_periods=21).mean()
    b = raw + 5.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution z plus momentum z (additive trap, distinct from multiplicative)
def f39dx_f39_dilution_trap_detector_addtrap_126d_base_v088_signal(sharesbas, closeadj):
    dz = _z(_f39_share_growth(sharesbas, 126), 252)
    pz = _z(_f39_mom(closeadj, 126), 252)
    b = dz + pz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise-into-strength flag, count of flagged months over the year (weighted)
def f39dx_f39_dilution_trap_detector_flagcount_252d_base_v089_signal(ncfcommon, closeadj):
    raise_ = (-ncfcommon).rolling(21, min_periods=10).mean()
    raisez = _z(raise_, 252)
    flag = ((raisez > 0.5) & (_f39_mom(closeadj, 21) > 0)).astype(float)
    cnt = flag.rolling(252, min_periods=126).mean()
    b = cnt + 0.1 * raisez.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share growth per unit of momentum, long horizon
def f39dx_f39_dilution_trap_detector_dilperpump_252d_base_v090_signal(sharesbas, closeadj):
    dil = _f39_share_growth(sharesbas, 252)
    mom = _f39_mom(closeadj, 252).abs()
    b = dil / (mom + 0.10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume z times issuance, long horizon (liquidity-funded raise)
def f39dx_f39_dilution_trap_detector_dvliqiss_252d_base_v091_signal(ncfcommon, closeadj, volume):
    dvz = _z(_f39_dollar_vol(closeadj, volume), 252)
    iss = _z(_f39_issuance(ncfcommon), 504)
    b = dvz * iss
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap distance with range-position on a 252d horizon (distinct from v017)
def f39dx_f39_dilution_trap_detector_trapdistrp_252d_base_v092_signal(sharesbas, closeadj):
    dz = _z(_f39_share_growth(sharesbas, 126), 252)
    rp = _f39_rngpos(closeadj, 252) - 0.5
    b = dz * rp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative dilution weighted by being in the upper 252d range third
def f39dx_f39_dilution_trap_detector_cumdilupper_252d_base_v093_signal(sharesbas, closeadj):
    cumdil = _f39_share_growth(sharesbas, 252)
    upper = (_f39_rngpos(closeadj, 252) >= 0.6667).astype(float)
    b = cumdil * upper
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance frequency on a half-year window, strength-weighted
def f39dx_f39_dilution_trap_detector_issfreq_126d_base_v094_signal(ncfcommon, closeadj):
    raise_m = (-ncfcommon).rolling(21, min_periods=10).mean()
    pos = (raise_m > 0).astype(float)
    freq = pos.rolling(126, min_periods=63).mean()
    strong = _f39_prox_high(closeadj, 126)
    b = freq * strong + 0.05 * _z(raise_m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution z times short-window volume surge (intraday-pump dilution)
def f39dx_f39_dilution_trap_detector_dilvolwt_63d_base_v095_signal(sharesbas, volume):
    dz = _z(_f39_share_growth(sharesbas, 63), 252)
    vs = _f39_volsurge(volume, 5, 21)
    b = dz * vs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# clean-strength on a long horizon (strong price, low dilution = NOT a trap)
def f39dx_f39_dilution_trap_detector_cleanstr_252d_base_v096_signal(sharesbas, closeadj):
    mom = _z(_f39_mom(closeadj, 252), 252)
    nodil = (-_z(_f39_share_growth(sharesbas, 252), 252)).clip(lower=0)
    b = mom * nodil
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# excess dilution (vs own baseline) times momentum on a 126d horizon
def f39dx_f39_dilution_trap_detector_exdil_126d_base_v097_signal(sharesbas, closeadj):
    g = _f39_share_growth(sharesbas, 21)
    base = g.rolling(126, min_periods=63).mean()
    excess = g - base
    strong = _f39_mom(closeadj, 63).clip(lower=0)
    b = excess * strong
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap tanh on a long horizon
def f39dx_f39_dilution_trap_detector_traptanh_252d_base_v098_signal(sharesbas, closeadj):
    dz = _z(_f39_share_growth(sharesbas, 252), 252)
    pz = _z(_f39_mom(closeadj, 252), 252)
    b = np.tanh(0.7 * dz * pz)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise-funded run efficiency on a 504d horizon
def f39dx_f39_dilution_trap_detector_raisefund_504d_base_v099_signal(ncfcommon, closeadj):
    cumraise = (-ncfcommon).rolling(504, min_periods=252).sum()
    cumret = closeadj / closeadj.shift(504).replace(0, np.nan) - 1.0
    b = np.sign(cumret) * _z(cumraise, 504) * cumret.abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution coincident with new 504d highs (count over the year)
def f39dx_f39_dilution_trap_detector_newhidil_504d_base_v100_signal(sharesbas, closeadj):
    hi = closeadj.rolling(504, min_periods=252).max()
    new_hi = (closeadj >= hi * 0.999).astype(float)
    diluting = (_f39_share_growth(sharesbas, 21) > 0).astype(float)
    coincide = (new_hi * diluting).rolling(252, min_periods=126).sum()
    g = _f39_share_growth(sharesbas, 21).clip(lower=0)
    b = coincide + 50.0 * (new_hi * g).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance-into-strength persistence on a long EMA
def f39dx_f39_dilution_trap_detector_isspersist_252d_base_v101_signal(ncfcommon, closeadj):
    iss = _z(_f39_issuance(ncfcommon), 504)
    strong = _f39_prox_high(closeadj, 252)
    gated = iss * strong
    b = gated.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# safe-distance Euclidean trap on a 126d horizon
def f39dx_f39_dilution_trap_detector_safedist_126d_base_v102_signal(sharesbas, closeadj):
    dz = _z(_f39_share_growth(sharesbas, 126), 252).clip(lower=0)
    pz = _z(_f39_mom(closeadj, 126), 252).clip(lower=0)
    b = np.sqrt(dz ** 2 + 0.5 * pz ** 2)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# co-movement regime on a long window (sign agreement of dilution & price)
def f39dx_f39_dilution_trap_detector_comove_252d_base_v103_signal(sharesbas, closeadj):
    sg = _f39_share_growth(sharesbas, 126)
    pg = _f39_mom(closeadj, 126)
    co = np.sign(sg) * np.sign(pg)
    b = co.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap onset over a half-year (rising dilution & rising price)
def f39dx_f39_dilution_trap_detector_onset_126d_base_v104_signal(sharesbas, closeadj):
    dil_now = _f39_share_growth(sharesbas, 126)
    dil_prev = dil_now.shift(126)
    mom_now = _f39_mom(closeadj, 126)
    mom_prev = mom_now.shift(126)
    rising = ((dil_now > dil_prev).astype(float) * (mom_now > mom_prev).astype(float))
    b = rising * (dil_now.clip(lower=0) + mom_now.clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution intensity per dollar of activity, z-scored (distinct from rank v031)
def f39dx_f39_dilution_trap_detector_dilintz_126d_base_v105_signal(sharesbas, closeadj, volume):
    dil = _f39_share_growth(sharesbas, 126)
    dv = _z(_f39_dollar_vol(closeadj, volume), 126)
    intensity = dil * dv
    b = _z(intensity, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance-into-strength angle on a long horizon
def f39dx_f39_dilution_trap_detector_issangle_252d_base_v106_signal(ncfcommon, closeadj):
    iss = _z(_f39_issuance(ncfcommon), 504)
    mom = _z(_f39_mom(closeadj, 252), 504)
    b = np.arctan2(iss, mom.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution filtered by being above the 126d MA (strength-conditional dilution)
def f39dx_f39_dilution_trap_detector_dilabovema_252d_base_v107_signal(sharesbas, closeadj):
    g = _f39_share_growth(sharesbas, 21)
    above = (closeadj > _mean(closeadj, 126)).astype(float)
    filtered = (g * above).rolling(252, min_periods=126).sum()
    b = filtered
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise-to-momentum elasticity on a long horizon (distinct windows from v034)
def f39dx_f39_dilution_trap_detector_elastic_252d_base_v108_signal(sharesbas, closeadj):
    ds = _f39_share_growth(sharesbas, 63)
    dp = _f39_mom(closeadj, 63)
    cov = (ds * dp).rolling(252, min_periods=126).mean()
    var = (dp * dp).rolling(252, min_periods=126).mean()
    b = cov / var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share-accel times momentum z (acceleration-into-strength)
def f39dx_f39_dilution_trap_detector_accelstr_126d_base_v109_signal(sharesbas, closeadj):
    sa = _z(_f39_share_accel(sharesbas, 63), 252)
    mz = _z(_f39_mom(closeadj, 126), 252)
    b = sa * mz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of half-year dollar-volume consumed by issuance
def f39dx_f39_dilution_trap_detector_dvconsume_126d_base_v110_signal(ncfcommon, closeadj, volume):
    raise_ = (-ncfcommon).rolling(126, min_periods=63).sum().clip(lower=0)
    dv = _f39_dollar_vol(closeadj, volume).rolling(126, min_periods=63).sum()
    b = raise_ / dv.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite trap score with volume weight (four-driver blend)
def f39dx_f39_dilution_trap_detector_composite4_252d_base_v111_signal(sharesbas, ncfcommon, closeadj, volume):
    dz = _z(_f39_share_growth(sharesbas, 252), 252)
    iz = _z(_f39_issuance(ncfcommon), 252)
    pz = _z(_f39_mom(closeadj, 252), 252)
    vz = _z(_f39_volsurge(volume, 63, 252), 252)
    b = 0.35 * dz + 0.25 * iz + 0.25 * pz + 0.15 * vz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap change on a 126d horizon (momentum of the trap)
def f39dx_f39_dilution_trap_detector_trapchg_126d_base_v112_signal(sharesbas, closeadj):
    trap = _z(_f39_share_growth(sharesbas, 126), 252) * _z(_f39_mom(closeadj, 63), 126)
    b = trap - trap.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap confirmation on a longer reversal window
def f39dx_f39_dilution_trap_detector_confirm_252d_base_v113_signal(ncfcommon, closeadj):
    iss = _z(_f39_issuance(ncfcommon), 252)
    reversal = -_f39_mom(closeadj, 63)
    b = iss.shift(63) * reversal
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lumpy share-growth dispersion on a long horizon times strength
def f39dx_f39_dilution_trap_detector_lumpy_252d_base_v114_signal(sharesbas, closeadj):
    g = _f39_share_growth(sharesbas, 21)
    disp = g.rolling(252, min_periods=126).std()
    strong = _f39_prox_high(closeadj, 252)
    b = disp * strong
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance rank times range-position rank (both-high corner via ranks)
def f39dx_f39_dilution_trap_detector_issrngrank_126d_base_v115_signal(ncfcommon, closeadj):
    ir = _rank(_f39_issuance(ncfcommon), 252)
    rr = _rank(_f39_rngpos(closeadj, 126), 252)
    b = ir * rr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution accel during a 63d-MA blowoff stretch (longer stretch than v042)
def f39dx_f39_dilution_trap_detector_blowoffdil_126d_base_v116_signal(sharesbas, closeadj):
    sa = _f39_share_accel(sharesbas, 126)
    stretch = closeadj / _mean(closeadj, 63).replace(0, np.nan) - 1.0
    b = sa * stretch.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap per unit downside-risk (trap/semi-deviation)
def f39dx_f39_dilution_trap_detector_trapdrisk_252d_base_v117_signal(sharesbas, closeadj):
    trap = _f39_share_growth(sharesbas, 252) * _f39_mom(closeadj, 252).clip(lower=0)
    ret = closeadj.pct_change()
    semidev = ret.clip(upper=0).rolling(126, min_periods=63).std()
    b = trap / semidev.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of aggressive-dilution-into-strength events (126d window, weighted)
def f39dx_f39_dilution_trap_detector_aggrevent_126d_base_v118_signal(sharesbas, closeadj):
    mg = _f39_share_growth(sharesbas, 21)
    mom = _f39_mom(closeadj, 21)
    aggressive = ((mg > 0.015) & (mom > 0)).astype(float)
    weighted = aggressive * (mg + mom)
    b = weighted.rolling(126, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution share of dollar-volume, long-EMA smoothed (distinct span from v045)
def f39dx_f39_dilution_trap_detector_dilshare_252d_base_v119_signal(sharesbas, closeadj, volume):
    dil = _f39_share_growth(sharesbas, 126)
    dvz = _z(_f39_dollar_vol(closeadj, volume), 504)
    raw = dil * dvz
    b = raw.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution drag on a 126d horizon (signed)
def f39dx_f39_dilution_trap_detector_dildrag_126d_base_v120_signal(sharesbas, closeadj):
    raw_mom = _f39_mom(closeadj, 126)
    dil = _f39_share_growth(sharesbas, 126)
    b = dil * np.sign(raw_mom) * raw_mom.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rank product on a 126d horizon (distinct window from v047)
def f39dx_f39_dilution_trap_detector_rankprod_126d_base_v121_signal(ncfcommon, closeadj):
    ir = _rank(_f39_issuance(ncfcommon), 252) + 0.5
    pr = _rank(_f39_mom(closeadj, 126), 252) + 0.5
    b = ir * pr - 0.25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of half-year diluting on high-volume days
def f39dx_f39_dilution_trap_detector_volregdil_126d_base_v122_signal(sharesbas, volume):
    diluting = (_f39_share_growth(sharesbas, 21) > 0).astype(float)
    high_vol = (_f39_volz(volume, 63) > 0.5).astype(float)
    coincide = (diluting * high_vol).rolling(126, min_periods=63).mean()
    surge = _f39_volsurge(volume, 21, 126)
    b = coincide + 0.1 * (surge - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-per-new-share efficiency on a long horizon
def f39dx_f39_dilution_trap_detector_cashpershare_252d_base_v123_signal(ncfcommon, sharesbas):
    raise_ = (-ncfcommon).rolling(126, min_periods=63).mean()
    new_shares = sharesbas.diff(126).abs()
    eff = raise_ / new_shares.replace(0, np.nan)
    b = _z(eff, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap pressure using 126d-MA stretch (longer stretch than v051)
def f39dx_f39_dilution_trap_detector_pressure_126d_base_v124_signal(sharesbas, closeadj):
    dz = _z(_f39_share_growth(sharesbas, 252), 252)
    stretch = closeadj / _mean(closeadj, 126).replace(0, np.nan) - 1.0
    b = dz * stretch
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# triple-gate fraction on a 126d window (distinct from v052)
def f39dx_f39_dilution_trap_detector_triplegate_126d_base_v125_signal(ncfcommon, closeadj, volume):
    raise_pos = (-ncfcommon).rolling(21, min_periods=10).mean() > 0
    strong = _f39_mom(closeadj, 21) > 0
    surge = _f39_volz(volume, 63) > 0
    gate = (raise_pos & strong & surge).astype(float)
    b = gate.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap regime relative to its 252d average (distinct window from v053)
def f39dx_f39_dilution_trap_detector_trapregime_252d_base_v126_signal(sharesbas, closeadj):
    trap = _f39_share_growth(sharesbas, 63) * _f39_mom(closeadj, 63)
    b = trap - trap.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# raise-on-rally beta on a 126d window
def f39dx_f39_dilution_trap_detector_raisecorr_126d_base_v127_signal(sharesbas, closeadj):
    sg = _f39_share_growth(sharesbas, 21)
    ret = closeadj.pct_change(21)
    sgz = _z(sg, 126)
    retz = _z(ret, 126)
    b = (sgz * retz).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance scaled by log-price, smoothed (affordability, distinct from v055)
def f39dx_f39_dilution_trap_detector_issaffrd_252d_base_v128_signal(ncfcommon, closeadj):
    raise_ = (-ncfcommon).rolling(126, min_periods=63).mean()
    raw = _z(raise_, 504) * np.log(closeadj.replace(0, np.nan))
    b = raw.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# desperation/trap sign on a 126d horizon (dilute high vs low)
def f39dx_f39_dilution_trap_detector_desperation_126d_base_v129_signal(sharesbas, closeadj):
    dil = _z(_f39_share_growth(sharesbas, 63), 252)
    rp = _f39_rngpos(closeadj, 126)
    b = dil * (2.0 * rp - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quiet dilution on a long horizon (dilution z minus volume z, 252d)
def f39dx_f39_dilution_trap_detector_quietdil_252d_base_v130_signal(sharesbas, volume):
    dz = _z(_f39_share_growth(sharesbas, 252), 252)
    vz = _z(_f39_volsurge(volume, 63, 252), 252)
    b = dz - vz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap acceleration on a 126d horizon (change in trapcore)
def f39dx_f39_dilution_trap_detector_trapaccel_126d_base_v131_signal(sharesbas, closeadj):
    trap = _f39_share_growth(sharesbas, 126) * _f39_prox_high(closeadj, 126)
    b = trap - trap.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance normalized by its own vol, long-strength gated
def f39dx_f39_dilution_trap_detector_issnorm_252d_base_v132_signal(ncfcommon, closeadj):
    raise_ = (-ncfcommon)
    raisez = (raise_ - raise_.rolling(504, min_periods=252).mean()) / \
        raise_.rolling(504, min_periods=252).std().replace(0, np.nan)
    strong = _f39_mom(closeadj, 126).clip(lower=0)
    b = raisez * strong
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# aggressive-dilution count on a 504d window (multi-year tally, weighted)
def f39dx_f39_dilution_trap_detector_aggrcount_504d_base_v133_signal(sharesbas, closeadj):
    mg = _f39_share_growth(sharesbas, 21)
    up = _f39_mom(closeadj, 21) > 0
    aggressive = ((mg > 0.015) & up).astype(float)
    cnt = aggressive.rolling(504, min_periods=252).sum()
    b = cnt + 100.0 * (aggressive * mg).rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# per-share gap rank on a 126d horizon
def f39dx_f39_dilution_trap_detector_psgaprank_126d_base_v134_signal(sharesbas, closeadj):
    raw = _f39_mom(closeadj, 126)
    gap = _f39_share_growth(sharesbas, 126)  # raw - (raw - dil) = dil
    b = _rank(gap * np.sign(raw), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pump-then-fade on a longer fade window
def f39dx_f39_dilution_trap_detector_pumpfade_126d_base_v135_signal(ncfcommon, closeadj):
    pulse = _z((-ncfcommon).rolling(63, min_periods=21).mean(), 252)
    run = _f39_mom(closeadj, 126).clip(lower=0)
    fade = (-_f39_mom(closeadj, 21)).clip(lower=0)
    b = pulse * run * fade
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap distance scaled by volume concentration on a 252d window
def f39dx_f39_dilution_trap_detector_volconcdist_252d_base_v136_signal(sharesbas, closeadj, volume):
    dz = _z(_f39_share_growth(sharesbas, 252), 252)
    pz = _z(_f39_mom(closeadj, 252), 252)
    vol_share = volume / volume.rolling(252, min_periods=126).sum().replace(0, np.nan)
    b = dz * pz * (vol_share * 252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dual-extreme on a 126d window (both ranks above 0.7)
def f39dx_f39_dilution_trap_detector_dualextreme_126d_base_v137_signal(sharesbas, closeadj):
    dr = _rank(_f39_share_growth(sharesbas, 126), 252) + 0.5
    pr = _rank(_f39_mom(closeadj, 126), 252) + 0.5
    both = ((dr > 0.7) & (pr > 0.7)).astype(float)
    b = both.rolling(63, min_periods=21).mean() + 0.1 * dr * pr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# escalating issuance on a 126d horizon
def f39dx_f39_dilution_trap_detector_escalate_126d_base_v138_signal(ncfcommon, closeadj):
    raise_ = (-ncfcommon).rolling(63, min_periods=21).mean()
    escalation = raise_ - raise_.shift(126)
    strong = _f39_prox_high(closeadj, 126)
    b = _z(escalation, 252) * strong
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution times dollar-volume momentum on a 252d horizon
def f39dx_f39_dilution_trap_detector_dvmomdil_252d_base_v139_signal(sharesbas, closeadj, volume):
    dil = _z(_f39_share_growth(sharesbas, 252), 252)
    dv = _f39_dollar_vol(closeadj, volume)
    dvmom = np.log(dv.rolling(63, min_periods=21).mean().replace(0, np.nan) /
                   dv.rolling(252, min_periods=126).mean().replace(0, np.nan))
    b = dil * dvmom
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap recency on a 504d window (time since last trap peak)
def f39dx_f39_dilution_trap_detector_traprecency_504d_base_v140_signal(sharesbas, closeadj):
    trap = (_f39_share_growth(sharesbas, 126) * _f39_mom(closeadj, 126)).clip(lower=0)

    def _dsh(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = trap.rolling(504, min_periods=252).apply(_dsh, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# funding efficiency on a 504d horizon (distinct from v068)
def f39dx_f39_dilution_trap_detector_fundeff_504d_base_v141_signal(ncfcommon, closeadj):
    cumraise = (-ncfcommon).rolling(504, min_periods=252).sum().clip(lower=0)
    cumret = closeadj / closeadj.shift(504).replace(0, np.nan) - 1.0
    b = cumret / (_z(cumraise, 504).abs() + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution times vol-expansion on a 252d horizon
def f39dx_f39_dilution_trap_detector_volexpdil_252d_base_v142_signal(sharesbas, closeadj):
    dz = _z(_f39_share_growth(sharesbas, 252), 252)
    volshort = closeadj.pct_change().rolling(63, min_periods=21).std()
    vollong = closeadj.pct_change().rolling(252, min_periods=126).std()
    expand = volshort / vollong.replace(0, np.nan)
    b = dz * (expand - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# issuance timing skew on a 126d horizon (raise-on-strength minus raise-on-weakness)
def f39dx_f39_dilution_trap_detector_timeskew_126d_base_v143_signal(ncfcommon, closeadj):
    raise_ = _z((-ncfcommon).rolling(21, min_periods=10).mean(), 252)
    up = (_f39_mom(closeadj, 21) > 0).astype(float)
    on_str = (raise_ * up).rolling(126, min_periods=63).mean()
    on_weak = (raise_ * (1 - up)).rolling(126, min_periods=63).mean()
    b = on_str - on_weak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap intensity log1p on a 252d horizon (distinct windows from v071)
def f39dx_f39_dilution_trap_detector_intensity_252d_base_v144_signal(sharesbas, closeadj, volume):
    dz = _z(_f39_share_growth(sharesbas, 252), 252)
    pz = _z(_f39_mom(closeadj, 252), 504)
    vz = _z(_f39_volsurge(volume, 63, 252), 252)
    raw = dz * pz * vz
    b = np.sign(raw) * np.log1p(raw.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# additive trap distance on the multi-year horizon, signed
def f39dx_f39_dilution_trap_detector_trapdistadd_1260d_base_v145_signal(sharesbas, closeadj):
    dz = _z(_f39_share_growth(sharesbas, 504), 504)
    pz = _z(_f39_prox_high(closeadj, 504), 504)
    b = (dz + pz) * np.sign(dz)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# self-rank of issuance-into-strength on a 252d window
def f39dx_f39_dilution_trap_detector_selfrank_252d_base_v146_signal(ncfcommon, closeadj):
    iss = _z(_f39_issuance(ncfcommon), 504)
    strong = _f39_prox_high(closeadj, 252)
    gated = iss * strong
    b = _rank(gated, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trap-vs-clean balance on a 126d window
def f39dx_f39_dilution_trap_detector_trapbalance_126d_base_v147_signal(sharesbas, closeadj):
    up = _f39_mom(closeadj, 21) > 0
    diluting = _f39_share_growth(sharesbas, 21) > 0
    trap_d = (up & diluting).astype(float).rolling(126, min_periods=63).sum()
    clean_d = (up & ~diluting).astype(float).rolling(126, min_periods=63).sum()
    b = (trap_d - clean_d) / (trap_d + clean_d).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dilution-weighted overextension exhaustion on a 126d horizon
def f39dx_f39_dilution_trap_detector_exhaust_126d_base_v148_signal(sharesbas, closeadj):
    cumdil = _f39_share_growth(sharesbas, 126)
    overext = (closeadj / _mean(closeadj, 126).replace(0, np.nan) - 1.0)
    b = cumdil * overext.clip(lower=0) * np.sign(cumdil)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-issuance momentum interacted with price drawdown-from-high (raise after top)
def f39dx_f39_dilution_trap_detector_issafterTop_252d_base_v149_signal(ncfcommon, closeadj):
    iss = _z((-ncfcommon).rolling(63, min_periods=21).mean(), 252)
    dd = _f39_prox_high(closeadj, 252) - 1.0  # negative drawdown from 252d high
    b = iss * dd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# grand trap composite: dilution-z x momentum-z x issuance-z, additive volume tilt
def f39dx_f39_dilution_trap_detector_grand_252d_base_v150_signal(sharesbas, ncfcommon, closeadj, volume):
    dz = _z(_f39_share_growth(sharesbas, 252), 252)
    pz = _z(_f39_mom(closeadj, 252), 252)
    iz = _z(_f39_issuance(ncfcommon), 252)
    vz = _z(_f39_volsurge(volume, 63, 252), 252)
    core = dz * pz
    b = core + 0.3 * iz * pz + 0.1 * vz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f39dx_f39_dilution_trap_detector_trapcore_126d_base_v076_signal,
    f39dx_f39_dilution_trap_detector_issuestr_21d_base_v077_signal,
    f39dx_f39_dilution_trap_detector_dilslopemom_126d_base_v078_signal,
    f39dx_f39_dilution_trap_detector_corner_252d_base_v079_signal,
    f39dx_f39_dilution_trap_detector_newspumpdil_63d_base_v080_signal,
    f39dx_f39_dilution_trap_detector_freshhigh_504d_base_v081_signal,
    f39dx_f39_dilution_trap_detector_raisepershr_126d_base_v082_signal,
    f39dx_f39_dilution_trap_detector_triple_252d_base_v083_signal,
    f39dx_f39_dilution_trap_detector_leadlag_252d_base_v084_signal,
    f39dx_f39_dilution_trap_detector_jointaccel_126d_base_v085_signal,
    f39dx_f39_dilution_trap_detector_issdown_126d_base_v086_signal,
    f39dx_f39_dilution_trap_detector_trapstreak_126d_base_v087_signal,
    f39dx_f39_dilution_trap_detector_addtrap_126d_base_v088_signal,
    f39dx_f39_dilution_trap_detector_flagcount_252d_base_v089_signal,
    f39dx_f39_dilution_trap_detector_dilperpump_252d_base_v090_signal,
    f39dx_f39_dilution_trap_detector_dvliqiss_252d_base_v091_signal,
    f39dx_f39_dilution_trap_detector_trapdistrp_252d_base_v092_signal,
    f39dx_f39_dilution_trap_detector_cumdilupper_252d_base_v093_signal,
    f39dx_f39_dilution_trap_detector_issfreq_126d_base_v094_signal,
    f39dx_f39_dilution_trap_detector_dilvolwt_63d_base_v095_signal,
    f39dx_f39_dilution_trap_detector_cleanstr_252d_base_v096_signal,
    f39dx_f39_dilution_trap_detector_exdil_126d_base_v097_signal,
    f39dx_f39_dilution_trap_detector_traptanh_252d_base_v098_signal,
    f39dx_f39_dilution_trap_detector_raisefund_504d_base_v099_signal,
    f39dx_f39_dilution_trap_detector_newhidil_504d_base_v100_signal,
    f39dx_f39_dilution_trap_detector_isspersist_252d_base_v101_signal,
    f39dx_f39_dilution_trap_detector_safedist_126d_base_v102_signal,
    f39dx_f39_dilution_trap_detector_comove_252d_base_v103_signal,
    f39dx_f39_dilution_trap_detector_onset_126d_base_v104_signal,
    f39dx_f39_dilution_trap_detector_dilintz_126d_base_v105_signal,
    f39dx_f39_dilution_trap_detector_issangle_252d_base_v106_signal,
    f39dx_f39_dilution_trap_detector_dilabovema_252d_base_v107_signal,
    f39dx_f39_dilution_trap_detector_elastic_252d_base_v108_signal,
    f39dx_f39_dilution_trap_detector_accelstr_126d_base_v109_signal,
    f39dx_f39_dilution_trap_detector_dvconsume_126d_base_v110_signal,
    f39dx_f39_dilution_trap_detector_composite4_252d_base_v111_signal,
    f39dx_f39_dilution_trap_detector_trapchg_126d_base_v112_signal,
    f39dx_f39_dilution_trap_detector_confirm_252d_base_v113_signal,
    f39dx_f39_dilution_trap_detector_lumpy_252d_base_v114_signal,
    f39dx_f39_dilution_trap_detector_issrngrank_126d_base_v115_signal,
    f39dx_f39_dilution_trap_detector_blowoffdil_126d_base_v116_signal,
    f39dx_f39_dilution_trap_detector_trapdrisk_252d_base_v117_signal,
    f39dx_f39_dilution_trap_detector_aggrevent_126d_base_v118_signal,
    f39dx_f39_dilution_trap_detector_dilshare_252d_base_v119_signal,
    f39dx_f39_dilution_trap_detector_dildrag_126d_base_v120_signal,
    f39dx_f39_dilution_trap_detector_rankprod_126d_base_v121_signal,
    f39dx_f39_dilution_trap_detector_volregdil_126d_base_v122_signal,
    f39dx_f39_dilution_trap_detector_cashpershare_252d_base_v123_signal,
    f39dx_f39_dilution_trap_detector_pressure_126d_base_v124_signal,
    f39dx_f39_dilution_trap_detector_triplegate_126d_base_v125_signal,
    f39dx_f39_dilution_trap_detector_trapregime_252d_base_v126_signal,
    f39dx_f39_dilution_trap_detector_raisecorr_126d_base_v127_signal,
    f39dx_f39_dilution_trap_detector_issaffrd_252d_base_v128_signal,
    f39dx_f39_dilution_trap_detector_desperation_126d_base_v129_signal,
    f39dx_f39_dilution_trap_detector_quietdil_252d_base_v130_signal,
    f39dx_f39_dilution_trap_detector_trapaccel_126d_base_v131_signal,
    f39dx_f39_dilution_trap_detector_issnorm_252d_base_v132_signal,
    f39dx_f39_dilution_trap_detector_aggrcount_504d_base_v133_signal,
    f39dx_f39_dilution_trap_detector_psgaprank_126d_base_v134_signal,
    f39dx_f39_dilution_trap_detector_pumpfade_126d_base_v135_signal,
    f39dx_f39_dilution_trap_detector_volconcdist_252d_base_v136_signal,
    f39dx_f39_dilution_trap_detector_dualextreme_126d_base_v137_signal,
    f39dx_f39_dilution_trap_detector_escalate_126d_base_v138_signal,
    f39dx_f39_dilution_trap_detector_dvmomdil_252d_base_v139_signal,
    f39dx_f39_dilution_trap_detector_traprecency_504d_base_v140_signal,
    f39dx_f39_dilution_trap_detector_fundeff_504d_base_v141_signal,
    f39dx_f39_dilution_trap_detector_volexpdil_252d_base_v142_signal,
    f39dx_f39_dilution_trap_detector_timeskew_126d_base_v143_signal,
    f39dx_f39_dilution_trap_detector_intensity_252d_base_v144_signal,
    f39dx_f39_dilution_trap_detector_trapdistadd_1260d_base_v145_signal,
    f39dx_f39_dilution_trap_detector_selfrank_252d_base_v146_signal,
    f39dx_f39_dilution_trap_detector_trapbalance_126d_base_v147_signal,
    f39dx_f39_dilution_trap_detector_exhaust_126d_base_v148_signal,
    f39dx_f39_dilution_trap_detector_issafterTop_252d_base_v149_signal,
    f39dx_f39_dilution_trap_detector_grand_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F39_DILUTION_TRAP_DETECTOR_REGISTRY_076_150 = REGISTRY


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

    sharesbas = _fund(101, base=5e7, drift=0.06, vol=0.10).rename("sharesbas")
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

    print("OK f39_dilution_trap_detector_base_076_150_claude: %d features pass" % n_features)
