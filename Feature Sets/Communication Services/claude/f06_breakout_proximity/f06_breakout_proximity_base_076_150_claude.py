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


# ===== folder domain primitives (breakout proximity / Donchian) =====
def _f06_donch_pos(price, w):
    hi = price.rolling(w, min_periods=max(1, w // 2)).max()
    lo = price.rolling(w, min_periods=max(1, w // 2)).min()
    return (price - lo) / (hi - lo).replace(0, np.nan)


def _f06_dist_high(price, w):
    hi = price.rolling(w, min_periods=max(1, w // 2)).max()
    return price / hi.replace(0, np.nan) - 1.0


def _f06_dist_low(price, w):
    lo = price.rolling(w, min_periods=max(1, w // 2)).min()
    return price / lo.replace(0, np.nan) - 1.0


def _f06_prior_high(price, w):
    return price.shift(1).rolling(w, min_periods=max(1, w // 2)).max()


def _f06_prior_low(price, w):
    return price.shift(1).rolling(w, min_periods=max(1, w // 2)).min()


def _f06_days_since_high(price, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    return price.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f06_days_since_low(price, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    return price.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f06_atr(high, low, w):
    return (high - low).rolling(w, min_periods=max(1, w // 2)).mean()


def _f06_band_width(price, w):
    hi = price.rolling(w, min_periods=max(1, w // 2)).max()
    lo = price.rolling(w, min_periods=max(1, w // 2)).min()
    return (hi - lo) / price.replace(0, np.nan)


# ============================================================
# Donchian channel position over 5d (very near-term breakout posture)
def f06bp_f06_breakout_proximity_donchpos_5d_base_v076_signal(close):
    b = _f06_donch_pos(close, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian channel position over 504d (multi-year band position)
def f06bp_f06_breakout_proximity_donchpos_504d_base_v077_signal(closeadj):
    b = _f06_donch_pos(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian position over 252d, percentile-ranked vs its own 252d history
def f06bp_f06_breakout_proximity_donchposrank_252d_base_v078_signal(closeadj):
    p = _f06_donch_pos(closeadj, 252)
    b = p.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance to 504d high, z-scored vs its own 252d history (de-trended deep proximity)
def f06bp_f06_breakout_proximity_disthi_504d_base_v079_signal(closeadj):
    d = _f06_dist_high(closeadj, 504)
    b = _z(d, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 504d low, percentile-ranked vs its own 252d history (deep proximity)
def f06bp_f06_breakout_proximity_distlo_504d_base_v080_signal(closeadj):
    d = _f06_dist_low(closeadj, 504)
    b = d.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since the 252d high (staleness of the long upper anchor)
def f06bp_f06_breakout_proximity_dsh_252d_base_v081_signal(closeadj):
    b = _f06_days_since_high(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since the 252d low (staleness of the long lower anchor)
def f06bp_f06_breakout_proximity_dsl_252d_base_v082_signal(closeadj):
    b = _f06_days_since_low(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days-since-high decay: exp-weighted recency of the 126d high (sharp near 1 = fresh)
def f06bp_f06_breakout_proximity_dshdecay_126d_base_v083_signal(closeadj):
    dsh = _f06_days_since_high(closeadj, 126)
    b = np.exp(-3.0 * dsh)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d upside breakout magnitude: positive-only headroom over prior 252d high
def f06bp_f06_breakout_proximity_brkup_252d_base_v084_signal(closeadj):
    ph = _f06_prior_high(closeadj, 252)
    b = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d breakdown cushion: signed log-distance from the prior 252d low
def f06bp_f06_breakout_proximity_brkdn_252d_base_v085_signal(closeadj):
    pl = _f06_prior_low(closeadj, 252)
    b = np.log(closeadj.replace(0, np.nan) / pl.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d breakout + volume confirmation (headroom weighted by 126d volume surge)
def f06bp_f06_breakout_proximity_brkvol_126d_base_v086_signal(closeadj, volume):
    ph = _f06_prior_high(closeadj, 126)
    head = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    vsurge = volume / _mean(volume, 126).replace(0, np.nan)
    b = head * vsurge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakdown + volume confirmation (63d): downside break depth weighted by volume
def f06bp_f06_breakout_proximity_brkdnvol_63d_base_v087_signal(closeadj, volume):
    pl = _f06_prior_low(closeadj, 63)
    depth = (closeadj / pl.replace(0, np.nan) - 1.0).clip(upper=0)
    vsurge = volume / _mean(volume, 63).replace(0, np.nan)
    b = depth * vsurge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume confirmed 63d breakout: positive headroom x dollar-volume surge
def f06bp_f06_breakout_proximity_dvbrk_63d_base_v088_signal(closeadj, volume):
    ph = _f06_prior_high(closeadj, 63)
    head = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    dv = closeadj * volume
    dvsurge = dv / _mean(dv, 63).replace(0, np.nan)
    b = head * dvsurge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume expansion at the upper band: volume z conditioned on being near 63d high
def f06bp_f06_breakout_proximity_volathigh_63d_base_v089_signal(closeadj, volume):
    pos = _f06_donch_pos(closeadj, 63)
    near = (pos >= 0.85).astype(float)
    vz = _z(volume, 63)
    b = (near * vz).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d squeeze-then-break: prior band tightness rank gating a 126d channel breakout
def f06bp_f06_breakout_proximity_squeezebrk_126d_base_v090_signal(closeadj):
    bw = _f06_band_width(closeadj, 21)
    tight_rank = 1.0 - bw.rolling(252, min_periods=126).rank(pct=True)
    prior_tight = tight_rank.shift(10)
    pos = _f06_donch_pos(closeadj, 126)
    b = prior_tight * (pos - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze regime distance: 63d band width relative to its own 252d minimum
def f06bp_f06_breakout_proximity_squeezedist_63d_base_v091_signal(closeadj):
    bw = _f06_band_width(closeadj, 63)
    bwmin = bw.rolling(252, min_periods=126).min()
    b = bw / bwmin.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze-break trigger: width expansion this month after a prior compression
def f06bp_f06_breakout_proximity_squeezetrig_base_v092_signal(closeadj):
    bw = _f06_band_width(closeadj, 21)
    prior_low = bw.rolling(126, min_periods=63).min().shift(5)
    expand = bw / prior_low.replace(0, np.nan) - 1.0
    pos = _f06_donch_pos(closeadj, 63) - 0.5
    b = expand * np.sign(pos)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-contraction streak: consecutive days the 21d range is below its 63d mean
def f06bp_f06_breakout_proximity_contractstreak_base_v093_signal(high, low):
    rng = (high - low).rolling(21, min_periods=10).mean()
    ref = (high - low).rolling(63, min_periods=21).mean()
    tight = (rng < ref).astype(float)
    grp = (tight == 0).cumsum()
    b = tight.groupby(grp).cumsum() / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true-range Donchian position over 126d (intraday hi/lo band)
def f06bp_f06_breakout_proximity_hldonch_126d_base_v094_signal(closeadj, high, low):
    hi = _rmax(high, 126)
    lo = _rmin(low, 126)
    b = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance to 126d high in ATR units (clean breakout proximity)
def f06bp_f06_breakout_proximity_disthiatr_126d_base_v095_signal(closeadj, high, low):
    hi = _rmax(closeadj, 126)
    atr = _f06_atr(high, low, 21)
    b = (closeadj - hi) / atr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# approach speed to 126d low in ATR units: change in ATR-distance over a month
def f06bp_f06_breakout_proximity_distloatr_126d_base_v096_signal(closeadj, high, low):
    lo = _rmin(closeadj, 126)
    atr = _f06_atr(high, low, 21)
    ratio = (closeadj - lo) / atr.replace(0, np.nan)
    b = ratio - ratio.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-63d-high frequency over the last half-year (medium-term breakout cadence)
def f06bp_f06_breakout_proximity_newhifreq_63d_base_v097_signal(closeadj):
    ph = _f06_prior_high(closeadj, 63)
    is_break = (closeadj > ph).astype(float)
    freq = is_break.rolling(126, min_periods=63).mean()
    head = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0).rolling(126, min_periods=63).mean()
    b = freq + 8.0 * head
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-63d-low frequency over the last half-year (medium-term breakdown cadence)
def f06bp_f06_breakout_proximity_newlofreq_63d_base_v098_signal(closeadj):
    pl = _f06_prior_low(closeadj, 63)
    is_break = (closeadj < pl).astype(float)
    freq = is_break.rolling(126, min_periods=63).mean()
    depth = (pl / closeadj.replace(0, np.nan) - 1.0).clip(lower=0).rolling(126, min_periods=63).mean()
    b = freq + 8.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net breakout pressure over a half-year using 63d break levels
def f06bp_f06_breakout_proximity_netbreak_126d_base_v099_signal(closeadj):
    ph = _f06_prior_high(closeadj, 63)
    pl = _f06_prior_low(closeadj, 63)
    up = (closeadj > ph).astype(float)
    dn = (closeadj < pl).astype(float)
    b = (up - dn).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian position momentum over a quarter (126d band approach speed)
def f06bp_f06_breakout_proximity_donchmom_126d_base_v100_signal(closeadj):
    p = _f06_donch_pos(closeadj, 126)
    b = p - p.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian position momentum over a week (5d band micro-thrust)
def f06bp_f06_breakout_proximity_donchmom_5d_base_v101_signal(close):
    p = _f06_donch_pos(close, 21)
    b = p - p.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread: 63d Donchian position minus 252d Donchian position (term-structure tilt)
def f06bp_f06_breakout_proximity_donchspr_63v252_base_v102_signal(closeadj):
    s = _f06_donch_pos(closeadj, 63)
    l = _f06_donch_pos(closeadj, 252)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread: 21d distance-to-high minus 126d distance-to-high (proximity term structure)
def f06bp_f06_breakout_proximity_disthispr_21v126_base_v103_signal(close, closeadj):
    s = _f06_dist_high(close, 21)
    l = _f06_dist_high(closeadj, 126)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout headroom (126d) per unit of volatility, ranked vs 252d history
def f06bp_f06_breakout_proximity_brkvoladj_126d_base_v104_signal(closeadj):
    ph = _f06_prior_high(closeadj, 126)
    head = closeadj / ph.replace(0, np.nan) - 1.0
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    ratio = head / vol.replace(0, np.nan)
    b = ratio.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-band hug time over a half-year (126d channel leadership persistence)
def f06bp_f06_breakout_proximity_upperhug_126d_base_v105_signal(closeadj):
    p = _f06_donch_pos(closeadj, 126)
    hug = (p >= 0.9).astype(float)
    b = hug.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-band hug time over a half-year (126d capitulation persistence)
def f06bp_f06_breakout_proximity_lowerhug_126d_base_v106_signal(closeadj):
    p = _f06_donch_pos(closeadj, 126)
    hug = (p <= 0.1).astype(float)
    b = hug.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian band-width trend over a quarter (126d channel expansion/contraction)
def f06bp_f06_breakout_proximity_widthtrend_126d_base_v107_signal(closeadj):
    bw = _f06_band_width(closeadj, 126)
    b = bw / bw.shift(63).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze release (126d): prior 126d compression x current 126d channel position
def f06bp_f06_breakout_proximity_squeezerelease_126d_base_v108_signal(closeadj):
    bw = _f06_band_width(closeadj, 63)
    med = bw.rolling(252, min_periods=126).median()
    compr = (med / bw.replace(0, np.nan)).shift(10)
    pos = _f06_donch_pos(closeadj, 126) - 0.5
    b = compr * pos
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian position smoothed over a quarter (126d persistent posture)
def f06bp_f06_breakout_proximity_donchposema_126d_base_v109_signal(closeadj):
    p = _f06_donch_pos(closeadj, 126)
    b = p.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian position displacement vs slow EMA (126d breakout impulse)
def f06bp_f06_breakout_proximity_donchdisp_126d_base_v110_signal(closeadj):
    p = _f06_donch_pos(closeadj, 126)
    b = p - p.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days-since-high minus days-since-low over 126d (recent-anchor balance)
def f06bp_f06_breakout_proximity_dshvsdsl_126d_base_v111_signal(closeadj):
    dsh = _f06_days_since_high(closeadj, 126)
    dsl = _f06_days_since_low(closeadj, 126)
    b = dsl - dsh
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fresh-high recency weighted by channel position over 252d
def f06bp_f06_breakout_proximity_freshhi_252d_base_v112_signal(closeadj):
    dsh = _f06_days_since_high(closeadj, 252)
    pos = _f06_donch_pos(closeadj, 252)
    b = (1.0 - dsh) * pos
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fresh-low recency weighted by inverse channel position over 252d (capitulation)
def f06bp_f06_breakout_proximity_freshlo_252d_base_v113_signal(closeadj):
    dsl = _f06_days_since_low(closeadj, 252)
    pos = _f06_donch_pos(closeadj, 252)
    b = (1.0 - dsl) * (1.0 - pos)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout magnitude bounded: tanh of 126d headroom (durable breakout strength)
def f06bp_f06_breakout_proximity_brktanh_126d_base_v114_signal(closeadj):
    ph = _f06_prior_high(closeadj, 126)
    head = closeadj / ph.replace(0, np.nan) - 1.0
    b = np.tanh(12.0 * head)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# channel-position curvature across 63/126/252 (long-window term curvature)
def f06bp_f06_breakout_proximity_convex_252d_base_v115_signal(closeadj):
    p_s = _f06_donch_pos(closeadj, 63)
    p_m = _f06_donch_pos(closeadj, 126)
    p_l = _f06_donch_pos(closeadj, 252)
    b = p_m - 0.5 * (p_s + p_l)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-window top-band proximity average across 5/21/63/126 (short-stack agreement)
def f06bp_f06_breakout_proximity_multiagreeshort_base_v116_signal(close, closeadj):
    p1 = _f06_donch_pos(close, 5)
    p2 = _f06_donch_pos(close, 21)
    p3 = _f06_donch_pos(closeadj, 63)
    p4 = _f06_donch_pos(closeadj, 126)
    b = pd.concat([p1, p2, p3, p4], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-window distance-to-high dispersion across 21/63/126/252
def f06bp_f06_breakout_proximity_disthidisp_base_v117_signal(close, closeadj):
    d1 = _f06_dist_high(close, 21)
    d2 = _f06_dist_high(closeadj, 63)
    d3 = _f06_dist_high(closeadj, 126)
    d4 = _f06_dist_high(closeadj, 252)
    b = pd.concat([d1, d2, d3, d4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout-then-hold over a quarter: fraction still above the prior 126d high
def f06bp_f06_breakout_proximity_brkhold_126d_base_v118_signal(closeadj):
    ph = _f06_prior_high(closeadj, 126).shift(63)
    hold = (closeadj >= ph).astype(float)
    b = hold.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# false-breakout / failure over 126d: recent max channel position minus current
def f06bp_f06_breakout_proximity_brkfail_126d_base_v119_signal(closeadj):
    p = _f06_donch_pos(closeadj, 126)
    recent_top = p.rolling(42, min_periods=21).max()
    b = recent_top - p
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-to-high momentum over 252d (yearly breakout approach speed)
def f06bp_f06_breakout_proximity_disthimom_252d_base_v120_signal(closeadj):
    d = _f06_dist_high(closeadj, 252)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance-to-low momentum over 252d (yearly pull-away from base)
def f06bp_f06_breakout_proximity_distlomom_252d_base_v121_signal(closeadj):
    d = _f06_dist_low(closeadj, 252)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout/volume rank divergence over 126d (position rank minus volume-trend rank)
def f06bp_f06_breakout_proximity_volconfpos_126d_base_v122_signal(closeadj, volume):
    pos = _f06_donch_pos(closeadj, 126)
    vtrend = _mean(volume, 63) / _mean(volume, 126).replace(0, np.nan)
    pos_r = pos.rolling(126, min_periods=63).rank(pct=True)
    vol_r = vtrend.rolling(126, min_periods=63).rank(pct=True)
    b = pos_r - vol_r
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian midline distance in ATR units over 126d (long midpoint distance)
def f06bp_f06_breakout_proximity_middist_126d_base_v123_signal(closeadj, high, low):
    hi = _rmax(closeadj, 126)
    lo = _rmin(closeadj, 126)
    mid = (hi + lo) / 2.0
    atr = _f06_atr(high, low, 21)
    b = (closeadj - mid) / atr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# channel-width-normalized headroom to the 252d high (how many widths to a breakout)
def f06bp_f06_breakout_proximity_headwidth_252d_base_v124_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    b = (hi - closeadj) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-band push streak over 126d channel: consecutive top-quartile days
def f06bp_f06_breakout_proximity_pushstreak_126d_base_v125_signal(closeadj):
    p = _f06_donch_pos(closeadj, 126)
    up = (p >= 0.75).astype(float)
    grp = (up == 0).cumsum()
    b = up.groupby(grp).cumsum() / 42.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-band slide streak over 63d channel: consecutive bottom-quartile days
def f06bp_f06_breakout_proximity_slidestreak_63d_base_v126_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    dn = (p <= 0.25).astype(float)
    grp = (dn == 0).cumsum()
    b = dn.groupby(grp).cumsum() / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze depth over 126d band width vs its own 252d max (deep compression)
def f06bp_f06_breakout_proximity_squeezedepth_126d_base_v127_signal(closeadj):
    bw = _f06_band_width(closeadj, 126)
    bwmax = bw.rolling(504, min_periods=252).max()
    b = bw / bwmax.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up/down volume balance near the 63d high (accumulation into breakouts)
def f06bp_f06_breakout_proximity_brkupvol_63d_base_v128_signal(closeadj, volume):
    pos = _f06_donch_pos(closeadj, 63)
    up = closeadj > closeadj.shift(1)
    upvol = volume.where(up, 0.0).rolling(63, min_periods=21).sum()
    dnvol = volume.where(~up, 0.0).rolling(63, min_periods=21).sum()
    ratio = upvol / (upvol + dnvol).replace(0, np.nan)
    b = pos * (ratio - 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout thrust over 126d: time at new highs x trailing quarter return
def f06bp_f06_breakout_proximity_thrust_126d_base_v129_signal(closeadj):
    ph = _f06_prior_high(closeadj, 126)
    at_high = (closeadj >= ph).astype(float)
    ret63 = closeadj / closeadj.shift(63).replace(0, np.nan) - 1.0
    b = at_high.rolling(63, min_periods=21).mean() * ret63
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# low-vol breakout setup: 63d breakout headroom gated by a vol-compression regime
def f06bp_f06_breakout_proximity_comprpos_126d_base_v130_signal(closeadj):
    vol = closeadj.pct_change().rolling(21, min_periods=10).std()
    vol_rank = vol.rolling(252, min_periods=126).rank(pct=True)
    calm = (1.0 - vol_rank)
    ph = _f06_prior_high(closeadj, 63)
    head = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    b = calm * head
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout headroom year-over-year change (252d prior-high break vs one year ago)
def f06bp_f06_breakout_proximity_brkupyoy_252d_base_v131_signal(closeadj):
    ph = _f06_prior_high(closeadj, 252)
    head = closeadj / ph.replace(0, np.nan) - 1.0
    b = head - head.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest 126d-high breakout extension seen in the trailing quarter (peak thrust)
def f06bp_f06_breakout_proximity_brkmagsum_126d_base_v132_signal(closeadj):
    ph = _f06_prior_high(closeadj, 126)
    head = (closeadj / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    b = head.rolling(63, min_periods=21).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# channel-position skew over a half-year (126d average asymmetry of price location)
def f06bp_f06_breakout_proximity_posskew_126d_base_v133_signal(closeadj):
    p = _f06_donch_pos(closeadj, 126)
    b = (p - 0.5).rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday breakout premium over 126d: 126d intraday high above 126d close high
def f06bp_f06_breakout_proximity_truepremium_126d_base_v134_signal(closeadj, high):
    hi_true = _rmax(high, 126)
    hi_close = _rmax(closeadj, 126)
    b = hi_true / hi_close.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian channel-position entropy proxy: dispersion of position over the last quarter
def f06bp_f06_breakout_proximity_posdispersion_63d_base_v135_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    b = p.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout cleanliness: 63d range traveled per net displacement (efficient breakout)
def f06bp_f06_breakout_proximity_clean_63d_base_v136_signal(closeadj):
    disp = (closeadj - closeadj.shift(63)).abs()
    path = closeadj.diff().abs().rolling(63, min_periods=21).sum()
    eff = disp / path.replace(0, np.nan)
    pos = _f06_donch_pos(closeadj, 63) - 0.5
    b = eff * np.sign(pos)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze-then-break interaction: 21d compression rank x 21d breakout headroom
def f06bp_f06_breakout_proximity_squeezehead_21d_base_v137_signal(close):
    bw = _f06_band_width(close, 21)
    tight = (1.0 - bw.rolling(126, min_periods=63).rank(pct=True)).shift(5)
    ph = _f06_prior_high(close, 21)
    head = (close / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    b = tight * head
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 252d midpoint-distance momentum: change in position-vs-midpoint over a quarter
def f06bp_f06_breakout_proximity_midrank_252d_base_v138_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    mid = (hi + lo) / 2.0
    rel = (closeadj - mid) / (hi - lo).replace(0, np.nan)
    b = rel - rel.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-band acceleration: change in time-at-top of the 63d channel over a month
def f06bp_f06_breakout_proximity_topaccel_63d_base_v139_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    top = (p >= 0.8).astype(float).rolling(21, min_periods=10).mean()
    b = top - top.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-confirmed breakdown near the 63d low (distribution into breakdowns)
def f06bp_f06_breakout_proximity_distrlo_63d_base_v140_signal(closeadj, volume):
    pos = _f06_donch_pos(closeadj, 63)
    near_low = (pos <= 0.15).astype(float)
    vz = _z(volume, 63)
    b = (near_low * vz).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position acceleration over 252d (yearly band position 2nd difference proxy)
def f06bp_f06_breakout_proximity_posaccel_252d_base_v141_signal(closeadj):
    p = _f06_donch_pos(closeadj, 252)
    b = (p - p.shift(63)) - (p.shift(63) - p.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5d-vs-63d distance-to-high spread (immediate vs medium breakout proximity)
def f06bp_f06_breakout_proximity_disthispr_5v63_base_v142_signal(close, closeadj):
    s = _f06_dist_high(close, 5)
    l = _f06_dist_high(closeadj, 63)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout volume confirmation over 21d, ranked vs 126d history (relative thrust)
def f06bp_f06_breakout_proximity_brkvolrank_21d_base_v143_signal(close, volume):
    ph = _f06_prior_high(close, 21)
    head = (close / ph.replace(0, np.nan) - 1.0).clip(lower=0)
    vsurge = volume / _mean(volume, 21).replace(0, np.nan)
    raw = head * vsurge
    b = raw.rolling(126, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity-weighted volume: dollar-volume share occurring in the top band (63d)
def f06bp_f06_breakout_proximity_topdvshare_63d_base_v144_signal(closeadj, volume):
    pos = _f06_donch_pos(closeadj, 63)
    dv = closeadj * volume
    top_dv = dv.where(pos >= 0.75, 0.0).rolling(63, min_periods=21).sum()
    all_dv = dv.rolling(63, min_periods=21).sum()
    b = top_dv / all_dv.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout-failure rate over 126d: count of new-high days that closed lower next 5d
def f06bp_f06_breakout_proximity_failrate_126d_base_v145_signal(closeadj):
    ph = _f06_prior_high(closeadj, 21)
    is_high = (closeadj > ph)
    fade = (closeadj.shift(-5) < closeadj) & is_high
    fail = fade.astype(float)
    raw = fail.rolling(126, min_periods=63).sum()
    base = is_high.astype(float).rolling(126, min_periods=63).sum()
    b = raw / base.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Donchian position relative to its 252d median (long-run band centering)
def f06bp_f06_breakout_proximity_poscentered_252d_base_v146_signal(closeadj):
    p = _f06_donch_pos(closeadj, 63)
    med = p.rolling(252, min_periods=126).median()
    b = p - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze count: number of squeeze episodes (entries below band-width median) over 252d
def f06bp_f06_breakout_proximity_squeezecount_base_v147_signal(closeadj):
    bw = _f06_band_width(closeadj, 21)
    med = bw.rolling(126, min_periods=63).median()
    tight = (bw < med).astype(float)
    entries = ((tight == 1) & (tight.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + 5.0 * (med - bw).clip(lower=0).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout posture composite: 126d channel position x days-since-high recency
def f06bp_f06_breakout_proximity_posture_126d_base_v148_signal(closeadj):
    pos = _f06_donch_pos(closeadj, 126)
    dsh = _f06_days_since_high(closeadj, 126)
    b = pos * np.exp(-2.0 * dsh)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakdown posture composite: 126d inverse channel position x days-since-low recency
def f06bp_f06_breakout_proximity_postlow_126d_base_v149_signal(closeadj):
    pos = _f06_donch_pos(closeadj, 126)
    dsl = _f06_days_since_low(closeadj, 126)
    b = (1.0 - pos) * np.exp(-2.0 * dsl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year breakout approach speed: change in 504d ATR-distance-to-high over a quarter
def f06bp_f06_breakout_proximity_truedisthiatr_504d_base_v150_signal(closeadj, high, low):
    hi = _rmax(high, 504)
    atr = _f06_atr(high, low, 63)
    ratio = (closeadj - hi) / atr.replace(0, np.nan)
    b = ratio - ratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06bp_f06_breakout_proximity_donchpos_5d_base_v076_signal,
    f06bp_f06_breakout_proximity_donchpos_504d_base_v077_signal,
    f06bp_f06_breakout_proximity_donchposrank_252d_base_v078_signal,
    f06bp_f06_breakout_proximity_disthi_504d_base_v079_signal,
    f06bp_f06_breakout_proximity_distlo_504d_base_v080_signal,
    f06bp_f06_breakout_proximity_dsh_252d_base_v081_signal,
    f06bp_f06_breakout_proximity_dsl_252d_base_v082_signal,
    f06bp_f06_breakout_proximity_dshdecay_126d_base_v083_signal,
    f06bp_f06_breakout_proximity_brkup_252d_base_v084_signal,
    f06bp_f06_breakout_proximity_brkdn_252d_base_v085_signal,
    f06bp_f06_breakout_proximity_brkvol_126d_base_v086_signal,
    f06bp_f06_breakout_proximity_brkdnvol_63d_base_v087_signal,
    f06bp_f06_breakout_proximity_dvbrk_63d_base_v088_signal,
    f06bp_f06_breakout_proximity_volathigh_63d_base_v089_signal,
    f06bp_f06_breakout_proximity_squeezebrk_126d_base_v090_signal,
    f06bp_f06_breakout_proximity_squeezedist_63d_base_v091_signal,
    f06bp_f06_breakout_proximity_squeezetrig_base_v092_signal,
    f06bp_f06_breakout_proximity_contractstreak_base_v093_signal,
    f06bp_f06_breakout_proximity_hldonch_126d_base_v094_signal,
    f06bp_f06_breakout_proximity_disthiatr_126d_base_v095_signal,
    f06bp_f06_breakout_proximity_distloatr_126d_base_v096_signal,
    f06bp_f06_breakout_proximity_newhifreq_63d_base_v097_signal,
    f06bp_f06_breakout_proximity_newlofreq_63d_base_v098_signal,
    f06bp_f06_breakout_proximity_netbreak_126d_base_v099_signal,
    f06bp_f06_breakout_proximity_donchmom_126d_base_v100_signal,
    f06bp_f06_breakout_proximity_donchmom_5d_base_v101_signal,
    f06bp_f06_breakout_proximity_donchspr_63v252_base_v102_signal,
    f06bp_f06_breakout_proximity_disthispr_21v126_base_v103_signal,
    f06bp_f06_breakout_proximity_brkvoladj_126d_base_v104_signal,
    f06bp_f06_breakout_proximity_upperhug_126d_base_v105_signal,
    f06bp_f06_breakout_proximity_lowerhug_126d_base_v106_signal,
    f06bp_f06_breakout_proximity_widthtrend_126d_base_v107_signal,
    f06bp_f06_breakout_proximity_squeezerelease_126d_base_v108_signal,
    f06bp_f06_breakout_proximity_donchposema_126d_base_v109_signal,
    f06bp_f06_breakout_proximity_donchdisp_126d_base_v110_signal,
    f06bp_f06_breakout_proximity_dshvsdsl_126d_base_v111_signal,
    f06bp_f06_breakout_proximity_freshhi_252d_base_v112_signal,
    f06bp_f06_breakout_proximity_freshlo_252d_base_v113_signal,
    f06bp_f06_breakout_proximity_brktanh_126d_base_v114_signal,
    f06bp_f06_breakout_proximity_convex_252d_base_v115_signal,
    f06bp_f06_breakout_proximity_multiagreeshort_base_v116_signal,
    f06bp_f06_breakout_proximity_disthidisp_base_v117_signal,
    f06bp_f06_breakout_proximity_brkhold_126d_base_v118_signal,
    f06bp_f06_breakout_proximity_brkfail_126d_base_v119_signal,
    f06bp_f06_breakout_proximity_disthimom_252d_base_v120_signal,
    f06bp_f06_breakout_proximity_distlomom_252d_base_v121_signal,
    f06bp_f06_breakout_proximity_volconfpos_126d_base_v122_signal,
    f06bp_f06_breakout_proximity_middist_126d_base_v123_signal,
    f06bp_f06_breakout_proximity_headwidth_252d_base_v124_signal,
    f06bp_f06_breakout_proximity_pushstreak_126d_base_v125_signal,
    f06bp_f06_breakout_proximity_slidestreak_63d_base_v126_signal,
    f06bp_f06_breakout_proximity_squeezedepth_126d_base_v127_signal,
    f06bp_f06_breakout_proximity_brkupvol_63d_base_v128_signal,
    f06bp_f06_breakout_proximity_thrust_126d_base_v129_signal,
    f06bp_f06_breakout_proximity_comprpos_126d_base_v130_signal,
    f06bp_f06_breakout_proximity_brkupyoy_252d_base_v131_signal,
    f06bp_f06_breakout_proximity_brkmagsum_126d_base_v132_signal,
    f06bp_f06_breakout_proximity_posskew_126d_base_v133_signal,
    f06bp_f06_breakout_proximity_truepremium_126d_base_v134_signal,
    f06bp_f06_breakout_proximity_posdispersion_63d_base_v135_signal,
    f06bp_f06_breakout_proximity_clean_63d_base_v136_signal,
    f06bp_f06_breakout_proximity_squeezehead_21d_base_v137_signal,
    f06bp_f06_breakout_proximity_midrank_252d_base_v138_signal,
    f06bp_f06_breakout_proximity_topaccel_63d_base_v139_signal,
    f06bp_f06_breakout_proximity_distrlo_63d_base_v140_signal,
    f06bp_f06_breakout_proximity_posaccel_252d_base_v141_signal,
    f06bp_f06_breakout_proximity_disthispr_5v63_base_v142_signal,
    f06bp_f06_breakout_proximity_brkvolrank_21d_base_v143_signal,
    f06bp_f06_breakout_proximity_topdvshare_63d_base_v144_signal,
    f06bp_f06_breakout_proximity_failrate_126d_base_v145_signal,
    f06bp_f06_breakout_proximity_poscentered_252d_base_v146_signal,
    f06bp_f06_breakout_proximity_squeezecount_base_v147_signal,
    f06bp_f06_breakout_proximity_posture_126d_base_v148_signal,
    f06bp_f06_breakout_proximity_postlow_126d_base_v149_signal,
    f06bp_f06_breakout_proximity_truedisthiatr_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_BREAKOUT_PROXIMITY_REGISTRY_076_150 = REGISTRY


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
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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

    print("OK f06_breakout_proximity_base_076_150_claude: %d features pass" % n_features)
