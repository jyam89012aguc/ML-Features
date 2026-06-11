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
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives: discovery / re-rating signature =====
def _f36_dollar_vol(closeadj, volume):
    return (closeadj * volume).astype(float)


def _f36_breakout(closeadj, w):
    prior_hi = closeadj.shift(1).rolling(w, min_periods=max(2, w // 2)).max()
    return closeadj / prior_hi.replace(0, np.nan) - 1.0


def _f36_base_pos(closeadj, w):
    hi = _rmax(closeadj, w)
    lo = _rmin(closeadj, w)
    return (closeadj - lo) / (hi - lo).replace(0, np.nan)


def _f36_vol_surge(closeadj, volume, w):
    dv = _f36_dollar_vol(closeadj, volume)
    base = dv.rolling(w, min_periods=max(2, w // 2)).mean()
    return np.log(dv.replace(0, np.nan) / base.replace(0, np.nan))


def _f36_ret_vol(closeadj, w):
    return closeadj.pct_change().rolling(w, min_periods=max(2, w // 2)).std()


def _f36_vol_expand(closeadj, short, long):
    vs = _f36_ret_vol(closeadj, short)
    vl = _f36_ret_vol(closeadj, long)
    return vs / vl.replace(0, np.nan)


def _f36_range_atr(high, low, closeadj, w):
    rng = (high - low)
    return (rng.rolling(w, min_periods=max(2, w // 2)).mean()) / closeadj.replace(0, np.nan)


def _f36_thrust(closeadj, w):
    return np.log(closeadj.replace(0, np.nan) / closeadj.shift(w).replace(0, np.nan))


def _f36_squash(x):
    return np.tanh(x)


# ============================================================
# ---- breakout facets (continued) ----

# breakout above 504d base (multi-year discovery to new highs)
def f36dr_f36_discovery_rerating_signature_brk_504d_base_v076_signal(closeadj):
    b = _f36_breakout(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout above 21d micro-base, smoothed over a week (fast re-rating onset)
def f36dr_f36_discovery_rerating_signature_brk_21d_base_v077_signal(closeadj):
    raw = _f36_breakout(closeadj, 21)
    b = raw.rolling(5, min_periods=3).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base-position spread: 63d base-pos minus 252d base-pos (short vs long coil)
def f36dr_f36_discovery_rerating_signature_baseposspr_base_v078_signal(closeadj):
    s = _f36_base_pos(closeadj, 63)
    l = _f36_base_pos(closeadj, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout quality: 126d breakout times the fraction of last month above the prior base
def f36dr_f36_discovery_rerating_signature_brkqual_126d_base_v079_signal(closeadj):
    prior_hi = closeadj.shift(1).rolling(126, min_periods=63).max()
    brk = (closeadj / prior_hi.replace(0, np.nan) - 1.0).clip(lower=0)
    held = (closeadj > prior_hi).astype(float).rolling(21, min_periods=10).mean()
    b = brk * held
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pullback depth from recent 21d high weighted by how high in the 126d base price sits
def f36dr_f36_discovery_rerating_signature_pullback_base_v080_signal(closeadj):
    hi21 = _rmax(closeadj, 21)
    pull = (closeadj / hi21.replace(0, np.nan) - 1.0)
    bp = _f36_base_pos(closeadj, 126)
    b = pull * bp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-126d-high creation staircase: log-slope of the rolling 126d max over a quarter
def f36dr_f36_discovery_rerating_signature_staircase_126d_base_v081_signal(closeadj):
    hi = _rmax(closeadj, 126)
    b = np.log(hi.replace(0, np.nan) / hi.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout extension above 63d base, percentile-ranked vs 252d history
def f36dr_f36_discovery_rerating_signature_brkrnk_63d_base_v082_signal(closeadj):
    brk = _f36_breakout(closeadj, 63)
    b = _rank(brk, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# headroom remaining to the 252d high (inverse breakout — base distance below the ceiling)
def f36dr_f36_discovery_rerating_signature_headroom_252d_base_v083_signal(closeadj):
    hi = _rmax(closeadj, 252)
    b = np.log(hi.replace(0, np.nan) / closeadj.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- volume facets (continued) ----

# dollar-volume z-score (raw liquidity surprise) over a quarter
def f36dr_f36_discovery_rerating_signature_dvz_63d_base_v084_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    b = _z(dv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity expansion ratio: 63d-avg dollar-vol over 252d-avg, smoothed (structural step)
def f36dr_f36_discovery_rerating_signature_liqexp_base_v085_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    short = dv.rolling(63, min_periods=21).mean()
    long = dv.rolling(252, min_periods=126).mean()
    b = (short / long.replace(0, np.nan)).ewm(span=10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume concentration: share of last quarter's dollar-vol in its top 5 days (spikiness)
def f36dr_f36_discovery_rerating_signature_volconc_63d_base_v086_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    total = dv.rolling(63, min_periods=21).sum()
    top5 = dv.rolling(63, min_periods=21).apply(
        lambda a: np.sort(a)[-5:].sum() if len(a) >= 5 else np.nan, raw=True)
    b = top5 / total.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume trend: slope of log dollar-volume over a quarter (OLS-style via cov)
def f36dr_f36_discovery_rerating_signature_voltrend_63d_base_v087_signal(closeadj, volume):
    ldv = np.log(_f36_dollar_vol(closeadj, volume).replace(0, np.nan))
    idx = pd.Series(np.arange(len(ldv), dtype=float), index=ldv.index)
    w = 63
    mx = idx.rolling(w, min_periods=21).mean()
    my = ldv.rolling(w, min_periods=21).mean()
    cov = (idx * ldv).rolling(w, min_periods=21).mean() - mx * my
    varx = (idx * idx).rolling(w, min_periods=21).mean() - mx * mx
    b = cov / varx.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Amihud-style illiquidity collapse: |return|/dollar-vol falling (re-rating into liquidity)
def f36dr_f36_discovery_rerating_signature_amihud_base_v088_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    illiq = (closeadj.pct_change().abs() / dv.replace(0, np.nan))
    short = illiq.rolling(21, min_periods=10).mean()
    long = illiq.rolling(126, min_periods=63).mean()
    b = -np.log(short.replace(0, np.nan) / long.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# turnover acceleration: 21d-avg share volume vs 63d-avg, z-scored
def f36dr_f36_discovery_rerating_signature_turnaccel_base_v089_signal(volume):
    short = volume.rolling(21, min_periods=10).mean()
    long = volume.rolling(63, min_periods=21).mean()
    ratio = short / long.replace(0, np.nan)
    b = _z(ratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume coefficient of variation (spiky junior turnover regime)
def f36dr_f36_discovery_rerating_signature_dvcv_63d_base_v090_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    cv = dv.rolling(63, min_periods=21).std() / dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
    b = cv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- volatility facets (continued) ----

# downside vs upside vol asymmetry expansion (re-ratings expand upside vol)
def f36dr_f36_discovery_rerating_signature_volasym_base_v091_signal(closeadj):
    ret = closeadj.pct_change()
    up = ret.where(ret > 0).rolling(63, min_periods=21).std()
    dn = ret.where(ret < 0).rolling(63, min_periods=21).std()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson-style high-low vol expansion: 21d vs 126d (intraday range volatility)
def f36dr_f36_discovery_rerating_signature_parkexp_base_v092_signal(high, low):
    hl = (np.log(high.replace(0, np.nan) / low.replace(0, np.nan))) ** 2
    short = np.sqrt(hl.rolling(21, min_periods=10).mean())
    long = np.sqrt(hl.rolling(126, min_periods=63).mean())
    b = short / long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-expansion percentile vs 252d history (regime placement of 21v63 expansion)
def f36dr_f36_discovery_rerating_signature_volexprnk_base_v093_signal(closeadj):
    ratio = _f36_vol_expand(closeadj, 21, 63)
    b = _rank(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-expansion momentum: change in 21v126 expansion over a quarter
def f36dr_f36_discovery_rerating_signature_volexpmom_base_v094_signal(closeadj):
    ratio = _f36_vol_expand(closeadj, 21, 126)
    b = ratio - ratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-truncation flag intensity: how far 5d range exceeds 252d-typical, summed (month)
def f36dr_f36_discovery_rerating_signature_rngblow_base_v095_signal(high, low, closeadj):
    amp = _f36_range_atr(high, low, closeadj, 5)
    typ = amp.rolling(252, min_periods=126).median()
    excess = (amp / typ.replace(0, np.nan) - 1.0).clip(lower=0)
    b = excess.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-of-vol expansion: dispersion of 5d vol relative to its 63d level
def f36dr_f36_discovery_rerating_signature_volofvol_base_v096_signal(closeadj):
    v = _f36_ret_vol(closeadj, 5)
    b = v.rolling(63, min_periods=21).std() / v.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range/return-vol ratio change (intraday energy vs close-to-close energy, monthly delta)
def f36dr_f36_discovery_rerating_signature_intraenergy_base_v097_signal(high, low, closeadj):
    rng = _f36_range_atr(high, low, closeadj, 21)
    rv = _f36_ret_vol(closeadj, 21)
    ratio = rng / rv.replace(0, np.nan)
    b = ratio - ratio.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- composite / signature facets (continued) ----

# triple-driver product over short windows (fast discovery spike: 21d/21d/5v21)
def f36dr_f36_discovery_rerating_signature_fastspike_base_v098_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 21).clip(lower=0)
    vs = _f36_vol_surge(closeadj, volume, 21).clip(lower=0)
    ve = (_f36_vol_expand(closeadj, 5, 21) - 1.0).clip(lower=0)
    b = brk * vs * ve
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted composite: 0.5*breakout-z + 0.3*surge-z + 0.2*expansion-z (tilted to price)
def f36dr_f36_discovery_rerating_signature_wcomp_base_v099_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    b = 0.5 * brk + 0.3 * vs + 0.2 * ve
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# product of base-position and volume rank and vol-expansion rank (coiled-loaded-energized)
def f36dr_f36_discovery_rerating_signature_loaded_base_v100_signal(closeadj, volume):
    bp = _f36_base_pos(closeadj, 63)
    vr = _rank(_f36_dollar_vol(closeadj, volume), 126) + 0.5
    ver = _rank(_f36_vol_expand(closeadj, 21, 126), 126) + 0.5
    b = bp * vr * ver
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# discovery signature change: monthly delta of the standardized triple-sum
def f36dr_f36_discovery_rerating_signature_sigdelta_base_v101_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    comp = (brk + vs + ve) / 3.0
    b = comp - comp.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# harmonic-mean composite of the three positive drivers (penalizes any weak link)
def f36dr_f36_discovery_rerating_signature_harmcomp_base_v102_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 126).clip(lower=0) + 1e-4
    vs = _f36_vol_surge(closeadj, volume, 63).clip(lower=0) + 1e-4
    ve = (_f36_vol_expand(closeadj, 21, 126) - 1.0).clip(lower=0) + 1e-4
    b = 3.0 / (1.0 / brk + 1.0 / vs + 1.0 / ve)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout x surge with NO volatility leg (price+liquidity only, 126d/126d)
def f36dr_f36_discovery_rerating_signature_brkvol_126d_base_v103_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 126)
    vs = _f36_vol_surge(closeadj, volume, 126)
    b = brk * vs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# discovery-spike EMA-smoothed level (persistent signature, 63d drivers)
def f36dr_f36_discovery_rerating_signature_spikeema_base_v104_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 63).clip(lower=0)
    vs = _f36_vol_surge(closeadj, volume, 63).clip(lower=0)
    ve = (_f36_vol_expand(closeadj, 5, 63) - 1.0).clip(lower=0)
    raw = brk * vs * ve
    b = raw.ewm(span=10, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- sustained re-rating momentum (continued) ----

# 21d thrust confirmed by volume surge (fast re-rating leg)
def f36dr_f36_discovery_rerating_signature_thrustconf_21d_base_v105_signal(closeadj, volume):
    thr = _f36_thrust(closeadj, 21)
    vs = _f36_vol_surge(closeadj, volume, 63).clip(lower=0)
    b = thr * (1.0 + vs)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-horizon thrust agreement: sign-consistency of 21/63/126d thrust
def f36dr_f36_discovery_rerating_signature_thrustagree_base_v106_signal(closeadj):
    t1 = np.sign(_f36_thrust(closeadj, 21))
    t2 = np.sign(_f36_thrust(closeadj, 63))
    t3 = np.sign(_f36_thrust(closeadj, 126))
    mag = _f36_thrust(closeadj, 63).abs()
    b = (t1 + t2 + t3) / 3.0 * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# re-rating smoothness: 126d thrust divided by max drawdown over that window
def f36dr_f36_discovery_rerating_signature_smoothrise_base_v107_signal(closeadj):
    thr = _f36_thrust(closeadj, 126)
    roll_max = closeadj.rolling(126, min_periods=63).max()
    dd = (roll_max - closeadj.rolling(126, min_periods=63).min()) / roll_max.replace(0, np.nan)
    b = thr / (dd + 0.05)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# thrust persistence: fraction of last quarter with rising 21d EMA of price
def f36dr_f36_discovery_rerating_signature_emaup_base_v108_signal(closeadj):
    ema = closeadj.ewm(span=21, min_periods=10).mean()
    rising = (ema > ema.shift(1)).astype(float)
    raw = rising.rolling(63, min_periods=21).mean()
    b = raw * _f36_thrust(closeadj, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend strength: 63d thrust per unit of path length traveled (efficiency ratio)
def f36dr_f36_discovery_rerating_signature_efficiency_base_v109_signal(closeadj):
    net = (closeadj - closeadj.shift(63)).abs()
    path = closeadj.diff().abs().rolling(63, min_periods=21).sum()
    er = net / path.replace(0, np.nan)
    b = er * np.sign(_f36_thrust(closeadj, 63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# re-rating velocity vs 252d typical: 21d thrust vs its own 252d std (standout move)
def f36dr_f36_discovery_rerating_signature_standout_base_v110_signal(closeadj):
    thr21 = _f36_thrust(closeadj, 21)
    b = thr21 / thr21.rolling(252, min_periods=126).std().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- richer interactions ----

# breakout x liquidity-expansion: price clearing base while liquidity structurally steps up
def f36dr_f36_discovery_rerating_signature_brkliq_base_v111_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 126).clip(lower=0)
    dv = _f36_dollar_vol(closeadj, volume)
    liq = np.log(dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
                 / dv.rolling(252, min_periods=126).mean().replace(0, np.nan)).clip(lower=0)
    b = brk * liq
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base-position x vol-expansion: coiled tight then volatility opens up (pre-break loading)
def f36dr_f36_discovery_rerating_signature_coilexp_base_v112_signal(closeadj):
    bp = _f36_base_pos(closeadj, 63)
    ve = _f36_vol_expand(closeadj, 5, 63) - 1.0
    b = bp * ve
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation-then-breakout: up/down dollar-vol balance times current breakout depth
def f36dr_f36_discovery_rerating_signature_accumbreak_base_v113_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f36_dollar_vol(closeadj, volume)
    upv = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    dnv = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    bal = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    brk = _f36_breakout(closeadj, 126).clip(lower=0)
    b = bal * brk
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-led discovery: surge present but price still inside the base (stealth accumulation)
def f36dr_f36_discovery_rerating_signature_stealth_base_v114_signal(closeadj, volume):
    vs = _f36_vol_surge(closeadj, volume, 63).clip(lower=0)
    bp = _f36_base_pos(closeadj, 126)
    below_top = (1.0 - bp).clip(lower=0)
    b = vs * below_top
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# climax-risk signature: extreme thrust + extreme surge + extreme vol (blow-off top warning)
def f36dr_f36_discovery_rerating_signature_climax_base_v115_signal(closeadj, volume):
    thr = _rank(_f36_thrust(closeadj, 21), 252) + 0.5
    vs = _rank(_f36_vol_surge(closeadj, volume, 63), 252) + 0.5
    ve = _rank(_f36_vol_expand(closeadj, 5, 63), 252) + 0.5
    b = thr * vs * ve
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout failure signature: was above base last month, now back below (failed re-rating)
def f36dr_f36_discovery_rerating_signature_failbreak_base_v116_signal(closeadj):
    base126 = closeadj.shift(1).rolling(126, min_periods=63).max()
    above = (closeadj > base126).astype(float)
    was_above = above.shift(21)
    fail = ((was_above == 1) & (above == 0)).astype(float)
    depth = (base126 / closeadj.replace(0, np.nan) - 1.0).clip(lower=0)
    b = fail.rolling(21, min_periods=10).mean() + depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ---- additional distinct facets to complete 75 ----

# breakout extension in Parkinson-vol units (break per unit intraday risk)
def f36dr_f36_discovery_rerating_signature_brkpark_base_v117_signal(closeadj, high, low):
    brk = _f36_breakout(closeadj, 126)
    hl = np.sqrt(((np.log(high.replace(0, np.nan) / low.replace(0, np.nan))) ** 2).rolling(21, min_periods=10).mean())
    b = brk / hl.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume surge x intraday-range expansion (energy without requiring a price break)
def f36dr_f36_discovery_rerating_signature_surgerange_base_v118_signal(closeadj, volume, high, low):
    vs = _f36_vol_surge(closeadj, volume, 63)
    short = _f36_range_atr(high, low, closeadj, 5)
    long = _f36_range_atr(high, low, closeadj, 63)
    rexp = short / long.replace(0, np.nan) - 1.0
    b = vs * rexp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity-to-252d-high momentum: how close-to-high changed over a quarter
def f36dr_f36_discovery_rerating_signature_proxmom_base_v119_signal(closeadj):
    hi = _rmax(closeadj, 252)
    prox = closeadj / hi.replace(0, np.nan)
    b = prox - prox.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-high frequency weighted by volume: fraction of month at new 63d high, vol-weighted
def f36dr_f36_discovery_rerating_signature_vwnewhi_base_v120_signal(closeadj, volume):
    hi = _rmax(closeadj, 63)
    at_hi = (closeadj >= hi * 0.999).astype(float)
    dv = _f36_dollar_vol(closeadj, volume)
    dvr = _rank(dv, 126) + 0.5
    b = (at_hi * dvr).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# thrust z-scored vs 252d history, confirmed by sign of volume balance
def f36dr_f36_discovery_rerating_signature_thrustzconf_base_v121_signal(closeadj, volume):
    thrz = _z(_f36_thrust(closeadj, 63), 252)
    ret = closeadj.pct_change()
    dv = _f36_dollar_vol(closeadj, volume)
    upv = dv.where(ret > 0, 0.0).rolling(63, min_periods=21).sum()
    dnv = dv.where(ret < 0, 0.0).rolling(63, min_periods=21).sum()
    bal = (upv - dnv) / (upv + dnv).replace(0, np.nan)
    b = thrz * (0.5 + bal)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-expansion gated by direction: 21v126 intraday-range expansion x sign of 5d thrust
def f36dr_f36_discovery_rerating_signature_rngthrust_base_v122_signal(high, low, closeadj):
    short = _f36_range_atr(high, low, closeadj, 21)
    long = _f36_range_atr(high, low, closeadj, 126)
    rexp = short / long.replace(0, np.nan) - 1.0
    direction = np.sign(_f36_thrust(closeadj, 5))
    b = rexp * direction
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout decay: how fast the 126d breakout has faded from its quarter peak
def f36dr_f36_discovery_rerating_signature_brkdecay_base_v123_signal(closeadj):
    brk = _f36_breakout(closeadj, 126)
    peak = brk.rolling(63, min_periods=21).max()
    b = brk - peak
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-confirmed new-high streak: consecutive-ish days near 126d high x volume rank
def f36dr_f36_discovery_rerating_signature_streakliq_base_v124_signal(closeadj, volume):
    hi = _rmax(closeadj, 126)
    near = (closeadj >= hi * 0.97).astype(float)
    streak = near.rolling(21, min_periods=10).sum()
    dvr = _rank(_f36_dollar_vol(closeadj, volume), 252) + 0.5
    b = streak * dvr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-adjusted breakout slope: change in (breakout/vol) over a month
def f36dr_f36_discovery_rerating_signature_brkvolslope_base_v125_signal(closeadj):
    brk = _f36_breakout(closeadj, 126)
    vol = _f36_ret_vol(closeadj, 63)
    ratio = brk / vol.replace(0, np.nan)
    b = ratio - ratio.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# discovery breadth across windows: mean breakout over 21/63/126/252 bases
def f36dr_f36_discovery_rerating_signature_brkbreadth_base_v126_signal(closeadj):
    b1 = _f36_breakout(closeadj, 21)
    b2 = _f36_breakout(closeadj, 63)
    b3 = _f36_breakout(closeadj, 126)
    b4 = _f36_breakout(closeadj, 252)
    b = pd.concat([b1, b2, b3, b4], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout dispersion across windows (disagreement of short vs long bases)
def f36dr_f36_discovery_rerating_signature_brkdisp_base_v127_signal(closeadj):
    b1 = _f36_breakout(closeadj, 21)
    b2 = _f36_breakout(closeadj, 63)
    b3 = _f36_breakout(closeadj, 126)
    b4 = _f36_breakout(closeadj, 252)
    b = pd.concat([b1, b2, b3, b4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# surge breadth across windows: mean dollar-vol surge over 21/63/126 bases
def f36dr_f36_discovery_rerating_signature_surgebreadth_base_v128_signal(closeadj, volume):
    s1 = _f36_vol_surge(closeadj, volume, 21)
    s2 = _f36_vol_surge(closeadj, volume, 63)
    s3 = _f36_vol_surge(closeadj, volume, 126)
    b = pd.concat([s1, s2, s3], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite signature smoothed and ranked vs year history (headline percentile)
def f36dr_f36_discovery_rerating_signature_headrank_base_v129_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    comp = (brk + vs + ve) / 3.0
    b = _rank(comp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volatility-expansion x liquidity-step: vol opens while liquidity structurally rises
def f36dr_f36_discovery_rerating_signature_volliq_base_v130_signal(closeadj, volume):
    ve = (_f36_vol_expand(closeadj, 21, 126) - 1.0).clip(lower=0)
    dv = _f36_dollar_vol(closeadj, volume)
    liq = np.log(dv.rolling(21, min_periods=10).mean().replace(0, np.nan)
                 / dv.rolling(126, min_periods=63).mean().replace(0, np.nan)).clip(lower=0)
    b = ve * liq
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last quarter spent breaking out (above prior 63d base), depth-weighted
def f36dr_f36_discovery_rerating_signature_brktime_base_v131_signal(closeadj):
    prior_hi = closeadj.shift(1).rolling(63, min_periods=21).max()
    ext = (closeadj / prior_hi.replace(0, np.nan) - 1.0).clip(lower=0)
    b = ext.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# discovery re-rating slope vs base: 126d thrust per unit base width (move vs prior coil)
def f36dr_f36_discovery_rerating_signature_thrustcoil_base_v132_signal(closeadj):
    thr = _f36_thrust(closeadj, 126)
    hi = closeadj.shift(126).rolling(63, min_periods=21).max()
    lo = closeadj.shift(126).rolling(63, min_periods=21).min()
    width = (hi - lo) / hi.replace(0, np.nan)
    b = thr / (width + 0.05)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume surge minus return — surge that exceeds what the price move would justify
def f36dr_f36_discovery_rerating_signature_excesssurge_base_v133_signal(closeadj, volume):
    vs = _f36_vol_surge(closeadj, volume, 63)
    thr = _f36_thrust(closeadj, 5).abs()
    b = vs - 20.0 * thr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# discovery composite gated by being in the upper half of the 252d base
def f36dr_f36_discovery_rerating_signature_upperhalf_base_v134_signal(closeadj, volume):
    bp = _f36_base_pos(closeadj, 252)
    gate = (bp > 0.5).astype(float)
    vs = _f36_vol_surge(closeadj, volume, 63)
    ve = _f36_vol_expand(closeadj, 21, 126) - 1.0
    b = gate * (vs + ve)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spike recency: days since the largest dollar-vol day in the last quarter (freshness)
def f36dr_f36_discovery_rerating_signature_spikerecency_base_v135_signal(closeadj, volume):
    dv = _f36_dollar_vol(closeadj, volume)
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    b = dv.rolling(63, min_periods=21).apply(_f, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout sustainability: 126d new-high count x mean base-position over the quarter
def f36dr_f36_discovery_rerating_signature_sustainbreak_base_v136_signal(closeadj):
    hi = _rmax(closeadj, 126)
    at_hi = (closeadj >= hi * 0.999).astype(float)
    newhi = at_hi.rolling(63, min_periods=21).sum()
    bp = _f36_base_pos(closeadj, 126).rolling(63, min_periods=21).mean()
    b = newhi * bp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-expansion regime distance: 21d Parkinson vol minus its own 252d median
def f36dr_f36_discovery_rerating_signature_parkregime_base_v137_signal(high, low):
    hl = np.sqrt(((np.log(high.replace(0, np.nan) / low.replace(0, np.nan))) ** 2).rolling(21, min_periods=10).mean())
    med = hl.rolling(252, min_periods=126).median()
    b = (hl - med) / med.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# triple-driver tanh composite over short windows, EMA-smoothed
def f36dr_f36_discovery_rerating_signature_shortblend_base_v138_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 63), 63)
    vs = _z(_f36_vol_surge(closeadj, volume, 21), 63)
    ve = _z(_f36_vol_expand(closeadj, 5, 63), 63)
    raw = _f36_squash((brk + vs + ve) / 3.0)
    b = raw.ewm(span=5, min_periods=3).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# re-rating return skew: rolling 63d skewness of daily returns (discovery = positive skew)
def f36dr_f36_discovery_rerating_signature_energybudget_base_v139_signal(closeadj):
    ret = closeadj.pct_change()
    b = ret.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout x surge x thrust (all three positive-leaning, magnitude product)
def f36dr_f36_discovery_rerating_signature_tripthrust_base_v140_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 126).clip(lower=0)
    vs = _f36_vol_surge(closeadj, volume, 63).clip(lower=0)
    thr = _f36_thrust(closeadj, 63).clip(lower=0)
    b = brk * vs * thr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-rank vs breakout-rank gap (which is leading the discovery)
def f36dr_f36_discovery_rerating_signature_leadgap_base_v141_signal(closeadj, volume):
    dvr = _rank(_f36_dollar_vol(closeadj, volume), 252)
    brkr = _rank(_f36_breakout(closeadj, 126), 252)
    b = dvr - brkr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-expansion confirmed breakout, z-scored composite over a year
def f36dr_f36_discovery_rerating_signature_vebrkz_base_v142_signal(closeadj):
    brk = _f36_breakout(closeadj, 126)
    ve = _f36_vol_expand(closeadj, 21, 126) - 1.0
    raw = brk * ve.clip(lower=0)
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation slope: OLS slope of cumulative signed dollar-vol over a quarter, normalized
def f36dr_f36_discovery_rerating_signature_accumslope_base_v143_signal(closeadj, volume):
    ret = closeadj.pct_change()
    dv = _f36_dollar_vol(closeadj, volume)
    obv = (np.sign(ret) * dv).cumsum()
    idx = pd.Series(np.arange(len(obv), dtype=float), index=obv.index)
    w = 63
    mx = idx.rolling(w, min_periods=21).mean()
    my = obv.rolling(w, min_periods=21).mean()
    cov = (idx * obv).rolling(w, min_periods=21).mean() - mx * my
    varx = (idx * idx).rolling(w, min_periods=21).mean() - mx * mx
    slope = cov / varx.replace(0, np.nan)
    base = dv.rolling(63, min_periods=21).mean()
    b = slope / base.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout above 126d base normalized by the 252d amplitude (break vs full-range travel)
def f36dr_f36_discovery_rerating_signature_brkamp_base_v144_signal(closeadj):
    brk = _f36_breakout(closeadj, 126)
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    amp = (hi - lo) / closeadj.replace(0, np.nan)
    b = brk / amp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustained discovery: 63d thrust x liquidity-step x vol-expansion (full re-rating engine)
def f36dr_f36_discovery_rerating_signature_engine_base_v145_signal(closeadj, volume):
    thr = _f36_thrust(closeadj, 63).clip(lower=0)
    dv = _f36_dollar_vol(closeadj, volume)
    liq = np.log(dv.rolling(63, min_periods=21).mean().replace(0, np.nan)
                 / dv.rolling(252, min_periods=126).mean().replace(0, np.nan)).clip(lower=0)
    ve = (_f36_vol_expand(closeadj, 21, 126) - 1.0).clip(lower=0)
    b = thr * (1.0 + liq) * (1.0 + ve)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# discovery composite minus its own 126d EMA (signature displacement / fresh impulse)
def f36dr_f36_discovery_rerating_signature_impulse_base_v146_signal(closeadj, volume):
    brk = _z(_f36_breakout(closeadj, 126), 126)
    vs = _z(_f36_vol_surge(closeadj, volume, 63), 126)
    ve = _z(_f36_vol_expand(closeadj, 21, 126), 126)
    comp = (brk + vs + ve) / 3.0
    b = comp - comp.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# percent of last year at a fresh 252d high, volume-weighted (re-rating leadership)
def f36dr_f36_discovery_rerating_signature_leadership_base_v147_signal(closeadj, volume):
    hi = _rmax(closeadj, 252)
    fresh = (closeadj >= hi * 0.999).astype(float)
    dvr = _rank(_f36_dollar_vol(closeadj, volume), 252) + 0.5
    b = (fresh * dvr).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expansion-confirmed thrust ranked vs year (where today's confirmed move sits)
def f36dr_f36_discovery_rerating_signature_confrank_base_v148_signal(closeadj):
    thr = _f36_thrust(closeadj, 21)
    ve = _f36_vol_expand(closeadj, 5, 63)
    raw = thr * ve
    b = _rank(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# discovery half-life: breakout depth divided by its own decay rate (durability proxy)
def f36dr_f36_discovery_rerating_signature_durability_base_v149_signal(closeadj):
    brk = _f36_breakout(closeadj, 126).clip(lower=0)
    decay = (brk.shift(21) - brk).clip(lower=0) + 0.01
    b = brk / decay
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# full discovery score: weighted geometric blend of breakout, surge, expansion, thrust
def f36dr_f36_discovery_rerating_signature_fullscore_base_v150_signal(closeadj, volume):
    brk = _f36_breakout(closeadj, 126).clip(lower=0) + 1e-4
    vs = _f36_vol_surge(closeadj, volume, 63).clip(lower=0) + 1e-4
    ve = (_f36_vol_expand(closeadj, 21, 126) - 1.0).clip(lower=0) + 1e-4
    thr = _f36_thrust(closeadj, 63).clip(lower=0) + 1e-4
    b = (brk * vs * ve * thr) ** 0.25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36dr_f36_discovery_rerating_signature_brk_504d_base_v076_signal,
    f36dr_f36_discovery_rerating_signature_brk_21d_base_v077_signal,
    f36dr_f36_discovery_rerating_signature_baseposspr_base_v078_signal,
    f36dr_f36_discovery_rerating_signature_brkqual_126d_base_v079_signal,
    f36dr_f36_discovery_rerating_signature_pullback_base_v080_signal,
    f36dr_f36_discovery_rerating_signature_staircase_126d_base_v081_signal,
    f36dr_f36_discovery_rerating_signature_brkrnk_63d_base_v082_signal,
    f36dr_f36_discovery_rerating_signature_headroom_252d_base_v083_signal,
    f36dr_f36_discovery_rerating_signature_dvz_63d_base_v084_signal,
    f36dr_f36_discovery_rerating_signature_liqexp_base_v085_signal,
    f36dr_f36_discovery_rerating_signature_volconc_63d_base_v086_signal,
    f36dr_f36_discovery_rerating_signature_voltrend_63d_base_v087_signal,
    f36dr_f36_discovery_rerating_signature_amihud_base_v088_signal,
    f36dr_f36_discovery_rerating_signature_turnaccel_base_v089_signal,
    f36dr_f36_discovery_rerating_signature_dvcv_63d_base_v090_signal,
    f36dr_f36_discovery_rerating_signature_volasym_base_v091_signal,
    f36dr_f36_discovery_rerating_signature_parkexp_base_v092_signal,
    f36dr_f36_discovery_rerating_signature_volexprnk_base_v093_signal,
    f36dr_f36_discovery_rerating_signature_volexpmom_base_v094_signal,
    f36dr_f36_discovery_rerating_signature_rngblow_base_v095_signal,
    f36dr_f36_discovery_rerating_signature_volofvol_base_v096_signal,
    f36dr_f36_discovery_rerating_signature_intraenergy_base_v097_signal,
    f36dr_f36_discovery_rerating_signature_fastspike_base_v098_signal,
    f36dr_f36_discovery_rerating_signature_wcomp_base_v099_signal,
    f36dr_f36_discovery_rerating_signature_loaded_base_v100_signal,
    f36dr_f36_discovery_rerating_signature_sigdelta_base_v101_signal,
    f36dr_f36_discovery_rerating_signature_harmcomp_base_v102_signal,
    f36dr_f36_discovery_rerating_signature_brkvol_126d_base_v103_signal,
    f36dr_f36_discovery_rerating_signature_spikeema_base_v104_signal,
    f36dr_f36_discovery_rerating_signature_thrustconf_21d_base_v105_signal,
    f36dr_f36_discovery_rerating_signature_thrustagree_base_v106_signal,
    f36dr_f36_discovery_rerating_signature_smoothrise_base_v107_signal,
    f36dr_f36_discovery_rerating_signature_emaup_base_v108_signal,
    f36dr_f36_discovery_rerating_signature_efficiency_base_v109_signal,
    f36dr_f36_discovery_rerating_signature_standout_base_v110_signal,
    f36dr_f36_discovery_rerating_signature_brkliq_base_v111_signal,
    f36dr_f36_discovery_rerating_signature_coilexp_base_v112_signal,
    f36dr_f36_discovery_rerating_signature_accumbreak_base_v113_signal,
    f36dr_f36_discovery_rerating_signature_stealth_base_v114_signal,
    f36dr_f36_discovery_rerating_signature_climax_base_v115_signal,
    f36dr_f36_discovery_rerating_signature_failbreak_base_v116_signal,
    f36dr_f36_discovery_rerating_signature_brkpark_base_v117_signal,
    f36dr_f36_discovery_rerating_signature_surgerange_base_v118_signal,
    f36dr_f36_discovery_rerating_signature_proxmom_base_v119_signal,
    f36dr_f36_discovery_rerating_signature_vwnewhi_base_v120_signal,
    f36dr_f36_discovery_rerating_signature_thrustzconf_base_v121_signal,
    f36dr_f36_discovery_rerating_signature_rngthrust_base_v122_signal,
    f36dr_f36_discovery_rerating_signature_brkdecay_base_v123_signal,
    f36dr_f36_discovery_rerating_signature_streakliq_base_v124_signal,
    f36dr_f36_discovery_rerating_signature_brkvolslope_base_v125_signal,
    f36dr_f36_discovery_rerating_signature_brkbreadth_base_v126_signal,
    f36dr_f36_discovery_rerating_signature_brkdisp_base_v127_signal,
    f36dr_f36_discovery_rerating_signature_surgebreadth_base_v128_signal,
    f36dr_f36_discovery_rerating_signature_headrank_base_v129_signal,
    f36dr_f36_discovery_rerating_signature_volliq_base_v130_signal,
    f36dr_f36_discovery_rerating_signature_brktime_base_v131_signal,
    f36dr_f36_discovery_rerating_signature_thrustcoil_base_v132_signal,
    f36dr_f36_discovery_rerating_signature_excesssurge_base_v133_signal,
    f36dr_f36_discovery_rerating_signature_upperhalf_base_v134_signal,
    f36dr_f36_discovery_rerating_signature_spikerecency_base_v135_signal,
    f36dr_f36_discovery_rerating_signature_sustainbreak_base_v136_signal,
    f36dr_f36_discovery_rerating_signature_parkregime_base_v137_signal,
    f36dr_f36_discovery_rerating_signature_shortblend_base_v138_signal,
    f36dr_f36_discovery_rerating_signature_energybudget_base_v139_signal,
    f36dr_f36_discovery_rerating_signature_tripthrust_base_v140_signal,
    f36dr_f36_discovery_rerating_signature_leadgap_base_v141_signal,
    f36dr_f36_discovery_rerating_signature_vebrkz_base_v142_signal,
    f36dr_f36_discovery_rerating_signature_accumslope_base_v143_signal,
    f36dr_f36_discovery_rerating_signature_brkamp_base_v144_signal,
    f36dr_f36_discovery_rerating_signature_engine_base_v145_signal,
    f36dr_f36_discovery_rerating_signature_impulse_base_v146_signal,
    f36dr_f36_discovery_rerating_signature_leadership_base_v147_signal,
    f36dr_f36_discovery_rerating_signature_confrank_base_v148_signal,
    f36dr_f36_discovery_rerating_signature_durability_base_v149_signal,
    f36dr_f36_discovery_rerating_signature_fullscore_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_DISCOVERY_RERATING_SIGNATURE_REGISTRY_076_150 = REGISTRY


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

    print("OK f36_discovery_rerating_signature_base_076_150_claude: %d features pass" % n_features)
