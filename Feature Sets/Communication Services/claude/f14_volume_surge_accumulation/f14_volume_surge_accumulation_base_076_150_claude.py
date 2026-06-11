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
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).min()


def _med(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).median()


# ===== folder domain primitives: RAW VOLUME SURGE / ACCUMULATION ONLY =====
# Dollar-volume (closeadj*volume) belongs to f17; turnover/Amihud belong to f16.
# closeadj is used ONLY for the SIGN of the daily return, never as a dollar multiplier.
def _f14_ret_sign(closeadj):
    return np.sign(closeadj.pct_change())


def _f14_surge_ratio(volume, w):
    base = volume.rolling(w, min_periods=max(2, w // 2)).mean()
    return volume / base.replace(0, np.nan)


def _f14_surge_excess(volume, w, k):
    base = volume.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = volume.rolling(w, min_periods=max(2, w // 2)).std()
    return ((volume - base) / sd.replace(0, np.nan) - k).clip(lower=0)


def _f14_signed_vol_norm(closeadj, volume, w):
    nvol = volume / _mean(volume, w).replace(0, np.nan)
    return _f14_ret_sign(closeadj) * nvol


def _f14_signed_surgez(closeadj, volume, w):
    vz = _z(volume, w)
    return _f14_ret_sign(closeadj) * vz


# ============================================================
# --- SURGE-RATIO TRANSFORMS (sqrt / tanh / log compression of the surge multiple) ---

# tanh-squashed surge multiple smoothed over 21d (bounded participation intensity)
def f14vs_f14_volume_surge_accumulation_surgetanh_21d_base_v076_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    b = np.tanh(sr - 1.0).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log surge multiple over the 126d baseline (compressed long-horizon surge stretch)
def f14vs_f14_volume_surge_accumulation_logsurge_126d_base_v077_signal(volume):
    sr = _f14_surge_ratio(volume, 126)
    b = np.log(sr.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign-magnitude compressed surge vs its own 126d typical level (deviation, sqrt-scaled)
def f14vs_f14_volume_surge_accumulation_surgesqrt_63d_base_v078_signal(volume):
    sr = _f14_surge_ratio(volume, 126)
    typ = sr.rolling(126, min_periods=63).median()
    d = sr - typ
    b = np.sign(d) * d.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge multiple at 10d vs 126d baseline, de-trended by its own 63d level (medium surge stretch)
def f14vs_f14_volume_surge_accumulation_surge5v63_base_v079_signal(volume):
    s10 = _mean(volume, 10)
    base = _mean(volume, 126)
    r = np.log(s10.replace(0, np.nan) / base.replace(0, np.nan))
    b = r - r.rolling(63, min_periods=32).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge multiple acceleration: 21d surge-ratio slope minus its prior-month slope (onset accel)
def f14vs_f14_volume_surge_accumulation_surgeaccel_base_v080_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    slope = sr - sr.shift(21)
    b = slope - slope.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SURGE-DAY STRUCTURE (excess summaries that are NOT entropy/Gini/CV) ---

# mean standardized excess over POSITIVE-excess days only in 63d (typical surge size when surging)
def f14vs_f14_volume_surge_accumulation_meanexcess_63d_base_v081_signal(volume):
    base = _mean(volume, 63)
    sd = _std(volume, 63)
    z = (volume - base) / sd.replace(0, np.nan)
    pos = z.where(z > 0, np.nan)
    b = pos.rolling(63, min_periods=20).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge-day count change: 21d burst count now vs a quarter ago (short surge-regime shift)
def f14vs_f14_volume_surge_accumulation_burstchg_21d_base_v082_signal(volume):
    cnt = _f14_surge_excess(volume, 63, 1.5).rolling(21, min_periods=10).sum()
    b = cnt - cnt.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge drought: longest calm run over 126d, scaled by how calm the floor is (continuous)
def f14vs_f14_volume_surge_accumulation_surgedrought_base_v083_signal(volume):
    base = _mean(volume, 63)
    sd = _std(volume, 63)
    calm = (volume <= base + 2.0 * sd).astype(float)
    grp = (calm != calm.shift(1)).cumsum()
    run = (calm.groupby(grp).cumcount() + 1) * calm
    floor = _rmin(_f14_surge_ratio(volume, 63), 21)
    b = _rmax(run, 126) * floor
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 126d above the 126d-mean baseline, surge-magnitude weighted (broad heat)
def f14vs_f14_volume_surge_accumulation_broadheat_126d_base_v084_signal(volume):
    base = _mean(volume, 126)
    heat = (volume / base.replace(0, np.nan) - 1.0).clip(lower=0)
    b = heat.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike-versus-floor ratio: 21d max volume over 21d min volume (intra-month surge span, log)
def f14vs_f14_volume_surge_accumulation_spikefloor_21d_base_v085_signal(volume):
    hi = _rmax(volume, 21)
    lo = _rmin(volume, 21)
    b = np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- DIRECTIONAL ACCUMULATION (sign-based, NOT dollar, NOT raw turnover) ---

# 63d up-day surge excess minus down-day surge excess, summed (directional spike pressure)
def f14vs_f14_volume_surge_accumulation_dirspike_63d_base_v086_signal(closeadj, volume):
    ret = closeadj.pct_change()
    exc = _f14_surge_excess(volume, 63, 1.0)
    up = exc.where(ret > 0, 0.0).rolling(63, min_periods=32).sum()
    dn = exc.where(ret < 0, 0.0).rolling(63, min_periods=32).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weekly signed-volume tilt over 13 weeks (weekly accumulation, normalized RAW volume)
def f14vs_f14_volume_surge_accumulation_wkflow_base_v087_signal(closeadj, volume):
    ret5 = closeadj / closeadj.shift(5) - 1.0
    wkvol = volume.rolling(5).sum()
    signed = np.sign(ret5) * wkvol
    net = signed.rolling(63, min_periods=32).sum()
    tot = wkvol.rolling(63, min_periods=32).sum()
    b = net / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weekly accumulation breadth over 126d (net up-volume-dominant weeks, mag-weighted)
def f14vs_f14_volume_surge_accumulation_wkbreadth_base_v088_signal(closeadj, volume):
    ret5 = closeadj / closeadj.shift(5) - 1.0
    wkvol = volume.rolling(5).sum()
    nv = wkvol / _mean(wkvol, 63).replace(0, np.nan)
    contrib = np.sign(ret5) * nv
    b = contrib.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-volume conviction power: 126d mean of (up-vol normalized)^1.5 minus down-vol^1.5 (convex bias)
def f14vs_f14_volume_surge_accumulation_voldirpow_126d_base_v089_signal(closeadj, volume):
    ret = closeadj.pct_change()
    nv = volume / _mean(volume, 126).replace(0, np.nan)
    up = (nv.where(ret > 0, 0.0) ** 1.5).rolling(126, min_periods=63).mean()
    dn = (nv.where(ret < 0, 0.0) ** 1.5).rolling(126, min_periods=63).mean()
    b = up - dn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-surgez accumulation efficiency: |net 63d surgez travel| / total path (trend purity)
def f14vs_f14_volume_surge_accumulation_acceff_63d_base_v090_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 63).cumsum()
    net = (line - line.shift(63)).abs()
    path = line.diff().abs().rolling(63, min_periods=32).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation tilt CHANGE at 21d vs 63d horizon spread (flow front-loading)
def f14vs_f14_volume_surge_accumulation_flowspread_base_v091_signal(closeadj, volume):
    ret = closeadj.pct_change()
    sv = np.sign(ret) * volume
    t21 = sv.rolling(21, min_periods=10).sum() / volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    t63 = sv.rolling(63, min_periods=32).sum() / volume.rolling(63, min_periods=32).sum().replace(0, np.nan)
    b = t21 - t63
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# flow-spread momentum: the 21v63 flow spread now minus its level a month ago (flow jerk-as-level)
def f14vs_f14_volume_surge_accumulation_flowmom_base_v092_signal(closeadj, volume):
    ret = closeadj.pct_change()
    sv = np.sign(ret) * volume
    t21 = sv.rolling(21, min_periods=10).sum() / volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    t63 = sv.rolling(63, min_periods=32).sum() / volume.rolling(63, min_periods=32).sum().replace(0, np.nan)
    spread = t21 - t63
    b = spread - spread.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distribution warning: mean RAW volume on down-days relative to all-day mean over 21d (acute selling)
def f14vs_f14_volume_surge_accumulation_distrwarn_base_v093_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dnvol = volume.where(ret < 0, np.nan).rolling(21, min_periods=8).mean()
    allvol = _mean(volume, 21)
    b = np.log(dnvol / allvol.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation regime persistence: fraction of 252d the 21d up/down tilt stayed positive (centered)
def f14vs_f14_volume_surge_accumulation_accpersist_252d_base_v094_signal(closeadj, volume):
    ret = closeadj.pct_change()
    tilt = (np.sign(ret) * volume).rolling(21, min_periods=10).sum() \
        / volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    pos = (tilt > 0).astype(float)
    b = pos.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- VOLUME-PRICE CONVICTION (uses return sign / magnitude, never dollar level) ---

# effort-vs-result: 63d surge-ratio mean minus |63d price ROC| rank (heavy crowd, little move)
def f14vs_f14_volume_surge_accumulation_voleffort_63d_base_v095_signal(closeadj, volume):
    surge_rk = _mean(_f14_surge_ratio(volume, 63), 21).rolling(252, min_periods=63).rank(pct=True)
    move = (closeadj / closeadj.shift(63) - 1.0).abs()
    move_rk = move.rolling(252, min_periods=63).rank(pct=True)
    b = surge_rk - move_rk
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# climactic exhaustion: surge-excess on reversal days, summed over 63d (magnitude-weighted)
def f14vs_f14_volume_surge_accumulation_exhaust_63d_base_v096_signal(closeadj, volume):
    ret = closeadj.pct_change()
    exc = _f14_surge_excess(volume, 63, 1.0)
    rev = (np.sign(ret) != np.sign(ret.shift(1))).astype(float)
    b = (exc * rev).rolling(63, min_periods=32).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge-day directional consistency: agreement of return sign on the 5 loudest 63d days
def f14vs_f14_volume_surge_accumulation_loudagree_63d_base_v097_signal(closeadj, volume):
    ret = closeadj.pct_change()
    thr = volume.rolling(63, min_periods=32).quantile(0.92)
    big = volume >= thr
    signs = (np.sign(ret) * big.astype(float))
    netsign = signs.rolling(63, min_periods=32).sum()
    count = big.astype(float).rolling(63, min_periods=32).sum()
    b = netsign / count.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# return per surge unit on up-days vs down-days (does buying-surge move price more?) 63d
def f14vs_f14_volume_surge_accumulation_movepersurge_base_v098_signal(closeadj, volume):
    ret = closeadj.pct_change()
    exc = (_f14_surge_ratio(volume, 63) - 1.0).clip(lower=0)
    upmove = (ret.where(ret > 0, 0.0) * exc).rolling(63, min_periods=32).sum()
    dnmove = (ret.where(ret < 0, 0.0).abs() * exc).rolling(63, min_periods=32).sum()
    b = (upmove - dnmove) / (upmove + dnmove).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SURGE PERSISTENCE / STREAK VARIANTS (raw volume, distinct from 001-075) ---

# surge-streak: consecutive days with surge ratio > 1.25, scaled by current surge multiple
def f14vs_f14_volume_surge_accumulation_surgestreak_base_v099_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    hot = (sr > 1.25).astype(float)
    grp = (hot != hot.shift(1)).cumsum()
    run = (hot.groupby(grp).cumcount() + 1) * hot
    b = run * sr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# quiet-streak: consecutive days BELOW 21d-mean volume, scaled by depth (calm-before-storm)
def f14vs_f14_volume_surge_accumulation_quietstreak_base_v100_signal(volume):
    m = _mean(volume, 21)
    cool = (volume < m).astype(float)
    grp = (cool != cool.shift(1)).cumsum()
    run = (cool.groupby(grp).cumcount() + 1) * cool
    depth = (m / volume.replace(0, np.nan)).clip(lower=1.0)
    b = run * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge ratio interquartile spread over 63d: q75 minus q25 of the daily surge multiple (regime body width)
def f14vs_f14_volume_surge_accumulation_postpeak_base_v101_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    q75 = sr.rolling(63, min_periods=32).quantile(0.75)
    q25 = sr.rolling(63, min_periods=32).quantile(0.25)
    b = q75 - q25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pre-surge calm: 21d-min surge ratio (how quiet the quietest recent day was)
def f14vs_f14_volume_surge_accumulation_presurgecalm_base_v102_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    b = _rmin(sr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge half-life proxy: ratio of summed excess in days 1-5 vs days 6-21 after window start
def f14vs_f14_volume_surge_accumulation_surgedecay_base_v103_signal(volume):
    exc = _f14_surge_excess(volume, 63, 1.0)
    recent = exc.rolling(5, min_periods=3).sum()
    older = exc.shift(5).rolling(16, min_periods=8).sum()
    b = recent / (recent + older).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SURGE-RATIO MOMENTUM / DRIFT (level facets distinct from slope file) ---

# surge ratio drift: log-OLS slope of daily surge ratio over 63d (steady surge build)
def f14vs_f14_volume_surge_accumulation_surgedrift_63d_base_v104_signal(volume):
    sr = _f14_surge_ratio(volume, 63)

    def _slope(a):
        x = np.arange(len(a), dtype=float)
        xc = x - x.mean()
        denom = (xc ** 2).sum()
        if denom == 0:
            return np.nan
        return float((xc * (a - a.mean())).sum() / denom)
    b = sr.rolling(63, min_periods=32).apply(_slope, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# participation expansion convexity: (5v21 surge) minus (21v63 surge) (short-burst convexity)
def f14vs_f14_volume_surge_accumulation_expconvex_base_v105_signal(volume):
    a = np.log(_mean(volume, 5).replace(0, np.nan) / _mean(volume, 21).replace(0, np.nan))
    c = np.log(_mean(volume, 21).replace(0, np.nan) / _mean(volume, 63).replace(0, np.nan))
    b = a - c
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year participation change: log 63d-mean volume now vs one year ago (annual growth)
def f14vs_f14_volume_surge_accumulation_volyoy_base_v106_signal(volume):
    m = _mean(volume, 63)
    b = np.log(m.replace(0, np.nan) / m.shift(252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# participation-step ACCELERATION: month-over-month log step now minus its value a month ago
def f14vs_f14_volume_surge_accumulation_volmom_step_base_v107_signal(volume):
    m = _mean(volume, 21)
    step = np.log(m.replace(0, np.nan) / m.shift(21).replace(0, np.nan))
    b = step - step.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge-ratio percentile distance from 0.5: how extreme the smoothed surge stands vs 252d
def f14vs_f14_volume_surge_accumulation_surgepctl_252d_base_v108_signal(volume):
    sr = _mean(_f14_surge_ratio(volume, 21), 5)
    b = (sr.rolling(252, min_periods=63).rank(pct=True) - 0.5).abs()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SURGE INTERACTION WITH VOLATILITY OF VOLUME (vol-of-surge variants) ---

# surge instability: 21d std of the surge ratio over its own 21d mean (relative jitter)
def f14vs_f14_volume_surge_accumulation_surgejitter_21d_base_v109_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    b = sr.rolling(21, min_periods=10).std() / sr.rolling(21, min_periods=10).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-surge change: 63d surge-ratio std now minus a quarter ago (instability trend)
def f14vs_f14_volume_surge_accumulation_surgevolchg_base_v110_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    sv = sr.rolling(63, min_periods=32).std()
    b = sv - sv.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# peak prominence: loudest 63d surge multiple over the 63d median surge multiple (spike sharpness)
def f14vs_f14_volume_surge_accumulation_surgeswing_63d_base_v111_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    peak = _rmax(sr, 63)
    med = sr.rolling(63, min_periods=32).median()
    b = peak / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# clumping of surges: max 5-day-summed surge excess in 63d vs its 63d total (burst clustering)
def f14vs_f14_volume_surge_accumulation_surgeclump_base_v112_signal(volume):
    exc = _f14_surge_excess(volume, 63, 1.0)
    win5 = exc.rolling(5, min_periods=3).sum()
    top5 = _rmax(win5, 63)
    tot = exc.rolling(63, min_periods=32).sum()
    b = top5 / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- LONG-HORIZON SURGE REGIME / POSITION ---

# surge regime z over 252d: smoothed surge ratio standardized vs a long history
def f14vs_f14_volume_surge_accumulation_surgez_252d_base_v113_signal(volume):
    sr = _mean(_f14_surge_ratio(volume, 63), 21)
    b = _z(sr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-year participation position: 63d-mean within its 504d min-max band
def f14vs_f14_volume_surge_accumulation_volregpos_504d_base_v114_signal(volume):
    base = _mean(volume, 63)
    hi = _rmax(base, 504)
    lo = _rmin(base, 504)
    b = (base - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of current 63d-mean above its 252d floor (lift off the participation floor, log)
def f14vs_f14_volume_surge_accumulation_floorlift_252d_base_v115_signal(volume):
    base = _mean(volume, 63)
    floor = _rmin(base, 252)
    b = np.log(base.replace(0, np.nan) / floor.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance of current 63d-mean below its 252d ceiling (room under participation peak, log)
def f14vs_f14_volume_surge_accumulation_ceilroom_252d_base_v116_signal(volume):
    base = _mean(volume, 63)
    ceil = _rmax(base, 252)
    b = np.log(base.replace(0, np.nan) / ceil.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# participation drawdown velocity: change in (63d-mean vs 252d-peak) over a quarter (fade speed)
def f14vs_f14_volume_surge_accumulation_partfade_base_v117_signal(volume):
    base = _mean(volume, 63)
    dd = base / _rmax(base, 252).replace(0, np.nan) - 1.0
    b = dd - dd.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SURGE-CONDITIONED ACCUMULATION (combining magnitude and direction, raw) ---

# net signed surge excess over 126d (directional spike accumulation, long horizon)
def f14vs_f14_volume_surge_accumulation_netsurge_126d_base_v118_signal(closeadj, volume):
    sign = _f14_ret_sign(closeadj)
    exc = _f14_surge_excess(volume, 126, 1.0)
    b = (sign * exc).rolling(126, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge-weighted return momentum: 21d-summed (sign x surge-excess), de-trended by 126d mean
def f14vs_f14_volume_surge_accumulation_surgemomflow_base_v119_signal(closeadj, volume):
    sign = _f14_ret_sign(closeadj)
    exc = _f14_surge_excess(volume, 63, 1.0)
    flow = (sign * exc).rolling(21, min_periods=10).sum()
    b = flow - flow.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-surge energy share of TOTAL raw volume over 63d (how much of all volume is up-directed spikes)
def f14vs_f14_volume_surge_accumulation_buyshare_63d_base_v120_signal(closeadj, volume):
    ret = closeadj.pct_change()
    exc = _f14_surge_excess(volume, 63, 1.5)
    upenergy = (exc * volume).where(ret > 0, 0.0).rolling(63, min_periods=32).sum()
    totvol = volume.rolling(63, min_periods=32).sum()
    b = upenergy / totvol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional surge tilt momentum: 63d dir-spike balance now minus a quarter ago (regime shift)
def f14vs_f14_volume_surge_accumulation_dirtiltmom_base_v121_signal(closeadj, volume):
    ret = closeadj.pct_change()
    exc = _f14_surge_excess(volume, 63, 1.0)
    up = exc.where(ret > 0, 0.0).rolling(63, min_periods=32).sum()
    dn = exc.where(ret < 0, 0.0).rolling(63, min_periods=32).sum()
    bal = (up - dn) / (up + dn).replace(0, np.nan)
    b = bal - bal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- WEEKLY / MULTI-DAY AGGREGATION (raw volume) ---

# weekly signed-flow z: 5d signed (by weekly return) volume tilt z-scored vs 13-week history
def f14vs_f14_volume_surge_accumulation_wksurgez_base_v122_signal(closeadj, volume):
    ret5 = closeadj / closeadj.shift(5) - 1.0
    wk = volume.rolling(5).sum()
    tilt = np.sign(ret5) * wk
    sm = tilt.rolling(21, min_periods=10).sum() / wk.rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = _z(sm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weekly surge acceleration: weekly-volume log-ratio change over 4 weeks (weekly onset)
def f14vs_f14_volume_surge_accumulation_wkaccel_base_v123_signal(volume):
    wk = volume.rolling(5).sum()
    r = np.log(wk.replace(0, np.nan) / wk.shift(5).replace(0, np.nan))
    b = r - r.shift(20)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5d-block max-day share within the week: how concentrated weekly volume is in one day
def f14vs_f14_volume_surge_accumulation_dayspike_base_v124_signal(volume):
    daymax = _rmax(volume, 5)
    wk = volume.rolling(5, min_periods=3).sum()
    b = daymax / wk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SURGE FREQUENCY REGIME & RARE-EVENT INTENSITY ---

# extreme-spike intensity: summed (surge ratio - 1.8)+ over 126d (rare blowoff energy)
def f14vs_f14_volume_surge_accumulation_extspike_126d_base_v125_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    b = (sr - 1.8).clip(lower=0).rolling(126, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge frequency at 1-sd vs 2-sd thresholds (shape of the surge tail) 126d
def f14vs_f14_volume_surge_accumulation_tailshape_126d_base_v126_signal(volume):
    base = _mean(volume, 126)
    sd = _std(volume, 126)
    z = (volume - base) / sd.replace(0, np.nan)
    c1 = (z > 1.0).astype(float).rolling(126, min_periods=63).sum()
    c2 = (z > 2.0).astype(float).rolling(126, min_periods=63).sum()
    b = c2 / (c1 + 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge intensity now vs a year ago: 63d summed excess minus its value 252d back (annual shift)
def f14vs_f14_volume_surge_accumulation_surgeyoy_base_v127_signal(volume):
    cnt = _f14_surge_excess(volume, 63, 1.5).rolling(63, min_periods=32).sum()
    b = cnt - cnt.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share of last 252d in an elevated-participation regime (above 252d-median 21d-mean), centered
def f14vs_f14_volume_surge_accumulation_hiregime_252d_base_v128_signal(volume):
    base = _mean(volume, 21)
    med = _med(base, 252)
    above = (base > med).astype(float)
    b = above.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regime crossings: count of 21d-mean crossing its 252d-median over a year (participation toggling)
def f14vs_f14_volume_surge_accumulation_regcross_252d_base_v129_signal(volume):
    base = _mean(volume, 21)
    med = _med(base, 252)
    above = (base > med).astype(float)
    cross = (above != above.shift(1)).astype(float)
    b = cross.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- ACCUMULATION-LINE LONG VARIANTS / SIGN-MAGNITUDE COMPRESSION ---

# long signed-surge accumulation distance vs 252d mean (multi-quarter flow extension)
def f14vs_f14_volume_surge_accumulation_accdist_252d_base_v130_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 126).cumsum()
    b = (line - _mean(line, 252)) / _std(line, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign-magnitude compressed net flow: sqrt-scaled signed 63d normalized-volume tilt
def f14vs_f14_volume_surge_accumulation_flowsignmag_base_v131_signal(closeadj, volume):
    ret = closeadj.pct_change()
    tilt = (np.sign(ret) * volume).rolling(63, min_periods=32).sum() \
        / volume.rolling(63, min_periods=32).sum().replace(0, np.nan)
    b = np.sign(tilt) * tilt.abs() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation tilt vs its own slow EMA (flow displacement, normalized RAW volume)
def f14vs_f14_volume_surge_accumulation_flowdisp_base_v132_signal(closeadj, volume):
    sv = _f14_signed_vol_norm(closeadj, volume, 63)
    tilt = sv.rolling(21, min_periods=10).mean()
    b = tilt - tilt.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation-line new-high recency over 252d (how recently flow set a fresh long peak)
def f14vs_f14_volume_surge_accumulation_accnewhi_252d_base_v133_signal(closeadj, volume):
    line = _f14_signed_surgez(closeadj, volume, 126).cumsum()

    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = line.rolling(252, min_periods=126).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- SURGE-PRICE EFFICIENCY / DIVERGENCE VARIANTS ---

# flow-vs-price rank divergence over 63d (signed flow leads/lags the price return)
def f14vs_f14_volume_surge_accumulation_flowpricediv_base_v134_signal(closeadj, volume):
    ret = closeadj.pct_change()
    flow = (np.sign(ret) * volume).rolling(63, min_periods=32).sum() \
        / volume.rolling(63, min_periods=32).sum().replace(0, np.nan)
    flow_rk = flow.rolling(252, min_periods=63).rank(pct=True)
    roc = closeadj / closeadj.shift(63) - 1.0
    roc_rk = roc.rolling(252, min_periods=63).rank(pct=True)
    b = flow_rk - roc_rk
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge-vs-volatility divergence: 63d surge-ratio mean minus return-vol rank (crowd vs risk) 63d
def f14vs_f14_volume_surge_accumulation_surgevoldiv_base_v135_signal(closeadj, volume):
    surge_rk = _mean(_f14_surge_ratio(volume, 63), 21).rolling(252, min_periods=63).rank(pct=True)
    rv = closeadj.pct_change().rolling(63, min_periods=32).std()
    rv_rk = rv.rolling(252, min_periods=63).rank(pct=True)
    b = surge_rk - rv_rk
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge-day return DISPERSION: std of returns on top-quartile volume days vs all days over 126d
def f14vs_f14_volume_surge_accumulation_vwret_63d_base_v136_signal(closeadj, volume):
    ret = closeadj.pct_change()
    thr = volume.rolling(126, min_periods=63).quantile(0.75)
    bigstd = ret.where(volume >= thr, np.nan).rolling(126, min_periods=20).std()
    allstd = ret.rolling(126, min_periods=63).std()
    b = bigstd / allstd.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge-day price-impact asymmetry: avg |return| on surge days vs calm days over 126d
def f14vs_f14_volume_surge_accumulation_impactasym_base_v137_signal(closeadj, volume):
    ar = closeadj.pct_change().abs()
    thr = volume.rolling(126, min_periods=63).quantile(0.80)
    surge = ar.where(volume >= thr, np.nan).rolling(126, min_periods=20).mean()
    calm = ar.where(volume < thr, np.nan).rolling(126, min_periods=20).mean()
    b = np.log(surge / calm.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- RESIDUAL SURGE MAGNITUDE / SMOOTHING FACETS ---

# volume-floor displacement: 21d-min volume vs its own 63d-min (is the calm floor rising or falling)
def f14vs_f14_volume_surge_accumulation_surgedispema_base_v138_signal(volume):
    lo21 = _rmin(volume, 21)
    lo63 = _rmin(volume, 63)
    b = np.log(lo21.replace(0, np.nan) / lo63.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge ratio EMA level (persistent participation intensity over ~month)
def f14vs_f14_volume_surge_accumulation_surgeema_base_v139_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    b = sr.ewm(span=21, min_periods=10).mean() - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log-volume EMA stretch: today's log volume minus its 63d EMA, smoothed (persistent stretch)
def f14vs_f14_volume_surge_accumulation_logvolstretch_base_v140_signal(volume):
    lv = np.log(volume.clip(lower=1.0))
    b = (lv - lv.ewm(span=63, min_periods=21).mean()).rolling(10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# short excess-breach energy: summed log(volume/q75) on days above the 63d 75th-pct over 21d, de-leveled
def f14vs_f14_volume_surge_accumulation_q75frac_21d_base_v141_signal(volume):
    q75 = volume.rolling(63, min_periods=32).quantile(0.75)
    over = np.log(volume / q75.replace(0, np.nan)).clip(lower=0)
    energy = over.rolling(21, min_periods=10).sum()
    cnt = (volume > q75).astype(float).rolling(21, min_periods=10).sum()
    b = energy - 0.05 * cnt
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge symmetry vs median: signed log distance of volume from its 63d median, smoothed
def f14vs_f14_volume_surge_accumulation_medsym_63d_base_v142_signal(volume):
    med = _med(volume, 63)
    d = np.sign(volume - med) * np.log1p((volume - med).abs() / med.replace(0, np.nan))
    b = d.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge skewness proxy: (mean surge ratio - median surge ratio) over 63d (right-tail pull)
def f14vs_f14_volume_surge_accumulation_surgehotcnt_63d_base_v143_signal(volume):
    sr = _f14_surge_ratio(volume, 63)
    b = sr.rolling(63, min_periods=32).mean() - sr.rolling(63, min_periods=32).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d-mean surge ratio over 126d-mean surge ratio (short vs long participation regime ratio)
def f14vs_f14_volume_surge_accumulation_regimeratio_base_v144_signal(volume):
    s21 = _mean(_f14_surge_ratio(volume, 21), 21)
    s126 = _mean(_f14_surge_ratio(volume, 126), 21)
    b = s21 / s126.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation balance trend over 63d (21d up/down volume balance minus quarter-ago value)
def f14vs_f14_volume_surge_accumulation_accbaltrend_base_v145_signal(closeadj, volume):
    ret = closeadj.pct_change()
    up = volume.where(ret > 0, 0.0).rolling(21, min_periods=10).sum()
    dn = volume.where(ret < 0, 0.0).rolling(21, min_periods=10).sum()
    bal = (up - dn) / (up + dn).replace(0, np.nan)
    b = bal - bal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike-day return skew proxy: net sign of returns on the 10 loudest 126d days (event tilt)
def f14vs_f14_volume_surge_accumulation_loudtilt_126d_base_v146_signal(closeadj, volume):
    ret = closeadj.pct_change()
    thr = volume.rolling(126, min_periods=63).quantile(0.92)
    big = volume >= thr
    netsign = (np.sign(ret) * big.astype(float)).rolling(126, min_periods=63).sum()
    cnt = big.astype(float).rolling(126, min_periods=63).sum()
    b = netsign / cnt.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge onset vs persistence: short surge ratio minus its own 63d max (distance from recent peak)
def f14vs_f14_volume_surge_accumulation_peakgap_base_v147_signal(volume):
    sr = _f14_surge_ratio(volume, 21)
    peak = _rmax(sr, 63)
    b = sr / peak.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net accumulation efficiency long: |126d signed-vol net| / path, scaled by loudness (long purity)
def f14vs_f14_volume_surge_accumulation_acceff_126d_base_v148_signal(closeadj, volume):
    ret = closeadj.pct_change()
    signed = np.sign(ret) * volume
    net = signed.rolling(126, min_periods=63).sum().abs()
    path = signed.abs().rolling(126, min_periods=63).sum()
    eff = net / path.replace(0, np.nan)
    loud = _mean(volume, 126) / _mean(volume, 252).replace(0, np.nan)
    b = eff * loud
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge momentum interaction: surge-rank times signed flow tilt (loud AND directional) 63d
def f14vs_f14_volume_surge_accumulation_loudflowint_base_v149_signal(closeadj, volume):
    ret = closeadj.pct_change()
    surge_rk = _mean(_f14_surge_ratio(volume, 63), 21).rolling(252, min_periods=63).rank(pct=True) - 0.5
    tilt = (np.sign(ret) * volume).rolling(63, min_periods=32).sum() \
        / volume.rolling(63, min_periods=32).sum().replace(0, np.nan)
    b = surge_rk * tilt
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite surge-accumulation health: blend of surge rank, up-share tilt, and rising base
def f14vs_f14_volume_surge_accumulation_health_base_v150_signal(closeadj, volume):
    ret = closeadj.pct_change()
    surge_rk = _mean(_f14_surge_ratio(volume, 63), 21).rolling(252, min_periods=63).rank(pct=True) - 0.5
    up = volume.where(ret > 0, 0.0).rolling(63, min_periods=32).sum()
    tot = volume.rolling(63, min_periods=32).sum()
    tilt = up / tot.replace(0, np.nan) - 0.5
    rising = np.log(_mean(volume, 63).replace(0, np.nan) / _mean(volume, 252).replace(0, np.nan))
    b = surge_rk + tilt + np.tanh(rising)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f14vs_f14_volume_surge_accumulation_surgetanh_21d_base_v076_signal,
    f14vs_f14_volume_surge_accumulation_logsurge_126d_base_v077_signal,
    f14vs_f14_volume_surge_accumulation_surgesqrt_63d_base_v078_signal,
    f14vs_f14_volume_surge_accumulation_surge5v63_base_v079_signal,
    f14vs_f14_volume_surge_accumulation_surgeaccel_base_v080_signal,
    f14vs_f14_volume_surge_accumulation_meanexcess_63d_base_v081_signal,
    f14vs_f14_volume_surge_accumulation_burstchg_21d_base_v082_signal,
    f14vs_f14_volume_surge_accumulation_surgedrought_base_v083_signal,
    f14vs_f14_volume_surge_accumulation_broadheat_126d_base_v084_signal,
    f14vs_f14_volume_surge_accumulation_spikefloor_21d_base_v085_signal,
    f14vs_f14_volume_surge_accumulation_dirspike_63d_base_v086_signal,
    f14vs_f14_volume_surge_accumulation_wkflow_base_v087_signal,
    f14vs_f14_volume_surge_accumulation_wkbreadth_base_v088_signal,
    f14vs_f14_volume_surge_accumulation_voldirpow_126d_base_v089_signal,
    f14vs_f14_volume_surge_accumulation_acceff_63d_base_v090_signal,
    f14vs_f14_volume_surge_accumulation_flowspread_base_v091_signal,
    f14vs_f14_volume_surge_accumulation_flowmom_base_v092_signal,
    f14vs_f14_volume_surge_accumulation_distrwarn_base_v093_signal,
    f14vs_f14_volume_surge_accumulation_accpersist_252d_base_v094_signal,
    f14vs_f14_volume_surge_accumulation_voleffort_63d_base_v095_signal,
    f14vs_f14_volume_surge_accumulation_exhaust_63d_base_v096_signal,
    f14vs_f14_volume_surge_accumulation_loudagree_63d_base_v097_signal,
    f14vs_f14_volume_surge_accumulation_movepersurge_base_v098_signal,
    f14vs_f14_volume_surge_accumulation_surgestreak_base_v099_signal,
    f14vs_f14_volume_surge_accumulation_quietstreak_base_v100_signal,
    f14vs_f14_volume_surge_accumulation_postpeak_base_v101_signal,
    f14vs_f14_volume_surge_accumulation_presurgecalm_base_v102_signal,
    f14vs_f14_volume_surge_accumulation_surgedecay_base_v103_signal,
    f14vs_f14_volume_surge_accumulation_surgedrift_63d_base_v104_signal,
    f14vs_f14_volume_surge_accumulation_expconvex_base_v105_signal,
    f14vs_f14_volume_surge_accumulation_volyoy_base_v106_signal,
    f14vs_f14_volume_surge_accumulation_volmom_step_base_v107_signal,
    f14vs_f14_volume_surge_accumulation_surgepctl_252d_base_v108_signal,
    f14vs_f14_volume_surge_accumulation_surgejitter_21d_base_v109_signal,
    f14vs_f14_volume_surge_accumulation_surgevolchg_base_v110_signal,
    f14vs_f14_volume_surge_accumulation_surgeswing_63d_base_v111_signal,
    f14vs_f14_volume_surge_accumulation_surgeclump_base_v112_signal,
    f14vs_f14_volume_surge_accumulation_surgez_252d_base_v113_signal,
    f14vs_f14_volume_surge_accumulation_volregpos_504d_base_v114_signal,
    f14vs_f14_volume_surge_accumulation_floorlift_252d_base_v115_signal,
    f14vs_f14_volume_surge_accumulation_ceilroom_252d_base_v116_signal,
    f14vs_f14_volume_surge_accumulation_partfade_base_v117_signal,
    f14vs_f14_volume_surge_accumulation_netsurge_126d_base_v118_signal,
    f14vs_f14_volume_surge_accumulation_surgemomflow_base_v119_signal,
    f14vs_f14_volume_surge_accumulation_buyshare_63d_base_v120_signal,
    f14vs_f14_volume_surge_accumulation_dirtiltmom_base_v121_signal,
    f14vs_f14_volume_surge_accumulation_wksurgez_base_v122_signal,
    f14vs_f14_volume_surge_accumulation_wkaccel_base_v123_signal,
    f14vs_f14_volume_surge_accumulation_dayspike_base_v124_signal,
    f14vs_f14_volume_surge_accumulation_extspike_126d_base_v125_signal,
    f14vs_f14_volume_surge_accumulation_tailshape_126d_base_v126_signal,
    f14vs_f14_volume_surge_accumulation_surgeyoy_base_v127_signal,
    f14vs_f14_volume_surge_accumulation_hiregime_252d_base_v128_signal,
    f14vs_f14_volume_surge_accumulation_regcross_252d_base_v129_signal,
    f14vs_f14_volume_surge_accumulation_accdist_252d_base_v130_signal,
    f14vs_f14_volume_surge_accumulation_flowsignmag_base_v131_signal,
    f14vs_f14_volume_surge_accumulation_flowdisp_base_v132_signal,
    f14vs_f14_volume_surge_accumulation_accnewhi_252d_base_v133_signal,
    f14vs_f14_volume_surge_accumulation_flowpricediv_base_v134_signal,
    f14vs_f14_volume_surge_accumulation_surgevoldiv_base_v135_signal,
    f14vs_f14_volume_surge_accumulation_vwret_63d_base_v136_signal,
    f14vs_f14_volume_surge_accumulation_impactasym_base_v137_signal,
    f14vs_f14_volume_surge_accumulation_surgedispema_base_v138_signal,
    f14vs_f14_volume_surge_accumulation_surgeema_base_v139_signal,
    f14vs_f14_volume_surge_accumulation_logvolstretch_base_v140_signal,
    f14vs_f14_volume_surge_accumulation_q75frac_21d_base_v141_signal,
    f14vs_f14_volume_surge_accumulation_medsym_63d_base_v142_signal,
    f14vs_f14_volume_surge_accumulation_surgehotcnt_63d_base_v143_signal,
    f14vs_f14_volume_surge_accumulation_regimeratio_base_v144_signal,
    f14vs_f14_volume_surge_accumulation_accbaltrend_base_v145_signal,
    f14vs_f14_volume_surge_accumulation_loudtilt_126d_base_v146_signal,
    f14vs_f14_volume_surge_accumulation_peakgap_base_v147_signal,
    f14vs_f14_volume_surge_accumulation_acceff_126d_base_v148_signal,
    f14vs_f14_volume_surge_accumulation_loudflowint_base_v149_signal,
    f14vs_f14_volume_surge_accumulation_health_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F14_VOLUME_SURGE_ACCUMULATION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "volume": volume}

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs=%s" % (name, meta["inputs"])
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

    print("OK f14_volume_surge_accumulation_base_076_150_claude: %d features pass" % n_features)
