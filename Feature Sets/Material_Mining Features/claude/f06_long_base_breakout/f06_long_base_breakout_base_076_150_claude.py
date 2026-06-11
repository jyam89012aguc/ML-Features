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
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


# ===== folder domain primitives (long-base / breakout) =====
def _f06_base_range(close, w):
    hi = _rmax(close, w)
    lo = _rmin(close, w)
    mid = (hi + lo) / 2.0
    return (hi - lo) / mid.replace(0, np.nan)


def _f06_tightness(close, w):
    return _std(close, w) / _mean(close, w).replace(0, np.nan)


def _f06_ceiling_dist(close, w):
    ceil = close.shift(1).rolling(w, min_periods=max(1, w // 2)).max()
    return close / ceil.replace(0, np.nan) - 1.0


def _f06_floor_dist(close, w):
    floor = close.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    return close / floor.replace(0, np.nan) - 1.0


def _f06_breakout(close, w):
    ceil = close.shift(1).rolling(w, min_periods=max(1, w // 2)).max()
    return (close / ceil.replace(0, np.nan) - 1.0).clip(lower=0.0)


def _f06_basepos(close, w):
    hi = _rmax(close, w)
    lo = _rmin(close, w)
    return (close - lo) / (hi - lo).replace(0, np.nan)


# ============================================================
# dollar-volume base dry-up: 21d vs 252d dollar-volume (accumulation base => low)
def f06lb_f06_long_base_breakout_dvoldry_252d_base_v076_signal(closeadj, volume):
    dv = closeadj * volume
    b = _mean(dv, 21) / _mean(dv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume surge on the breakout day vs 252d base average
def f06lb_f06_long_base_breakout_dvolsurge_252d_base_v077_signal(closeadj, volume):
    dv = closeadj * volume
    b = dv / _mean(dv, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout magnitude scaled by dollar-volume z (heavy-money confirmed thrust)
def f06lb_f06_long_base_breakout_brkmoney_252d_base_v078_signal(closeadj, volume):
    bo = _f06_breakout(closeadj, 252)
    dv = closeadj * volume
    dz = _z(dv, 126)
    b = bo * (1.0 + dz.clip(lower=-1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson-style base range using intraday high/low over 252d, price-normalized
def f06lb_f06_long_base_breakout_pkrange_252d_base_v079_signal(high, low, closeadj):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    pk = np.sqrt((hl ** 2).rolling(252, min_periods=126).mean() / (4.0 * np.log(2.0)))
    b = pk
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-range base tightness vs its own 1260d history (rank: tight vs usual)
def f06lb_f06_long_base_breakout_hlbasetight_504d_base_v080_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    avg = rng.rolling(504, min_periods=252).mean()
    b = _rank(avg, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout above intraday-high 504d lid, normalized by ATR (true two-year breakout)
def f06lb_f06_long_base_breakout_truebrkatr_504d_base_v081_signal(high, low, closeadj):
    ceil = high.shift(1).rolling(504, min_periods=252).max()
    atr = (high - low).rolling(21, min_periods=5).mean()
    b = ((closeadj - ceil) / atr.replace(0, np.nan)).clip(lower=0.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base channel slope: linear-ish drift of the 504d midpoint normalized by price
def f06lb_f06_long_base_breakout_channelslope_504d_base_v082_signal(closeadj):
    hi = _rmax(closeadj, 504)
    lo = _rmin(closeadj, 504)
    mid = (hi + lo) / 2.0
    b = (mid - mid.shift(126)) / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base width stability: how steady the 252d range has been (std of base range)
def f06lb_f06_long_base_breakout_widthstab_252d_base_v083_signal(closeadj):
    br = _f06_base_range(closeadj, 252)
    b = br.rolling(126, min_periods=63).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout quality: breakout magnitude times days-since-base-floor (long base then pop)
def f06lb_f06_long_base_breakout_qualbrk_504d_base_v084_signal(closeadj):
    bo = _f06_breakout(closeadj, 504)

    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    floorstale = closeadj.rolling(504, min_periods=252).apply(_f, raw=True)
    b = bo * floorstale
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from base ceiling in volatility units (how many vols below the lid)
def f06lb_f06_long_base_breakout_ceilvol_252d_base_v085_signal(closeadj):
    cd = _f06_ceiling_dist(closeadj, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = cd / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# floor support in volatility units (how many vols above the base floor)
def f06lb_f06_long_base_breakout_floorvol_252d_base_v086_signal(closeadj):
    fd = _f06_floor_dist(closeadj, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = fd / vol.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base contraction acceleration: change in 252/504 range ratio over a quarter
def f06lb_f06_long_base_breakout_contractacc_base_v087_signal(closeadj):
    s = _f06_base_range(closeadj, 252)
    l = _f06_base_range(closeadj, 504)
    ratio = s / l.replace(0, np.nan)
    b = ratio - ratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tight-base streak length normalized: consecutive days CoV below its 252d median
def f06lb_f06_long_base_breakout_tightstreak_252d_base_v088_signal(closeadj):
    t = _f06_tightness(closeadj, 252)
    med = t.rolling(252, min_periods=126).median()
    tight = (t < med).astype(float)

    def _streak(a):
        c = 0
        for v in a[::-1]:
            if v >= 0.5:
                c += 1
            else:
                break
        return c
    b = tight.rolling(126, min_periods=42).apply(_streak, raw=True) / 126.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout volume thrust: up-volume share on the breakout-pressing days
def f06lb_f06_long_base_breakout_upvolthrust_252d_base_v089_signal(closeadj, volume):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    prox = (closeadj / ceil.replace(0, np.nan)).clip(lower=0.0, upper=1.05)
    up = (closeadj > closeadj.shift(1)).astype(float)
    b = (prox * up * volume).rolling(21, min_periods=10).sum() / volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year base depth: log range from 1260d low to 1260d high (base amplitude)
def f06lb_f06_long_base_breakout_baseamp_1260d_base_v090_signal(closeadj):
    hi = _rmax(closeadj, 1260)
    lo = _rmin(closeadj, 1260)
    b = np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of last 2y spent in the upper quartile of the 504d base (lid-hugging)
def f06lb_f06_long_base_breakout_upperhug_504d_base_v091_signal(closeadj):
    pos = _f06_basepos(closeadj, 504)
    upper = (pos >= 0.75).astype(float)
    b = upper.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of last 2y spent in the lower quartile of the 504d base (floor-hugging)
def f06lb_f06_long_base_breakout_lowerhug_504d_base_v092_signal(closeadj):
    pos = _f06_basepos(closeadj, 504)
    lower = (pos <= 0.25).astype(float)
    b = lower.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout cleanliness in ATR: breakout magnitude vs ATR-measured base width
def f06lb_f06_long_base_breakout_cleanatr_252d_base_v093_signal(high, low, closeadj):
    bo = _f06_breakout(closeadj, 252)
    atr = (high - low).rolling(21, min_periods=5).mean() / closeadj.replace(0, np.nan)
    b = bo / atr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# false-breakout severity: max overshoot above 252d lid that then failed, over 63d
def f06lb_f06_long_base_breakout_failsev_252d_base_v094_signal(high, closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    overshoot = (high / ceil.replace(0, np.nan) - 1.0).clip(lower=0.0)
    failed = overshoot * (closeadj <= ceil).astype(float)
    b = failed.rolling(63, min_periods=21).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base position momentum: change in 252d position over a quarter (climbing the base)
def f06lb_f06_long_base_breakout_posmom_252d_base_v095_signal(closeadj):
    pos = _f06_basepos(closeadj, 252)
    b = pos - pos.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range compression vs realized vol: base range shrinking while vol low (quiet coil)
def f06lb_f06_long_base_breakout_quietcoil_252d_base_v096_signal(closeadj):
    br = _f06_base_range(closeadj, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    b = br * vol
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance traveled vs straight-line gain over 504d (path efficiency in base)
def f06lb_f06_long_base_breakout_pathineff_504d_base_v097_signal(closeadj):
    net = (closeadj / closeadj.shift(504) - 1.0).abs()
    path = closeadj.pct_change().abs().rolling(504, min_periods=252).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout above 252d lid weighted by tightness of the prior base (coiled-spring pop)
def f06lb_f06_long_base_breakout_coilpop_252d_base_v098_signal(closeadj):
    bo = _f06_breakout(closeadj, 252)
    br = _f06_base_range(closeadj, 252).shift(21)
    b = bo / br.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-test resistance: number of distinct touches of the 504d lid over last year
def f06lb_f06_long_base_breakout_touches_504d_base_v099_signal(closeadj):
    ceil = closeadj.shift(1).rolling(504, min_periods=252).max()
    near = (closeadj / ceil.replace(0, np.nan) >= 0.95).astype(float)
    entries = ((near == 1) & (near.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + closeadj / ceil.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base floor durability: cushion above the rolling 63d low minus depth of any
# undercuts of the 252d base floor (high => support holding firmly, low => cracking)
def f06lb_f06_long_base_breakout_floordur_252d_base_v100_signal(closeadj):
    floor = closeadj.shift(1).rolling(252, min_periods=126).min()
    undercut = (floor / closeadj.replace(0, np.nan) - 1.0).clip(lower=0.0)
    cushion = closeadj / _rmin(closeadj, 63).replace(0, np.nan) - 1.0
    b = cushion - 5.0 * undercut.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volatility-of-range: how stable the daily range is within the base (steady base)
def f06lb_f06_long_base_breakout_rangevov_252d_base_v101_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    b = _std(rng, 252) / _mean(rng, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout day gap: how far close pushed above prior-day close on lid-pressing days
def f06lb_f06_long_base_breakout_gapthrust_252d_base_v102_signal(closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    near = (closeadj / ceil.replace(0, np.nan) >= 0.95).astype(float)
    r1 = (closeadj / closeadj.shift(1) - 1.0)
    b = (near * r1).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base midpoint convergence: ceiling and floor both flattening (apex forming)
def f06lb_f06_long_base_breakout_apex_252d_base_v103_signal(closeadj):
    ceil = _rmax(closeadj, 252)
    floor = _rmin(closeadj, 252)
    cs = (ceil - ceil.shift(63)).abs() / closeadj.replace(0, np.nan)
    fs = (floor - floor.shift(63)).abs() / closeadj.replace(0, np.nan)
    b = -(cs + fs)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout sustainability: fraction of last 21d the close stayed above the 252d lid
def f06lb_f06_long_base_breakout_holdfrac_252d_base_v104_signal(closeadj):
    ceil = closeadj.shift(22).rolling(252, min_periods=126).max()
    above = (closeadj > ceil).astype(float)
    b = above.rolling(21, min_periods=10).mean() + 0.001 * _f06_ceiling_dist(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-volume trend slope through the base (rising liquidity into breakout)
def f06lb_f06_long_base_breakout_dvoltrend_252d_base_v105_signal(closeadj, volume):
    dv = closeadj * volume
    b = np.log(_mean(dv, 63).replace(0, np.nan) / _mean(dv, 252).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base low retest depth: how far the last 63d low sits below the 252d base midpoint
def f06lb_f06_long_base_breakout_retest_252d_base_v106_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    mid = (hi + lo) / 2.0
    recent_lo = _rmin(closeadj, 63)
    b = (recent_lo - mid) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base high tag freshness: how recently the 252d high vs the 504d high were set
def f06lb_f06_long_base_breakout_hifresh_base_v107_signal(closeadj):
    hi252 = _rmax(closeadj, 252)
    hi504 = _rmax(closeadj, 504)
    b = (hi252 / hi504.replace(0, np.nan) - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout strength rank vs own history (relative breakout magnitude)
def f06lb_f06_long_base_breakout_brkrank_252d_base_v108_signal(closeadj):
    bo = _f06_breakout(closeadj, 252)
    cd = _f06_ceiling_dist(closeadj, 252)
    raw = bo + cd
    b = _rank(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coil-then-expand: was tight then range expanded (squeeze-release detector)
def f06lb_f06_long_base_breakout_squeezerel_252d_base_v109_signal(closeadj):
    br5 = _f06_base_range(closeadj, 21)
    br_long = _f06_base_range(closeadj, 252).shift(21)
    b = br5 / br_long.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base accumulation: mean money-flow position over 126d (smart money in the base)
def f06lb_f06_long_base_breakout_baseacc_126d_base_v110_signal(high, low, close, closeadj, volume):
    mfm = ((close - low) - (high - close)) / (high - low).replace(0, np.nan)
    mfv = mfm * volume
    b = mfv.rolling(126, min_periods=63).sum() / volume.rolling(126, min_periods=63).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout failure rate over 2y: share of lid pokes that closed back inside
def f06lb_f06_long_base_breakout_failrate_504d_base_v111_signal(high, closeadj):
    ceil = closeadj.shift(1).rolling(504, min_periods=252).max()
    poke = (high > ceil).astype(float)
    held = ((high > ceil) & (closeadj > ceil)).astype(float)
    pk = poke.rolling(252, min_periods=126).sum()
    hd = held.rolling(252, min_periods=126).sum()
    b = (pk - hd) / pk.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base tightness asymmetry: upper-half vs lower-half dispersion within the base
def f06lb_f06_long_base_breakout_tightasym_252d_base_v112_signal(closeadj):
    mid = _mean(closeadj, 252)
    up = (closeadj - mid).clip(lower=0)
    dn = (mid - closeadj).clip(lower=0)
    b = (up.rolling(252, min_periods=126).mean() - dn.rolling(252, min_periods=126).mean()) / mid.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 1260d base floor in ATR units (multi-year lift off the bottom)
def f06lb_f06_long_base_breakout_deepliftatr_1260d_base_v113_signal(high, low, closeadj):
    floor = closeadj.shift(1).rolling(1260, min_periods=504).min()
    atr = (high - low).rolling(63, min_periods=21).mean()
    b = (closeadj - floor) / atr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout momentum quality: 21d return only when above the 252d lid, smoothed
def f06lb_f06_long_base_breakout_brkmomq_252d_base_v114_signal(closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    prox = (closeadj / ceil.replace(0, np.nan)).clip(upper=1.1)
    r21 = closeadj / closeadj.shift(21) - 1.0
    b = (prox * r21).ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how long the base has been forming via low-range persistence over 1260d (rank)
def f06lb_f06_long_base_breakout_baseformrank_1260d_base_v115_signal(closeadj):
    br = _f06_base_range(closeadj, 252)
    persist = (br <= br.rolling(1260, min_periods=504).median()).astype(float)
    raw = persist.rolling(504, min_periods=252).mean()
    b = _rank(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-confirmed base position: position times normalized volume (lift on volume)
def f06lb_f06_long_base_breakout_volpos_252d_base_v116_signal(closeadj, volume):
    pos = _f06_basepos(closeadj, 252)
    vn = volume / _mean(volume, 252).replace(0, np.nan)
    b = pos * vn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base ceiling slope minus price slope (is price catching up to a flat lid?)
def f06lb_f06_long_base_breakout_lidcatch_252d_base_v117_signal(closeadj):
    ceil = _rmax(closeadj, 252)
    cs = np.log(ceil.replace(0, np.nan) / ceil.shift(63).replace(0, np.nan))
    ps = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    b = ps - cs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout extension exhaustion: distance above lid relative to recent max distance
def f06lb_f06_long_base_breakout_extexh_252d_base_v118_signal(closeadj):
    cd = _f06_ceiling_dist(closeadj, 252).clip(lower=0.0)
    maxcd = cd.rolling(63, min_periods=21).max()
    b = cd / maxcd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base depth recovery: where price sits between the 1260d low and the 252d high
def f06lb_f06_long_base_breakout_deeprecov_base_v119_signal(closeadj):
    lo = _rmin(closeadj, 1260)
    hi = _rmax(closeadj, 252)
    b = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout with liquidity expansion: breakout x dollar-volume trend slope
def f06lb_f06_long_base_breakout_brkliq_252d_base_v120_signal(closeadj, volume):
    bo = _f06_breakout(closeadj, 252)
    dv = closeadj * volume
    trend = np.log(_mean(dv, 21).replace(0, np.nan) / _mean(dv, 126).replace(0, np.nan))
    b = bo * trend
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base age via consecutive sub-median tightness over 504d, normalized
def f06lb_f06_long_base_breakout_basematdur_504d_base_v121_signal(closeadj):
    t = _f06_tightness(closeadj, 504)
    med = t.rolling(504, min_periods=252).median()
    tight = (t < med).astype(float)

    def _streak(a):
        c = 0
        for v in a[::-1]:
            if v >= 0.5:
                c += 1
            else:
                break
        return c
    b = tight.rolling(252, min_periods=126).apply(_streak, raw=True) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pre-breakout pinch: 21d range as fraction of 252d range (NR-period inside base)
def f06lb_f06_long_base_breakout_pinch_252d_base_v122_signal(closeadj):
    r21 = (_rmax(closeadj, 21) - _rmin(closeadj, 21))
    r252 = (_rmax(closeadj, 252) - _rmin(closeadj, 252))
    b = r21 / r252.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout direction bias: net sign of last 21 closes above vs below 252d midpoint
def f06lb_f06_long_base_breakout_midbias_252d_base_v123_signal(closeadj):
    mid = (_rmax(closeadj, 252) + _rmin(closeadj, 252)) / 2.0
    sign = np.sign(closeadj - mid)
    b = sign.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from base ceiling smoothed (persistent pressing of the lid)
def f06lb_f06_long_base_breakout_ceilsmooth_252d_base_v124_signal(closeadj):
    cd = _f06_ceiling_dist(closeadj, 252)
    b = cd.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout participation: up-day count in last 21d when above 252d lid
def f06lb_f06_long_base_breakout_partic_252d_base_v125_signal(closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    prox = (closeadj / ceil.replace(0, np.nan)).clip(upper=1.1)
    up = (closeadj > closeadj.shift(1)).astype(float)
    b = (prox * up).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year base skew momentum: change over a quarter in price skew within the
# 1260d base (price migrating from the lower half toward the upper half of the base)
def f06lb_f06_long_base_breakout_symmetry_1260d_base_v126_signal(closeadj):
    hi = _rmax(closeadj, 1260)
    lo = _rmin(closeadj, 1260)
    mid = (hi + lo) / 2.0
    skew = (closeadj - mid) / (hi - lo).replace(0, np.nan)
    b = skew - skew.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tightening velocity: rate of decline in 252d bandwidth (coiling speed)
def f06lb_f06_long_base_breakout_coilspeed_252d_base_v127_signal(closeadj):
    m = _mean(closeadj, 252)
    sd = _std(closeadj, 252)
    bw = (4.0 * sd) / m.replace(0, np.nan)
    b = (bw.shift(21) - bw)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout vs prior failed-breakout: net of magnitude minus recent fail severity
def f06lb_f06_long_base_breakout_netquality_252d_base_v128_signal(high, closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    good = (closeadj / ceil.replace(0, np.nan) - 1.0).clip(lower=0.0)
    overshoot = (high / ceil.replace(0, np.nan) - 1.0).clip(lower=0.0)
    bad = (overshoot * (closeadj <= ceil).astype(float)).rolling(63, min_periods=21).mean()
    b = good - 3.0 * bad
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base trend efficiency: net 252d gain divided by 252d path length (drift vs chop)
def f06lb_f06_long_base_breakout_drifteff_252d_base_v129_signal(closeadj):
    net = (closeadj / closeadj.shift(252) - 1.0)
    path = closeadj.pct_change().abs().rolling(252, min_periods=126).sum()
    b = net / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance below the 504d base ceiling rank-normalized (relative headroom)
def f06lb_f06_long_base_breakout_headroomrank_504d_base_v130_signal(closeadj):
    cd = _f06_ceiling_dist(closeadj, 504)
    b = _rank(cd, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout thrust over base height: 21d gain divided by 252d base amplitude
def f06lb_f06_long_base_breakout_thrustamp_252d_base_v131_signal(closeadj):
    r21 = (closeadj / closeadj.shift(21) - 1.0)
    amp = (_rmax(closeadj, 252) - _rmin(closeadj, 252)) / closeadj.replace(0, np.nan)
    b = r21 / amp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation streak: consecutive days OBV-proxy rising during base, normalized
def f06lb_f06_long_base_breakout_accstreak_base_v132_signal(closeadj, volume):
    signed = np.sign(closeadj.diff()) * volume
    flow = signed.rolling(21, min_periods=10).sum()
    rising = (flow > flow.shift(1)).astype(float)

    def _streak(a):
        c = 0
        for v in a[::-1]:
            if v >= 0.5:
                c += 1
            else:
                break
        return c
    streak = rising.rolling(63, min_periods=21).apply(_streak, raw=True) / 63.0
    flow_norm = flow / _mean(volume, 63).replace(0, np.nan) / 21.0
    b = streak + flow_norm
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year ceiling proximity smoothed (long approach toward the lid)
def f06lb_f06_long_base_breakout_longprox_1260d_base_v133_signal(closeadj):
    ceil = _rmax(closeadj, 1260)
    prox = closeadj / ceil.replace(0, np.nan)
    b = prox.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout confirmation by range expansion: today's range vs 63d avg on pop days
def f06lb_f06_long_base_breakout_rangepop_252d_base_v134_signal(high, low, closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    prox = (closeadj / ceil.replace(0, np.nan)).clip(lower=0.0, upper=1.1)
    rng = (high - low) / closeadj.replace(0, np.nan)
    rexp = rng / _mean(rng, 63).replace(0, np.nan)
    b = (prox * rexp).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base height shrinkage over 2y: 252d amplitude vs 504d amplitude (tightening base)
def f06lb_f06_long_base_breakout_ampshrink_base_v135_signal(closeadj):
    a252 = (_rmax(closeadj, 252) - _rmin(closeadj, 252)) / closeadj.replace(0, np.nan)
    a504 = (_rmax(closeadj, 504) - _rmin(closeadj, 504)) / closeadj.replace(0, np.nan)
    b = a252 / a504.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# constructive-base tenure: current consecutive-day streak of holding above the 504d
# base midpoint, normalized (long uninterrupted tenure above mid => base maturing up)
def f06lb_f06_long_base_breakout_abovemid_504d_base_v136_signal(closeadj):
    mid = (_rmax(closeadj, 504) + _rmin(closeadj, 504)) / 2.0
    above = (closeadj > mid).astype(float)

    def _streak(a):
        c = 0
        for v in a[::-1]:
            if v >= 0.5:
                c += 1
            else:
                break
        return c
    b = above.rolling(252, min_periods=126).apply(_streak, raw=True) / 252.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout pullback resilience: drawdown from 21d high after a 252d breakout
def f06lb_f06_long_base_breakout_pullback_252d_base_v137_signal(closeadj):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    prox = (closeadj / ceil.replace(0, np.nan)).clip(upper=1.1)
    dd21 = closeadj / _rmax(closeadj, 21).replace(0, np.nan) - 1.0
    b = prox * dd21
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base volume profile skew: volume in upper half vs lower half of base (demand zone)
def f06lb_f06_long_base_breakout_volskew_252d_base_v138_signal(closeadj, volume):
    mid = (_rmax(closeadj, 252) + _rmin(closeadj, 252)) / 2.0
    uphalf = ((closeadj > mid).astype(float) * volume).rolling(126, min_periods=63).sum()
    dnhalf = ((closeadj <= mid).astype(float) * volume).rolling(126, min_periods=63).sum()
    b = (uphalf - dnhalf) / (uphalf + dnhalf).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from base ceiling in log terms over 1260d (multi-year overhead, log)
def f06lb_f06_long_base_breakout_logceil_1260d_base_v139_signal(closeadj):
    ceil = closeadj.shift(1).rolling(1260, min_periods=504).max()
    raw = np.log(closeadj.replace(0, np.nan) / ceil.replace(0, np.nan))
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# coil intensity: inverse base range times base position (tight AND near top)
def f06lb_f06_long_base_breakout_coilint_504d_base_v140_signal(closeadj):
    br = _f06_base_range(closeadj, 504)
    pos = _f06_basepos(closeadj, 504)
    b = pos / br.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-base-high persistence: fraction of 63d making fresh 504d highs (lid breaking)
def f06lb_f06_long_base_breakout_freshhi_504d_base_v141_signal(closeadj):
    hi = _rmax(closeadj, 504)
    fresh = (closeadj >= hi * 0.99999).astype(float)
    b = fresh.rolling(63, min_periods=21).mean() + 0.1 * _f06_ceiling_dist(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# measured-move readiness: how far through the 504d base price has travelled toward
# the ceiling, percentile-ranked vs its own 252d history (distinct from raw position)
def f06lb_f06_long_base_breakout_measmove_504d_base_v142_signal(closeadj):
    lo = _rmin(closeadj, 504)
    hi = _rmax(closeadj, 504)
    height = (hi - lo).replace(0, np.nan)
    progress = (closeadj - lo) / height
    b = _rank(progress, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base quietness: count of days in last year with daily range below 1% of price
def f06lb_f06_long_base_breakout_quietdays_252d_base_v143_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    quiet = (rng <= rng.rolling(504, min_periods=126).quantile(0.3)).astype(float)
    b = quiet.rolling(252, min_periods=126).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout follow-through asymmetry: up-vol minus down-vol momentum near lid
def f06lb_f06_long_base_breakout_ftasym_252d_base_v144_signal(closeadj, volume):
    ceil = closeadj.shift(1).rolling(252, min_periods=126).max()
    near = (closeadj / ceil.replace(0, np.nan) >= 0.95).astype(float)
    up = (closeadj > closeadj.shift(1)).astype(float)
    uv = (near * up * volume).rolling(63, min_periods=21).sum()
    dv = (near * (1 - up) * volume).rolling(63, min_periods=21).sum()
    b = (uv - dv) / (uv + dv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# base contraction over 5y: 504d range vs 1260d range, z-scored (long coil regime)
def f06lb_f06_long_base_breakout_longcoilz_base_v145_signal(closeadj):
    s = _f06_base_range(closeadj, 504)
    l = _f06_base_range(closeadj, 1260)
    ratio = s / l.replace(0, np.nan)
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout strength times accumulation: pop magnitude x money-flow position
def f06lb_f06_long_base_breakout_popacc_252d_base_v146_signal(high, low, close, closeadj, volume):
    bo = _f06_breakout(closeadj, 252)
    mfm = ((close - low) - (high - close)) / (high - low).replace(0, np.nan)
    mf = (mfm * volume).rolling(21, min_periods=10).sum() / volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = bo + 0.5 * mf
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# stair-step base: count of higher 63d-lows over last year (rising base structure)
def f06lb_f06_long_base_breakout_higherlows_252d_base_v147_signal(closeadj):
    lo63 = _rmin(closeadj, 63)
    higher = (lo63 > lo63.shift(21)).astype(float)
    b = higher.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakout quality vs base age: pop magnitude weighted by base maturity duration
def f06lb_f06_long_base_breakout_matpop_504d_base_v148_signal(closeadj):
    bo = _f06_breakout(closeadj, 504)
    br = _f06_base_range(closeadj, 504)
    mature = (br <= br.rolling(1260, min_periods=504).median()).astype(float).rolling(252, min_periods=126).mean()
    b = bo * mature
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position dispersion across 252/504/1260 (anchor-base disagreement)
def f06lb_f06_long_base_breakout_posdisp_multi_base_v149_signal(closeadj):
    p1 = _f06_basepos(closeadj, 252)
    p2 = _f06_basepos(closeadj, 504)
    p3 = _f06_basepos(closeadj, 1260)
    b = pd.concat([p1, p2, p3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite coiled-spring: tight base x near-lid x dry volume (pre-breakout setup)
def f06lb_f06_long_base_breakout_setup_252d_base_v150_signal(closeadj, volume):
    br = _f06_base_range(closeadj, 252)
    pos = _f06_basepos(closeadj, 252)
    voldry = _mean(volume, 21) / _mean(volume, 252).replace(0, np.nan)
    b = (pos / br.replace(0, np.nan)) * (1.0 / voldry.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06lb_f06_long_base_breakout_dvoldry_252d_base_v076_signal,
    f06lb_f06_long_base_breakout_dvolsurge_252d_base_v077_signal,
    f06lb_f06_long_base_breakout_brkmoney_252d_base_v078_signal,
    f06lb_f06_long_base_breakout_pkrange_252d_base_v079_signal,
    f06lb_f06_long_base_breakout_hlbasetight_504d_base_v080_signal,
    f06lb_f06_long_base_breakout_truebrkatr_504d_base_v081_signal,
    f06lb_f06_long_base_breakout_channelslope_504d_base_v082_signal,
    f06lb_f06_long_base_breakout_widthstab_252d_base_v083_signal,
    f06lb_f06_long_base_breakout_qualbrk_504d_base_v084_signal,
    f06lb_f06_long_base_breakout_ceilvol_252d_base_v085_signal,
    f06lb_f06_long_base_breakout_floorvol_252d_base_v086_signal,
    f06lb_f06_long_base_breakout_contractacc_base_v087_signal,
    f06lb_f06_long_base_breakout_tightstreak_252d_base_v088_signal,
    f06lb_f06_long_base_breakout_upvolthrust_252d_base_v089_signal,
    f06lb_f06_long_base_breakout_baseamp_1260d_base_v090_signal,
    f06lb_f06_long_base_breakout_upperhug_504d_base_v091_signal,
    f06lb_f06_long_base_breakout_lowerhug_504d_base_v092_signal,
    f06lb_f06_long_base_breakout_cleanatr_252d_base_v093_signal,
    f06lb_f06_long_base_breakout_failsev_252d_base_v094_signal,
    f06lb_f06_long_base_breakout_posmom_252d_base_v095_signal,
    f06lb_f06_long_base_breakout_quietcoil_252d_base_v096_signal,
    f06lb_f06_long_base_breakout_pathineff_504d_base_v097_signal,
    f06lb_f06_long_base_breakout_coilpop_252d_base_v098_signal,
    f06lb_f06_long_base_breakout_touches_504d_base_v099_signal,
    f06lb_f06_long_base_breakout_floordur_252d_base_v100_signal,
    f06lb_f06_long_base_breakout_rangevov_252d_base_v101_signal,
    f06lb_f06_long_base_breakout_gapthrust_252d_base_v102_signal,
    f06lb_f06_long_base_breakout_apex_252d_base_v103_signal,
    f06lb_f06_long_base_breakout_holdfrac_252d_base_v104_signal,
    f06lb_f06_long_base_breakout_dvoltrend_252d_base_v105_signal,
    f06lb_f06_long_base_breakout_retest_252d_base_v106_signal,
    f06lb_f06_long_base_breakout_hifresh_base_v107_signal,
    f06lb_f06_long_base_breakout_brkrank_252d_base_v108_signal,
    f06lb_f06_long_base_breakout_squeezerel_252d_base_v109_signal,
    f06lb_f06_long_base_breakout_baseacc_126d_base_v110_signal,
    f06lb_f06_long_base_breakout_failrate_504d_base_v111_signal,
    f06lb_f06_long_base_breakout_tightasym_252d_base_v112_signal,
    f06lb_f06_long_base_breakout_deepliftatr_1260d_base_v113_signal,
    f06lb_f06_long_base_breakout_brkmomq_252d_base_v114_signal,
    f06lb_f06_long_base_breakout_baseformrank_1260d_base_v115_signal,
    f06lb_f06_long_base_breakout_volpos_252d_base_v116_signal,
    f06lb_f06_long_base_breakout_lidcatch_252d_base_v117_signal,
    f06lb_f06_long_base_breakout_extexh_252d_base_v118_signal,
    f06lb_f06_long_base_breakout_deeprecov_base_v119_signal,
    f06lb_f06_long_base_breakout_brkliq_252d_base_v120_signal,
    f06lb_f06_long_base_breakout_basematdur_504d_base_v121_signal,
    f06lb_f06_long_base_breakout_pinch_252d_base_v122_signal,
    f06lb_f06_long_base_breakout_midbias_252d_base_v123_signal,
    f06lb_f06_long_base_breakout_ceilsmooth_252d_base_v124_signal,
    f06lb_f06_long_base_breakout_partic_252d_base_v125_signal,
    f06lb_f06_long_base_breakout_symmetry_1260d_base_v126_signal,
    f06lb_f06_long_base_breakout_coilspeed_252d_base_v127_signal,
    f06lb_f06_long_base_breakout_netquality_252d_base_v128_signal,
    f06lb_f06_long_base_breakout_drifteff_252d_base_v129_signal,
    f06lb_f06_long_base_breakout_headroomrank_504d_base_v130_signal,
    f06lb_f06_long_base_breakout_thrustamp_252d_base_v131_signal,
    f06lb_f06_long_base_breakout_accstreak_base_v132_signal,
    f06lb_f06_long_base_breakout_longprox_1260d_base_v133_signal,
    f06lb_f06_long_base_breakout_rangepop_252d_base_v134_signal,
    f06lb_f06_long_base_breakout_ampshrink_base_v135_signal,
    f06lb_f06_long_base_breakout_abovemid_504d_base_v136_signal,
    f06lb_f06_long_base_breakout_pullback_252d_base_v137_signal,
    f06lb_f06_long_base_breakout_volskew_252d_base_v138_signal,
    f06lb_f06_long_base_breakout_logceil_1260d_base_v139_signal,
    f06lb_f06_long_base_breakout_coilint_504d_base_v140_signal,
    f06lb_f06_long_base_breakout_freshhi_504d_base_v141_signal,
    f06lb_f06_long_base_breakout_measmove_504d_base_v142_signal,
    f06lb_f06_long_base_breakout_quietdays_252d_base_v143_signal,
    f06lb_f06_long_base_breakout_ftasym_252d_base_v144_signal,
    f06lb_f06_long_base_breakout_longcoilz_base_v145_signal,
    f06lb_f06_long_base_breakout_popacc_252d_base_v146_signal,
    f06lb_f06_long_base_breakout_higherlows_252d_base_v147_signal,
    f06lb_f06_long_base_breakout_matpop_504d_base_v148_signal,
    f06lb_f06_long_base_breakout_posdisp_multi_base_v149_signal,
    f06lb_f06_long_base_breakout_setup_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_LONG_BASE_BREAKOUT_REGISTRY_076_150 = REGISTRY


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

    print("OK f06_long_base_breakout_base_076_150_claude: %d features pass" % n_features)
