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


def _rsum(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _slope(s, w):
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = float((idx ** 2).sum())

    def _f(a):
        if np.any(np.isnan(a)):
            return np.nan
        return float(np.dot(idx, a) / denom)
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== folder domain primitives (volume pressure) =====
def _f12_dollar_vol(closeadj, volume):
    return closeadj * volume


def _f12_rel_vol(volume, w):
    return volume / _mean(volume, w).replace(0, np.nan)


def _f12_surge(volume, wshort, wlong):
    return _mean(volume, wshort) / _mean(volume, wlong).replace(0, np.nan)


def _f12_updown_ratio(closeadj, volume, w):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0)
    dn = volume.where(ret < 0, 0.0)
    return _rsum(up, w) / _rsum(dn, w).replace(0, np.nan)


def _f12_concentration(volume, w):
    sm = _rsum(volume, w)
    sq = _rsum(volume ** 2, w)
    return sq / (sm ** 2).replace(0, np.nan)


def _f12_net_press(closeadj, volume, w):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0)
    dn = volume.where(ret < 0, 0.0)
    return (_rsum(up, w) - _rsum(dn, w)) / _rsum(volume, w).replace(0, np.nan)


# ============================================================
# --- dollar-volume trend & growth (windows > 21d) ---
def f12vp_f12_volume_pressure_dvolgrow_126d_base_v076_signal(closeadj, volume):
    dv = _f12_dollar_vol(closeadj, volume)
    a = _mean(dv, 21)
    b = np.log(a.replace(0, np.nan) / a.shift(126).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f12vp_f12_volume_pressure_dvolgrow_63d_base_v077_signal(closeadj, volume):
    dv = _f12_dollar_vol(closeadj, volume)
    a = _mean(dv, 21)
    b = np.log(a.replace(0, np.nan) / a.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume trend slope over a half-year (log-DV regression slope)
def f12vp_f12_volume_pressure_dvolslope_126d_base_v078_signal(closeadj, volume):
    dv = np.log(_f12_dollar_vol(closeadj, volume).replace(0, np.nan))
    b = _slope(dv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume monotonicity (net move / abs path) over a quarter
def f12vp_f12_volume_pressure_dvoltrendq_63d_base_v079_signal(closeadj, volume):
    dv = np.log(_f12_dollar_vol(closeadj, volume).replace(0, np.nan))
    net = dv - dv.shift(62)
    path = dv.diff().abs().rolling(63, min_periods=21).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume z vs 252d history (long-horizon liquidity abnormality)
def f12vp_f12_volume_pressure_dvolz_252d_base_v080_signal(closeadj, volume):
    dv = np.log(_f12_dollar_vol(closeadj, volume).replace(0, np.nan))
    b = _z(dv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume surge variants (distinct short/long pairs) ---
def f12vp_f12_volume_pressure_surge_3v21_base_v081_signal(volume):
    b = _f12_surge(volume, 3, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f12vp_f12_volume_pressure_surge_10v63_base_v082_signal(volume):
    b = _f12_surge(volume, 10, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f12vp_f12_volume_pressure_surge_42v252_base_v083_signal(volume):
    b = _f12_surge(volume, 42, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge ratio z-scored vs its own history (de-trended surge extremity)
def f12vp_f12_volume_pressure_surgez_5v63_base_v084_signal(volume):
    s = _f12_surge(volume, 5, 63)
    b = _z(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge percentile rank vs own 252d history
def f12vp_f12_volume_pressure_surgerank_21v126_base_v085_signal(volume):
    s = _f12_surge(volume, 21, 126)
    b = s.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- up/down volume pressure variants ---
def f12vp_f12_volume_pressure_netpress_21d_base_v086_signal(closeadj, volume):
    b = _f12_net_press(closeadj, volume, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


def f12vp_f12_volume_pressure_netpress_126d_base_v087_signal(closeadj, volume):
    b = _f12_net_press(closeadj, volume, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net pressure change over a quarter (pressure rotation)
def f12vp_f12_volume_pressure_netpressmom_63d_base_v088_signal(closeadj, volume):
    np_ = _f12_net_press(closeadj, volume, 63)
    b = np_ - np_.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-volume to total-volume EWMA (smoothed accumulation tilt)
def f12vp_f12_volume_pressure_upvolewma_base_v089_signal(closeadj, volume):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0)
    b = up.ewm(span=21, min_periods=10).mean() / volume.ewm(span=21, min_periods=10).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up/down DOLLAR-volume ratio over a quarter (money-weighted participation)
def f12vp_f12_volume_pressure_uddvol_63d_base_v090_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f12_dollar_vol(closeadj, volume)
    up = dv.where(ret > 0, 0.0)
    dn = dv.where(ret < 0, 0.0)
    b = np.log(_rsum(up, 63) / _rsum(dn, 63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- relative volume regime / position ---
def f12vp_f12_volume_pressure_volregime_126d_base_v091_signal(volume):
    av = _mean(volume, 21)
    hi = _rmax(volume, 126)
    lo = _rmin(volume, 126)
    b = (av - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current volume position within its own 63d high-low band
def f12vp_f12_volume_pressure_volband_63d_base_v092_signal(volume):
    hi = _rmax(volume, 63)
    lo = _rmin(volume, 63)
    b = (volume - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of current volume from its 252d max (how far below peak activity)
def f12vp_f12_volume_pressure_volpeakgap_252d_base_v093_signal(volume):
    av = _mean(volume, 5)
    hi = _rmax(volume, 252)
    b = np.log(av.replace(0, np.nan) / hi.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume trend slope variants ---
def f12vp_f12_volume_pressure_volslope_126d_base_v094_signal(volume):
    b = _slope(volume, 126) / _mean(volume, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of the 5d-average volume over a month (smoothed trend)
def f12vp_f12_volume_pressure_volslopesm_21d_base_v095_signal(volume):
    av = _mean(volume, 5)
    b = _slope(av, 21) / _mean(volume, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# difference between short and long volume slopes (trend curvature as level)
def f12vp_f12_volume_pressure_volslopespr_base_v096_signal(volume):
    s1 = _slope(volume, 21) / _mean(volume, 21).replace(0, np.nan)
    s2 = _slope(volume, 63) / _mean(volume, 63).replace(0, np.nan)
    b = s1 - s2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume concentration / distribution shape ---
def f12vp_f12_volume_pressure_conc_126d_base_v097_signal(volume):
    b = _f12_concentration(volume, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-3-day volume share over a quarter (extreme clustering)
def f12vp_f12_volume_pressure_top3share_63d_base_v098_signal(volume):
    def _top3(a):
        if np.any(np.isnan(a)):
            return np.nan
        s = np.sort(a)[-3:].sum()
        tot = a.sum()
        return s / tot if tot > 0 else np.nan
    b = volume.rolling(63, min_periods=42).apply(_top3, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Gini-like dispersion of volume over a quarter
def f12vp_f12_volume_pressure_volgini_63d_base_v099_signal(volume):
    def _gini(a):
        if np.any(np.isnan(a)) or a.sum() <= 0:
            return np.nan
        x = np.sort(a)
        nn = len(x)
        cum = np.cumsum(x)
        return (nn + 1 - 2 * (cum.sum() / cum[-1])) / nn
    b = volume.rolling(63, min_periods=42).apply(_gini, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of max single-day volume to median volume (spike-to-typical)
def f12vp_f12_volume_pressure_spike2med_63d_base_v100_signal(volume):
    hi = _rmax(volume, 63)
    med = volume.rolling(63, min_periods=21).median()
    b = hi / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- abnormal-volume frequency & magnitude ---
def f12vp_f12_volume_pressure_surgefreq_252d_base_v101_signal(volume):
    # how heavy is the quarter's average activity vs the 90th-pct day of the year
    q90 = volume.rolling(252, min_periods=126).quantile(0.9)
    b = _mean(volume, 63) / q90.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since the last big volume spike (staleness of last surge), normalized
def f12vp_f12_volume_pressure_dayssincesurge_base_v102_signal(volume):
    # recency of peak activity: how far back (within 63d) the max-volume day sits,
    # blended with the depth below that peak (continuous)
    def _argmax_pos(a):
        if np.any(np.isnan(a)):
            return np.nan
        return float(len(a) - 1 - int(np.argmax(a))) / float(len(a))
    pos = volume.rolling(63, min_periods=21).apply(_argmax_pos, raw=True)
    gap = np.log(_mean(volume, 5).replace(0, np.nan) / _rmax(volume, 63).replace(0, np.nan))
    b = pos + gap
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average surge magnitude on the top-decile volume days (intensity of big days)
def f12vp_f12_volume_pressure_bigdaymag_126d_base_v103_signal(volume):
    # average excess of the top-quartile volume days over the window mean (big-day lift)
    q75 = volume.rolling(126, min_periods=63).quantile(0.75)
    mn = _mean(volume, 126)
    excess = (volume - q75).clip(lower=0)
    b = excess.rolling(126, min_periods=63).mean() / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume-volatility interaction ---
def f12vp_f12_volume_pressure_volvolcorr_63d_base_v104_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    lv = np.log(volume.replace(0, np.nan))
    b = ret.rolling(63, min_periods=21).corr(lv)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume per unit of absolute return (effort to move price), inverse-illiquidity-like
def f12vp_f12_volume_pressure_voleffort_21d_base_v105_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    eff = volume / (ret.replace(0, np.nan))
    b = np.log(eff.rolling(21, min_periods=10).median())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- dollar-volume relative vs raw-volume relative (price-mix divergence) ---
def f12vp_f12_volume_pressure_dvmix_126d_base_v106_signal(closeadj, volume):
    dv = _f12_dollar_vol(closeadj, volume)
    rdv = np.log(dv / _mean(dv, 126).replace(0, np.nan))
    rv = np.log(volume / _mean(volume, 126).replace(0, np.nan))
    b = rdv - rv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume momentum & acceleration ---
def f12vp_f12_volume_pressure_volmom_63d_base_v107_signal(volume):
    a = _mean(volume, 21)
    b = a / a.shift(42).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume acceleration: difference of two consecutive monthly growth rates
def f12vp_f12_volume_pressure_volaccel2_base_v108_signal(volume):
    a = _mean(volume, 21)
    g1 = a / a.shift(21).replace(0, np.nan) - 1.0
    b = g1 - g1.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA-volume momentum (fast vs slow EWMA, log)
def f12vp_f12_volume_pressure_volewmom_base_v109_signal(volume):
    fast = volume.ewm(span=5, min_periods=3).mean()
    slow = volume.ewm(span=42, min_periods=21).mean()
    b = np.log(fast.replace(0, np.nan) / slow.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- relative-volume dispersion / breadth ---
def f12vp_f12_volume_pressure_relvoldisp_252_base_v110_signal(volume):
    r1 = _f12_rel_vol(volume, 21)
    r2 = _f12_rel_vol(volume, 63)
    r3 = _f12_rel_vol(volume, 252)
    b = pd.concat([r1, r2, r3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread between two surge ratios at different long anchors (term structure of surge)
def f12vp_f12_volume_pressure_surgeterm_base_v111_signal(volume):
    s1 = _f12_surge(volume, 5, 21)
    s2 = _f12_surge(volume, 21, 126)
    b = s1 - s2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume entropy / evenness ---
def f12vp_f12_volume_pressure_volentropy_63d_base_v112_signal(volume):
    sm = _rsum(volume, 63)
    p = volume / sm.replace(0, np.nan)
    contrib = -(p * np.log(p.replace(0, np.nan)))
    ent = contrib.rolling(63, min_periods=42).sum()
    b = ent / np.log(63.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- signed dollar-volume pressure (money flow direction) ---
def f12vp_f12_volume_pressure_signdvolpr_21d_base_v113_signal(closeadj, volume):
    # short-term dollar-flow thrust: 5d signed dollar-volume vs 21d signed dollar-volume
    ret = closeadj.pct_change()
    dv = _f12_dollar_vol(closeadj, volume)
    short = _rsum(np.sign(ret) * dv, 5) / _rsum(dv, 5).replace(0, np.nan)
    long = _rsum(np.sign(ret) * dv, 21) / _rsum(dv, 21).replace(0, np.nan)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return-weighted dollar-volume (does money chase the move) over a quarter
def f12vp_f12_volume_pressure_dvolretw_63d_base_v114_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f12_dollar_vol(closeadj, volume)
    b = _rsum(ret * dv, 63) / _rsum(dv, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- abnormal volume on big-move days (event participation, distinct window) ---
def f12vp_f12_volume_pressure_eventvol_126d_base_v115_signal(closeadj, volume):
    ret = closeadj.pct_change()
    thr = ret.abs().rolling(126, min_periods=63).quantile(0.9)
    big = ret.abs() >= thr
    rv = _f12_rel_vol(volume, 126)
    ev = rv.where(big, np.nan)
    b = ev.rolling(126, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume on up-moves vs down-moves: relative-volume asymmetry of magnitude
def f12vp_f12_volume_pressure_magasym_63d_base_v116_signal(closeadj, volume):
    ret = closeadj.pct_change()
    upv = volume.where(ret > 0, np.nan)
    dnv = volume.where(ret < 0, np.nan)
    ur = upv.rolling(63, min_periods=10).median()
    dr = dnv.rolling(63, min_periods=10).median()
    b = np.log(ur / dr.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume trend confirmation with price (directional agreement, distinct) ---
def f12vp_f12_volume_pressure_voltrendconf_126d_base_v117_signal(closeadj, volume):
    vsl = _slope(np.log(volume.replace(0, np.nan)), 126)
    pmom = closeadj / closeadj.shift(126) - 1.0
    b = vsl * np.sign(pmom)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# correlation of daily log-volume changes with daily returns (price-vol coupling)
def f12vp_f12_volume_pressure_pvcorr_63d_base_v118_signal(closeadj, volume):
    dlv = np.log(volume.replace(0, np.nan)).diff()
    ret = closeadj.pct_change()
    b = ret.rolling(63, min_periods=21).corr(dlv)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume z-score extremity counts / tails ---
def f12vp_f12_volume_pressure_voltailfreq_126d_base_v119_signal(volume):
    # right-tail mass of abnormal volume: mean of positive z-scores over the half-year
    zz = _z(volume, 126)
    b = zz.clip(lower=0).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume drought: fraction of quarter below the 10th percentile of 252d volume
def f12vp_f12_volume_pressure_droughtfreq_base_v120_signal(volume):
    q10 = volume.rolling(252, min_periods=126).quantile(0.1)
    dry = (volume < q10).astype(float)
    freq = dry.rolling(63, min_periods=21).mean()
    depth = (1.0 - volume / q10.replace(0, np.nan)).clip(lower=0).rolling(21, min_periods=10).mean()
    b = freq + depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume-weighted price-pressure composites ---
def f12vp_f12_volume_pressure_pressidx_63d_base_v121_signal(closeadj, volume):
    ret = closeadj.pct_change()
    lr = np.log(volume.replace(0, np.nan) / _mean(volume, 126).replace(0, np.nan))
    b = _rsum(np.sign(ret) * lr, 63) / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation/distribution tilt: net-pressure smoothed and ranked
def f12vp_f12_volume_pressure_accrank_126d_base_v122_signal(closeadj, volume):
    npress = _f12_net_press(closeadj, volume, 21)
    sm = npress.ewm(span=10, min_periods=5).mean()
    b = sm.rolling(126, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- relative dollar-volume level vs annual baseline ---
def f12vp_f12_volume_pressure_dvolrel_252d_base_v123_signal(closeadj, volume):
    dv = _f12_dollar_vol(closeadj, volume)
    av = _mean(dv, 21)
    b = np.log(av.replace(0, np.nan) / _mean(dv, 252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume surge percentile rank vs own history
def f12vp_f12_volume_pressure_dvolsurgerank_base_v124_signal(closeadj, volume):
    dv = _f12_dollar_vol(closeadj, volume)
    s = _mean(dv, 5) / _mean(dv, 63).replace(0, np.nan)
    b = s.rolling(252, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume autocorrelation (persistence/clustering of activity) ---
def f12vp_f12_volume_pressure_volacf1_63d_base_v125_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    b = lv.rolling(63, min_periods=42).corr(lv.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume change autocorrelation (do surges reverse or persist)
def f12vp_f12_volume_pressure_volchgacf_63d_base_v126_signal(volume):
    dlv = np.log(volume.replace(0, np.nan)).diff()
    b = dlv.rolling(63, min_periods=42).corr(dlv.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- rising-volume streak weighted by magnitude ---
def f12vp_f12_volume_pressure_risestreak_base_v127_signal(volume):
    av = _mean(volume, 5)
    up = (av > av.shift(1)).astype(float)
    grp = (up == 0).cumsum()
    streak = up.groupby(grp).cumsum()
    b = streak * np.log(av / _mean(volume, 63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- breadth of accumulation: fraction of last quarter with net buying pressure ---
def f12vp_f12_volume_pressure_accbreadth_63d_base_v128_signal(closeadj, volume):
    npress = _f12_net_press(closeadj, volume, 21)
    pos = (npress > 0).astype(float)
    frac = pos.rolling(63, min_periods=21).mean()
    b = frac + npress.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume-weighted return consistency (do high-vol days agree in direction) ---
def f12vp_f12_volume_pressure_volconsist_63d_base_v129_signal(closeadj, volume):
    # volume-weighted vs equal-weighted average return gap over a quarter
    # (do the heavy-volume days move price more than typical days?)
    ret = closeadj.pct_change()
    w = volume / _rsum(volume, 63).replace(0, np.nan)
    vwret = _rsum(w * ret, 63)
    ewret = _mean(ret, 63)
    b = (vwret - ewret) * 100.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- surge clustering: variance of relative volume over a quarter ---
def f12vp_f12_volume_pressure_relvolvar_63d_base_v130_signal(volume):
    rv = _f12_rel_vol(volume, 63)
    b = rv.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ratio of recent to prior half-window average volume (step change) ---
def f12vp_f12_volume_pressure_stepchg_126d_base_v131_signal(volume):
    recent = _mean(volume, 63)
    prior = _mean(volume.shift(63), 63)
    b = np.log(recent.replace(0, np.nan) / prior.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume skewness over a half year (asymmetry of activity) ---
def f12vp_f12_volume_pressure_volskew_126d_base_v132_signal(volume):
    b = volume.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume "shock" indicator: today's z vs the prior day's z (jump in abnormality) ---
def f12vp_f12_volume_pressure_volshock_base_v133_signal(volume):
    zz = _z(volume, 63)
    b = zz - zz.shift(1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- net dollar pressure minus net raw pressure (mix-adjusted flow) ---
def f12vp_f12_volume_pressure_mixflow_63d_base_v134_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f12_dollar_vol(closeadj, volume)
    dpress = _rsum(np.sign(ret) * dv, 63) / _rsum(dv, 63).replace(0, np.nan)
    vpress = _f12_net_press(closeadj, volume, 63)
    b = dpress - vpress
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- relative volume on the close-to-close gap days (continuation participation) ---
def f12vp_f12_volume_pressure_trendvol_63d_base_v135_signal(closeadj, volume):
    ret = closeadj.pct_change()
    trend = np.sign(closeadj - _mean(closeadj, 63))
    agree = (np.sign(ret) == trend).astype(float)
    rv = _f12_rel_vol(volume, 63)
    b = _rsum(agree * rv, 63) / _rsum(rv, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume regime transition: 21d avg crossing 126d avg, magnitude ---
def f12vp_f12_volume_pressure_regimecross_base_v136_signal(volume):
    fast = _mean(volume, 21)
    slow = _mean(volume, 126)
    spread = (fast - slow) / slow.replace(0, np.nan)
    b = spread - spread.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- dollar-volume Herfindahl over half-year (money clustering, distinct window) ---
def f12vp_f12_volume_pressure_dvolconc_126d_base_v137_signal(closeadj, volume):
    dv = _f12_dollar_vol(closeadj, volume)
    b = _f12_concentration(dv, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- coefficient of variation of dollar-volume (money-flow dispersion) ---
def f12vp_f12_volume_pressure_dvoliqr_63d_base_v138_signal(closeadj, volume):
    dv = _f12_dollar_vol(closeadj, volume)
    q75 = dv.rolling(63, min_periods=21).quantile(0.75)
    q25 = dv.rolling(63, min_periods=21).quantile(0.25)
    med = dv.rolling(63, min_periods=21).median()
    b = (q75 - q25) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- net buying pressure vs price trend divergence (vol confirms or fights price) ---
def f12vp_f12_volume_pressure_pvdiverge_63d_base_v139_signal(closeadj, volume):
    npress = _f12_net_press(closeadj, volume, 63)
    pmom = closeadj / closeadj.shift(63) - 1.0
    b = npress - np.tanh(5.0 * pmom)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- abnormal volume relative to a robust band, signed by recent return ---
def f12vp_f12_volume_pressure_signsurge_21d_base_v140_signal(closeadj, volume):
    rv = _f12_rel_vol(volume, 63)
    ret = closeadj.pct_change().rolling(5, min_periods=2).sum()
    b = np.log(rv) * np.sign(ret)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- fraction of dollar-volume traded on up days (money accumulation share) ---
def f12vp_f12_volume_pressure_updvolshare_126d_base_v141_signal(closeadj, volume):
    # trend in the up-day dollar-volume share: is accumulation strengthening?
    # 21d up-share minus 126d up-share (short minus long accumulation tilt)
    ret = closeadj.pct_change()
    dv = _f12_dollar_vol(closeadj, volume)
    up = dv.where(ret > 0, 0.0)
    short = _rsum(up, 21) / _rsum(dv, 21).replace(0, np.nan)
    long = _rsum(up, 126) / _rsum(dv, 126).replace(0, np.nan)
    b = short - long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- relative volume EWMA crossover (fast/slow exponential RVOL) ---
def f12vp_f12_volume_pressure_relvolxover_base_v142_signal(volume):
    rv = _f12_rel_vol(volume, 63)
    b = rv.ewm(span=5, min_periods=3).mean() - rv.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- variance ratio of volume (clustering across scales) ---
def f12vp_f12_volume_pressure_volvarratio_base_v143_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    v5 = (lv - lv.shift(5)).rolling(126, min_periods=63).var()
    v1 = (lv - lv.shift(1)).rolling(126, min_periods=63).var()
    b = v5 / (5.0 * v1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- climactic volume: big volume + big move together (blowoff proxy) ---
def f12vp_f12_volume_pressure_climax_21d_base_v144_signal(closeadj, volume):
    ret = closeadj.pct_change().abs()
    rv = _f12_rel_vol(volume, 63)
    climax = (rv * ret)
    b = climax.rolling(21, min_periods=10).max() * 100.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- volume trend quality: slope divided by dispersion (signal-to-noise of trend) ---
def f12vp_f12_volume_pressure_trendqual_63d_base_v145_signal(volume):
    lv = np.log(volume.replace(0, np.nan))
    sl = _slope(lv, 63)
    disp = _std(lv, 63)
    b = sl / disp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- net pressure intensity weighted by surge (pressure when volume is heavy) ---
def f12vp_f12_volume_pressure_heavypress_63d_base_v146_signal(closeadj, volume):
    # net buying pressure computed using only the heaviest-volume days of the quarter
    # (top-half-volume days), vs all-day pressure (smart-volume tilt)
    ret = closeadj.pct_change()
    med = volume.rolling(63, min_periods=21).median()
    heavy = volume.where(volume > med, 0.0)
    signed = np.sign(ret) * heavy
    b = _rsum(signed, 63) / _rsum(heavy, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- relative volume kurtosis (spikiness of recent activity) ---
def f12vp_f12_volume_pressure_relvolkurt_126d_base_v147_signal(volume):
    rv = _f12_rel_vol(volume, 126)
    b = rv.rolling(126, min_periods=63).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- decay of a volume spike: ratio of today's vol to its own 5d-ago spike ---
def f12vp_f12_volume_pressure_spikedecay_base_v148_signal(volume):
    av = _mean(volume, 3)
    spikeref = _rmax(volume.shift(1), 21)
    b = av / spikeref.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- long-horizon dollar-volume trend confirmation with price ---
def f12vp_f12_volume_pressure_dvolconf_252d_base_v149_signal(closeadj, volume):
    dv = np.log(_f12_dollar_vol(closeadj, volume).replace(0, np.nan))
    dvsl = _slope(dv, 252)
    pmom = closeadj / closeadj.shift(252) - 1.0
    b = dvsl * np.sign(pmom)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite volume-pressure score: surge x net-direction x trend ---
def f12vp_f12_volume_pressure_pressurescore_base_v150_signal(closeadj, volume):
    surge = np.log(_f12_surge(volume, 21, 126))
    npress = _f12_net_press(closeadj, volume, 63)
    trend = np.sign(closeadj / closeadj.shift(63) - 1.0)
    b = surge * npress * trend
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f12vp_f12_volume_pressure_dvolgrow_126d_base_v076_signal,
    f12vp_f12_volume_pressure_dvolgrow_63d_base_v077_signal,
    f12vp_f12_volume_pressure_dvolslope_126d_base_v078_signal,
    f12vp_f12_volume_pressure_dvoltrendq_63d_base_v079_signal,
    f12vp_f12_volume_pressure_dvolz_252d_base_v080_signal,
    f12vp_f12_volume_pressure_surge_3v21_base_v081_signal,
    f12vp_f12_volume_pressure_surge_10v63_base_v082_signal,
    f12vp_f12_volume_pressure_surge_42v252_base_v083_signal,
    f12vp_f12_volume_pressure_surgez_5v63_base_v084_signal,
    f12vp_f12_volume_pressure_surgerank_21v126_base_v085_signal,
    f12vp_f12_volume_pressure_netpress_21d_base_v086_signal,
    f12vp_f12_volume_pressure_netpress_126d_base_v087_signal,
    f12vp_f12_volume_pressure_netpressmom_63d_base_v088_signal,
    f12vp_f12_volume_pressure_upvolewma_base_v089_signal,
    f12vp_f12_volume_pressure_uddvol_63d_base_v090_signal,
    f12vp_f12_volume_pressure_volregime_126d_base_v091_signal,
    f12vp_f12_volume_pressure_volband_63d_base_v092_signal,
    f12vp_f12_volume_pressure_volpeakgap_252d_base_v093_signal,
    f12vp_f12_volume_pressure_volslope_126d_base_v094_signal,
    f12vp_f12_volume_pressure_volslopesm_21d_base_v095_signal,
    f12vp_f12_volume_pressure_volslopespr_base_v096_signal,
    f12vp_f12_volume_pressure_conc_126d_base_v097_signal,
    f12vp_f12_volume_pressure_top3share_63d_base_v098_signal,
    f12vp_f12_volume_pressure_volgini_63d_base_v099_signal,
    f12vp_f12_volume_pressure_spike2med_63d_base_v100_signal,
    f12vp_f12_volume_pressure_surgefreq_252d_base_v101_signal,
    f12vp_f12_volume_pressure_dayssincesurge_base_v102_signal,
    f12vp_f12_volume_pressure_bigdaymag_126d_base_v103_signal,
    f12vp_f12_volume_pressure_volvolcorr_63d_base_v104_signal,
    f12vp_f12_volume_pressure_voleffort_21d_base_v105_signal,
    f12vp_f12_volume_pressure_dvmix_126d_base_v106_signal,
    f12vp_f12_volume_pressure_volmom_63d_base_v107_signal,
    f12vp_f12_volume_pressure_volaccel2_base_v108_signal,
    f12vp_f12_volume_pressure_volewmom_base_v109_signal,
    f12vp_f12_volume_pressure_relvoldisp_252_base_v110_signal,
    f12vp_f12_volume_pressure_surgeterm_base_v111_signal,
    f12vp_f12_volume_pressure_volentropy_63d_base_v112_signal,
    f12vp_f12_volume_pressure_signdvolpr_21d_base_v113_signal,
    f12vp_f12_volume_pressure_dvolretw_63d_base_v114_signal,
    f12vp_f12_volume_pressure_eventvol_126d_base_v115_signal,
    f12vp_f12_volume_pressure_magasym_63d_base_v116_signal,
    f12vp_f12_volume_pressure_voltrendconf_126d_base_v117_signal,
    f12vp_f12_volume_pressure_pvcorr_63d_base_v118_signal,
    f12vp_f12_volume_pressure_voltailfreq_126d_base_v119_signal,
    f12vp_f12_volume_pressure_droughtfreq_base_v120_signal,
    f12vp_f12_volume_pressure_pressidx_63d_base_v121_signal,
    f12vp_f12_volume_pressure_accrank_126d_base_v122_signal,
    f12vp_f12_volume_pressure_dvolrel_252d_base_v123_signal,
    f12vp_f12_volume_pressure_dvolsurgerank_base_v124_signal,
    f12vp_f12_volume_pressure_volacf1_63d_base_v125_signal,
    f12vp_f12_volume_pressure_volchgacf_63d_base_v126_signal,
    f12vp_f12_volume_pressure_risestreak_base_v127_signal,
    f12vp_f12_volume_pressure_accbreadth_63d_base_v128_signal,
    f12vp_f12_volume_pressure_volconsist_63d_base_v129_signal,
    f12vp_f12_volume_pressure_relvolvar_63d_base_v130_signal,
    f12vp_f12_volume_pressure_stepchg_126d_base_v131_signal,
    f12vp_f12_volume_pressure_volskew_126d_base_v132_signal,
    f12vp_f12_volume_pressure_volshock_base_v133_signal,
    f12vp_f12_volume_pressure_mixflow_63d_base_v134_signal,
    f12vp_f12_volume_pressure_trendvol_63d_base_v135_signal,
    f12vp_f12_volume_pressure_regimecross_base_v136_signal,
    f12vp_f12_volume_pressure_dvolconc_126d_base_v137_signal,
    f12vp_f12_volume_pressure_dvoliqr_63d_base_v138_signal,
    f12vp_f12_volume_pressure_pvdiverge_63d_base_v139_signal,
    f12vp_f12_volume_pressure_signsurge_21d_base_v140_signal,
    f12vp_f12_volume_pressure_updvolshare_126d_base_v141_signal,
    f12vp_f12_volume_pressure_relvolxover_base_v142_signal,
    f12vp_f12_volume_pressure_volvarratio_base_v143_signal,
    f12vp_f12_volume_pressure_climax_21d_base_v144_signal,
    f12vp_f12_volume_pressure_trendqual_63d_base_v145_signal,
    f12vp_f12_volume_pressure_heavypress_63d_base_v146_signal,
    f12vp_f12_volume_pressure_relvolkurt_126d_base_v147_signal,
    f12vp_f12_volume_pressure_spikedecay_base_v148_signal,
    f12vp_f12_volume_pressure_dvolconf_252d_base_v149_signal,
    f12vp_f12_volume_pressure_pressurescore_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_VOLUME_PRESSURE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.005, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.01, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.01, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)) + 1e5, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

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

    print("OK f12_volume_pressure_base_076_150_claude: %d features pass" % n_features)
