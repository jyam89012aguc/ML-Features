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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives: candle / range structure (per-day, unadjusted) =====
def _f13_range(high, low):
    # full daily high-low range
    return (high - low)


def _f13_body(open, close):
    # signed body
    return (close - open)


def _f13_body_abs(open, close):
    return (close - open).abs()


def _f13_body_ratio(open, high, low, close):
    # |body| / range : how much of the bar is directional body vs wick
    rng = (high - low).replace(0, np.nan)
    return (close - open).abs() / rng


def _f13_upper_wick(open, high, low, close):
    top = pd.concat([open, close], axis=1).max(axis=1)
    return (high - top)


def _f13_lower_wick(open, high, low, close):
    bot = pd.concat([open, close], axis=1).min(axis=1)
    return (bot - low)


def _f13_upper_wick_ratio(open, high, low, close):
    rng = (high - low).replace(0, np.nan)
    top = pd.concat([open, close], axis=1).max(axis=1)
    return (high - top) / rng


def _f13_lower_wick_ratio(open, high, low, close):
    rng = (high - low).replace(0, np.nan)
    bot = pd.concat([open, close], axis=1).min(axis=1)
    return (bot - low) / rng


def _f13_close_in_range(high, low, close):
    # where close sits in the bar: 0=at low, 1=at high (Williams %R-like)
    rng = (high - low).replace(0, np.nan)
    return (close - low) / rng


def _f13_open_in_range(open, high, low):
    rng = (high - low).replace(0, np.nan)
    return (open - low) / rng


def _f13_range_pct(high, low, close):
    # range normalized by close (intraday true-range proxy)
    return (high - low) / close.replace(0, np.nan)


def _f13_doji(open, high, low, close, thr=0.1):
    # doji = tiny body relative to range
    br = _f13_body_ratio(open, high, low, close)
    return (br <= thr).astype(float)


def _f13_typical(high, low, close):
    return (high + low + close) / 3.0


# ============================================================
# body/range ratio level
def f13cr_f13_candle_range_structure_bodyrng_5d_base_v001_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    b = _mean(br, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body/range ratio 21d level
def f13cr_f13_candle_range_structure_bodyrng_21d_base_v002_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    b = _mean(br, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body/range ratio 63d, z-scored vs own 126d history (de-trended decisiveness)
def f13cr_f13_candle_range_structure_bodyrngz_63d_base_v003_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    m = _mean(br, 63)
    b = _z(m, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick ratio (rejection at highs), 21d mean
def f13cr_f13_candle_range_structure_uwick_21d_base_v004_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    b = _mean(uw, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-wick ratio (demand at lows), 21d mean
def f13cr_f13_candle_range_structure_lwick_21d_base_v005_signal(open, high, low, close):
    lw = _f13_lower_wick_ratio(open, high, low, close)
    b = _mean(lw, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wick skew: lower-wick minus upper-wick mean (net demand vs rejection), 21d
def f13cr_f13_candle_range_structure_wickskew_21d_base_v006_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    b = _mean(lw - uw, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wick skew 63d (slower demand/rejection balance)
def f13cr_f13_candle_range_structure_wickskew_63d_base_v007_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    b = _mean(lw - uw, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-in-range (close strength) 5d mean - 0.5 centered
def f13cr_f13_candle_range_structure_cir_5d_base_v008_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    b = _mean(cir, 5) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-in-range 21d mean - 0.5
def f13cr_f13_candle_range_structure_cir_21d_base_v009_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    b = _mean(cir, 21) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-in-range 63d, z-scored vs own 126d history
def f13cr_f13_candle_range_structure_cirz_63d_base_v010_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    m = _mean(cir, 63)
    b = _z(m, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range as % of close (intraday range intensity), 21d mean
def f13cr_f13_candle_range_structure_rngpct_21d_base_v011_signal(high, low, close):
    rp = _f13_range_pct(high, low, close)
    b = _mean(rp, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range % z-scored vs own 63d history (range-expansion vs typical)
def f13cr_f13_candle_range_structure_rngpctz_63d_base_v012_signal(high, low, close):
    rp = _f13_range_pct(high, low, close)
    b = _z(rp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion: trailing 5d avg range vs trailing 21d avg range (smoothed expansion)
def f13cr_f13_candle_range_structure_rngexp_21d_base_v013_signal(high, low):
    rng = _f13_range(high, low)
    b = _mean(rng, 5) / _mean(rng, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion vs body: range/|body| (wide-range vs decisive), 21d mean
def f13cr_f13_candle_range_structure_rngvbody_21d_base_v014_signal(open, high, low, close):
    rng = _f13_range(high, low)
    body = _f13_body_abs(open, close).replace(0, np.nan)
    ratio = rng / body
    b = _mean(ratio.clip(upper=50), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# doji frequency over 21d (indecision frequency) + continuous small-body depth
def f13cr_f13_candle_range_structure_dojifreq_21d_base_v015_signal(open, high, low, close):
    d = _f13_doji(open, high, low, close, 0.1)
    br = _f13_body_ratio(open, high, low, close)
    depth = (0.1 - br).clip(lower=0)
    b = _mean(d, 21) + 2.0 * _mean(depth, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# doji frequency over 63d weighted by small-body depth (continuous indecision)
def f13cr_f13_candle_range_structure_dojifreq_63d_base_v016_signal(open, high, low, close):
    d = _f13_doji(open, high, low, close, 0.15)
    br = _f13_body_ratio(open, high, low, close)
    depth = (0.15 - br).clip(lower=0)
    b = _mean(d, 63) + 3.0 * _mean(depth, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# climactic candle: wide range + big volume (range z * volume z), 5d max
def f13cr_f13_candle_range_structure_climax_5d_base_v017_signal(high, low, volume):
    rngz = _z(_f13_range(high, low), 63)
    volz = _z(volume, 63)
    clim = rngz * volz
    b = _rmax(clim, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# climactic candle intensity over 21d: mean of positive range-z*vol-z product (continuous)
def f13cr_f13_candle_range_structure_climaxfreq_21d_base_v018_signal(high, low, volume):
    rngz = _z(_f13_range(high, low), 63)
    volz = _z(volume, 63)
    clim = (rngz.clip(lower=0) * volz.clip(lower=0))
    b = _mean(clim, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capitulation intensity: down-bar lower-wick depth scaled by volume-z, 21d mean (continuous)
def f13cr_f13_candle_range_structure_capit_21d_base_v019_signal(open, high, low, close, volume):
    down = (close < open).astype(float)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    volz = _z(volume, 63).clip(lower=0)
    cap = down * lw * volz
    b = _mean(cap, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marubozu intensity: excess of body-ratio above 0.8 (full-body decisiveness), 21d mean
def f13cr_f13_candle_range_structure_maru_21d_base_v020_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    maru = (br - 0.8).clip(lower=0)
    b = _mean(maru, 21) + 0.5 * _mean((br >= 0.8).astype(float), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body sign persistence weighted by body magnitude (net conviction), 21d
def f13cr_f13_candle_range_structure_bodysign_21d_base_v021_signal(open, close):
    sgn = np.sign(close - open)
    mag = (close - open).abs() / close.replace(0, np.nan)
    b = _mean(sgn, 21) + 5.0 * _mean(sgn * mag, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed body / range mean (directional conviction), 21d
def f13cr_f13_candle_range_structure_sbodyrng_21d_base_v022_signal(open, high, low, close):
    rng = (high - low).replace(0, np.nan)
    sbr = (close - open) / rng
    b = _mean(sbr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed body/range 63d z-scored
def f13cr_f13_candle_range_structure_sbodyrngz_63d_base_v023_signal(open, high, low, close):
    rng = (high - low).replace(0, np.nan)
    sbr = (close - open) / rng
    m = _mean(sbr, 63)
    b = _z(m, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick dominance magnitude (rejection asymmetry, excess over lower wick) 21d
def f13cr_f13_candle_range_structure_uwickdom_21d_base_v024_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    dom = (uw - lw).clip(lower=0)
    b = _mean(dom, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-wick dominance magnitude (support asymmetry, excess over upper wick) 21d
def f13cr_f13_candle_range_structure_lwickdom_21d_base_v025_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    dom = (lw - uw).clip(lower=0)
    b = _mean(dom, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total-wick to body length ratio (wick-to-body leverage), 21d mean (capped)
def f13cr_f13_candle_range_structure_wickfrac_21d_base_v026_signal(open, high, low, close):
    uw = _f13_upper_wick(open, high, low, close)
    lw = _f13_lower_wick(open, high, low, close)
    body = _f13_body_abs(open, close).replace(0, np.nan)
    ratio = ((uw + lw) / body).clip(upper=30)
    b = _mean(ratio, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-in-range dispersion: std of close-in-range over 21d (consistency of close strength)
def f13cr_f13_candle_range_structure_cirdisp_21d_base_v027_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    b = _std(cir, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range % dispersion (range-of-ranges), 21d std
def f13cr_f13_candle_range_structure_rngdisp_21d_base_v028_signal(high, low, close):
    rp = _f13_range_pct(high, low, close)
    b = _std(rp, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion streak (count) blended with magnitude of expansion (continuous)
def f13cr_f13_candle_range_structure_rngexpstk_base_v029_signal(high, low):
    rng = _f13_range(high, low)
    up = (rng > rng.shift(1)).astype(float)
    grp = (up == 0).cumsum()
    streak = up.groupby(grp).cumsum()
    mag = (rng / rng.shift(1).replace(0, np.nan) - 1.0).clip(lower=0)
    b = streak.clip(upper=10) / 10.0 + _mean(mag, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-contraction streak (NR-like) blended with contraction magnitude (continuous)
def f13cr_f13_candle_range_structure_rngconstk_base_v030_signal(high, low):
    rng = _f13_range(high, low)
    dn = (rng < rng.shift(1)).astype(float)
    grp = (dn == 0).cumsum()
    streak = dn.groupby(grp).cumsum()
    mag = (1.0 - rng / rng.shift(1).replace(0, np.nan)).clip(lower=0)
    b = streak.clip(upper=10) / 10.0 + _mean(mag, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# narrow-range-day pressure: depth below trailing-7 mean when range is smallest, 21d
def f13cr_f13_candle_range_structure_nr7freq_21d_base_v031_signal(high, low):
    rng = _f13_range(high, low)
    nr = (rng <= _rmin(rng, 7)).astype(float)
    depth = (1.0 - rng / _mean(rng, 7).replace(0, np.nan)).clip(lower=0)
    b = _mean(nr, 21) + _mean(nr * depth, 21) * 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wide-range-day pressure: excess over trailing-7 mean when range is largest, 21d
def f13cr_f13_candle_range_structure_wr7freq_21d_base_v032_signal(high, low):
    rng = _f13_range(high, low)
    wr = (rng >= _rmax(rng, 7)).astype(float)
    exc = (rng / _mean(rng, 7).replace(0, np.nan) - 1.0).clip(lower=0)
    b = _mean(wr, 21) + _mean(wr * exc, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-bar close strength: mean close-in-range on up bars only (follow-through), 21d
def f13cr_f13_candle_range_structure_upclosestr_21d_base_v033_signal(open, high, low, close):
    cir = _f13_close_in_range(high, low, close)
    up = (close > open)
    val = cir.where(up)
    b = val.rolling(21, min_periods=5).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# down-bar close weakness: mean close-in-range on down bars (capitulation depth), 21d
def f13cr_f13_candle_range_structure_dnclosewk_21d_base_v034_signal(open, high, low, close):
    cir = _f13_close_in_range(high, low, close)
    dn = (close < open)
    val = cir.where(dn)
    b = val.rolling(21, min_periods=5).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-range ratio percentile-rank vs own 126d (relative decisiveness)
def f13cr_f13_candle_range_structure_bodyrngrank_21d_base_v035_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    m = _mean(br, 21)
    b = _rank(m, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range%-rank vs own 252d (range regime percentile)
def f13cr_f13_candle_range_structure_rngpctrank_21d_base_v036_signal(high, low, close):
    rp = _f13_range_pct(high, low, close)
    m = _mean(rp, 21)
    b = _rank(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted body/range: decisiveness weighted by participation, 21d
def f13cr_f13_candle_range_structure_vwbodyrng_21d_base_v037_signal(open, high, low, close, volume):
    br = _f13_body_ratio(open, high, low, close)
    wsum = (br * volume).rolling(21, min_periods=5).sum()
    vsum = volume.rolling(21, min_periods=5).sum().replace(0, np.nan)
    b = wsum / vsum
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted close-in-range (where volume traded into the close), 21d
def f13cr_f13_candle_range_structure_vwcir_21d_base_v038_signal(high, low, close, volume):
    cir = _f13_close_in_range(high, low, close)
    wsum = (cir * volume).rolling(21, min_periods=5).sum()
    vsum = volume.rolling(21, min_periods=5).sum().replace(0, np.nan)
    b = wsum / vsum - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-vs-body: opening gap (open vs prior close) relative to bar range, 21d mean abs
def f13cr_f13_candle_range_structure_gapinbar_21d_base_v039_signal(open, high, low, close):
    rng = (high - low).replace(0, np.nan)
    gap = (open - close.shift(1)).abs() / rng
    b = _mean(gap, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# open position in range (where the day opened): persistent open-low/open-high bias, 21d
def f13cr_f13_candle_range_structure_openinrng_21d_base_v040_signal(open, high, low):
    oir = _f13_open_in_range(open, high, low)
    b = _mean(oir, 21) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday choppiness: 21d std of day-to-day close-in-range changes (whipsaw)
def f13cr_f13_candle_range_structure_drive_21d_base_v041_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    b = _std(cir.diff(), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pin-bar pressure: max wick ratio (dominant-tail magnitude), 21d mean
def f13cr_f13_candle_range_structure_pinfreq_21d_base_v042_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    dom = pd.concat([uw, lw], axis=1).max(axis=1)
    b = _mean(dom, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# engulfing magnitude: today's body size relative to prior body when it engulfs, 21d
def f13cr_f13_candle_range_structure_engulf_21d_base_v043_signal(open, close):
    body_lo = pd.concat([open, close], axis=1).min(axis=1)
    body_hi = pd.concat([open, close], axis=1).max(axis=1)
    eng = ((body_lo < body_lo.shift(1)) & (body_hi > body_hi.shift(1))).astype(float)
    today = (body_hi - body_lo)
    prior = (body_hi.shift(1) - body_lo.shift(1)).replace(0, np.nan)
    mag = eng * (today / prior - 1.0).clip(lower=0, upper=10)
    b = _mean(eng, 21) + 0.2 * _mean(mag, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inside-bar compression: how far today's range sits inside yesterday's, 21d
def f13cr_f13_candle_range_structure_inside_21d_base_v044_signal(high, low):
    ins = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    comp = (1.0 - _f13_range(high, low) / _f13_range(high, low).shift(1).replace(0, np.nan)).clip(lower=0)
    b = _mean(ins, 21) + _mean(ins * comp, 21) * 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# outside-bar expansion: how far today's range engulfs yesterday's, 21d
def f13cr_f13_candle_range_structure_outside_21d_base_v045_signal(high, low):
    out = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    exp = (_f13_range(high, low) / _f13_range(high, low).shift(1).replace(0, np.nan) - 1.0).clip(lower=0)
    b = _mean(out, 21) + _mean(out * exp, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-expansion thrust: rank of current 5d range vs its own 126d distribution
def f13cr_f13_candle_range_structure_rngthrust_21d_base_v046_signal(high, low):
    rng = _f13_range(high, low)
    r5 = _mean(rng, 5)
    b = _rank(r5, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body momentum: 5d mean signed body/range minus 21d mean (short vs long conviction)
def f13cr_f13_candle_range_structure_bodymom_5v21_base_v047_signal(open, high, low, close):
    rng = (high - low).replace(0, np.nan)
    sbr = (close - open) / rng
    b = _mean(sbr, 5) - _mean(sbr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wick-skew momentum: 5d wick skew minus 21d wick skew
def f13cr_f13_candle_range_structure_wickmom_5v21_base_v048_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    sk = lw - uw
    b = _mean(sk, 5) - _mean(sk, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# climactic-up intensity: range-z * close-strength * vol-z, positive part, 21d mean
def f13cr_f13_candle_range_structure_climaxup_21d_base_v049_signal(high, low, close, volume):
    rngz = _z(_f13_range(high, low), 63).clip(lower=0)
    cir = (_f13_close_in_range(high, low, close) - 0.5).clip(lower=0)
    volz = _z(volume, 63).clip(lower=0)
    clim = rngz * cir * volz
    b = _mean(clim, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# climactic-down intensity: range-z * close-weakness * vol-z, positive part, 21d mean
def f13cr_f13_candle_range_structure_climaxdn_21d_base_v050_signal(high, low, close, volume):
    rngz = _z(_f13_range(high, low), 63).clip(lower=0)
    cir = (0.5 - _f13_close_in_range(high, low, close)).clip(lower=0)
    volz = _z(volume, 63).clip(lower=0)
    clim = rngz * cir * volz
    b = _mean(clim, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range upside semivariance: dispersion of above-median range days only (252d), 21d
def f13cr_f13_candle_range_structure_rngextreme_base_v051_signal(high, low, close):
    rp = _f13_range_pct(high, low, close)
    med = rp.rolling(252, min_periods=126).median()
    exc = (rp - med).clip(lower=0)
    b = _std(exc, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overhead supply vs conviction: (high-close) relative to |body|, capped, 21d mean
def f13cr_f13_candle_range_structure_upshare_21d_base_v052_signal(open, high, close):
    body = (close - open).abs().replace(0, np.nan)
    overhead = ((high - close) / body).clip(upper=20)
    b = _mean(overhead, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-location skewness: 21d rolling skew of close-in-range (asymmetric closing bias)
def f13cr_f13_candle_range_structure_typskew_21d_base_v053_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    b = cir.rolling(21, min_periods=10).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional body run length x cumulative body magnitude within the run (signed)
def f13cr_f13_candle_range_structure_bodyrun_base_v054_signal(open, close):
    sgn = np.sign(close - open)
    mag = (close - open).abs() / close.replace(0, np.nan)
    grp = (sgn != sgn.shift(1)).cumsum()
    runlen = sgn.groupby(grp).cumcount() + 1
    cummag = mag.groupby(grp).cumsum()
    b = sgn * (runlen.clip(upper=12) / 12.0) * (1.0 + 10.0 * cummag)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-size dispersion: std of |body|/close over 21d (erratic-bar regime)
def f13cr_f13_candle_range_structure_bodydisp_21d_base_v055_signal(open, close):
    bsz = (close - open).abs() / close.replace(0, np.nan)
    b = _std(bsz, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range autocorrelation proxy: corr of range with prior-day range over 63d (clustering)
def f13cr_f13_candle_range_structure_rngclust_63d_base_v056_signal(high, low):
    rng = _f13_range(high, low)
    lag = rng.shift(1)
    cov = (rng * lag).rolling(63, min_periods=21).mean() - _mean(rng, 63) * _mean(lag, 63)
    b = cov / (_std(rng, 63) * _std(lag, 63)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# decisiveness instability: dispersion (std) of body/range over 63d (regime churn)
def f13cr_f13_candle_range_structure_bodyrngspr_5v63_base_v057_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    b = _std(br, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net wick balance weighted by range size (big-bar rejection emphasis), 21d
def f13cr_f13_candle_range_structure_wickwt_21d_base_v058_signal(open, high, low, close):
    uw = _f13_upper_wick(open, high, low, close)
    lw = _f13_lower_wick(open, high, low, close)
    net = (lw - uw)
    rng = _f13_range(high, low).replace(0, np.nan)
    b = _mean(net, 21) / _mean(rng, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tail-risk bar pressure: standardized exceedance of range% over its 63d mean, 21d
def f13cr_f13_candle_range_structure_tailbar_21d_base_v059_signal(high, low, close):
    rp = _f13_range_pct(high, low, close)
    thr = _mean(rp, 63) + 1.28 * _std(rp, 63)
    exc = ((rp - thr) / _std(rp, 63).replace(0, np.nan)).clip(lower=0)
    tail = (rp > thr).astype(float)
    b = _mean(tail, 21) + 0.3 * _mean(exc, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight-vs-intraday variance share: std of overnight gaps vs std of intraday ranges, 21d
def f13cr_f13_candle_range_structure_overnight_21d_base_v060_signal(open, high, low, close):
    onr = (open - close.shift(1)) / close.shift(1).replace(0, np.nan)
    rng = _f13_range(high, low) / close.replace(0, np.nan)
    b = _std(onr, 21) / (_std(onr, 21) + _std(rng, 21)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion regime: mean positive excess of range over 1.5x its 21d avg, 21d
def f13cr_f13_candle_range_structure_expregime_21d_base_v061_signal(high, low):
    rng = _f13_range(high, low)
    avg = _mean(rng, 21).replace(0, np.nan)
    expd = (rng > 1.5 * avg).astype(float)
    exc = (rng / avg - 1.5).clip(lower=0)
    b = _mean(expd, 21) + 0.5 * _mean(exc, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# doji clustering: small-body-depth weighted 21d minus 63d (indecision flare-up)
def f13cr_f13_candle_range_structure_dojiflare_base_v062_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    indec = (0.2 - br).clip(lower=0)
    b = _mean(indec, 21) - _mean(indec, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# strong-close streak x cumulative close-strength within the streak (continuous)
def f13cr_f13_candle_range_structure_strongclstk_base_v063_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    strong = (cir >= 0.6667).astype(float)
    grp = (strong == 0).cumsum()
    streak = strong.groupby(grp).cumsum()
    depth = (cir - 0.6667).clip(lower=0)
    cumd = depth.groupby(grp).cumsum()
    b = streak.clip(upper=10) / 10.0 + cumd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weak-close streak x cumulative close-weakness within the streak (continuous)
def f13cr_f13_candle_range_structure_weakclstk_base_v064_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    weak = (cir <= 0.3333).astype(float)
    grp = (weak == 0).cumsum()
    streak = weak.groupby(grp).cumsum()
    depth = (0.3333 - cir).clip(lower=0)
    cumd = depth.groupby(grp).cumsum()
    b = streak.clip(upper=10) / 10.0 + cumd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume per unit range (effort vs result): high effort low movement, 21d
def f13cr_f13_candle_range_structure_effort_21d_base_v065_signal(high, low, close, volume):
    rng = _f13_range_pct(high, low, close).replace(0, np.nan)
    eff = volume / rng
    b = _z(eff, 63).rolling(21, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range skew: are big-range days up or down? signed-body * range z mean, 21d
def f13cr_f13_candle_range_structure_rngdirskew_21d_base_v066_signal(open, high, low, close):
    rngz = _z(_f13_range(high, low), 63)
    sgn = np.sign(close - open)
    b = _mean(sgn * rngz, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick z (rejection intensity vs own history), 21d mean
def f13cr_f13_candle_range_structure_uwickz_21d_base_v067_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    b = _z(uw, 63).rolling(21, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-wick z (demand intensity vs own history), 21d mean
def f13cr_f13_candle_range_structure_lwickz_21d_base_v068_signal(open, high, low, close):
    lw = _f13_lower_wick_ratio(open, high, low, close)
    b = _z(lw, 63).rolling(21, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spinning-top intensity: balanced-wick smallness = min(uw,lw)*(1-body), 21d mean
def f13cr_f13_candle_range_structure_spintop_21d_base_v069_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    bal = pd.concat([uw, lw], axis=1).min(axis=1) * (1.0 - br).clip(lower=0)
    b = _mean(bal, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-day intensity: drive * close-extremity (continuous trend-day strength), 21d
def f13cr_f13_candle_range_structure_trendday_21d_base_v070_signal(open, high, low, close):
    rng = (high - low).replace(0, np.nan)
    drive = (close - open).abs() / rng
    cir = _f13_close_in_range(high, low, close)
    extr = (cir - 0.5).abs() * 2.0
    b = _mean(drive * extr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range compression ratio: 5d avg range vs 63d avg range (squeeze level)
def f13cr_f13_candle_range_structure_squeeze_5v63_base_v071_signal(high, low):
    rng = _f13_range(high, low)
    b = _mean(rng, 5) / _mean(rng, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-to-range entropy proxy: mean of br*(1-br) (mid-decisiveness/uncertainty), 21d
def f13cr_f13_candle_range_structure_brentropy_21d_base_v072_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close).clip(0, 1)
    ent = br * (1.0 - br)
    b = _mean(ent, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-weighted CLV: accumulation emphasized on wide-range bars, 21d (big-bar accumulation)
def f13cr_f13_candle_range_structure_clv_21d_base_v073_signal(high, low, close):
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    rngz = _z(_f13_range(high, low), 63)
    w = rngz.clip(lower=-2) + 2.0
    wsum = (clv * w).rolling(21, min_periods=5).sum()
    wd = w.rolling(21, min_periods=5).sum().replace(0, np.nan)
    b = wsum / wd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# reversal-bar intensity: counter-trend wick magnitude vs prior body direction, 21d
def f13cr_f13_candle_range_structure_revbar_21d_base_v074_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    prev_up = (close.shift(1) > open.shift(1)).astype(float)
    prev_dn = (close.shift(1) < open.shift(1)).astype(float)
    rev = prev_up * uw + prev_dn * lw
    b = _mean(rev, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-expansion-with-volume confirmation: corr-style product, 21d mean
def f13cr_f13_candle_range_structure_rngvolconf_21d_base_v075_signal(high, low, volume):
    rngz = _z(_f13_range(high, low), 63)
    volz = _z(volume, 63)
    b = _mean(rngz * volz, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f13cr_f13_candle_range_structure_bodyrng_5d_base_v001_signal,
    f13cr_f13_candle_range_structure_bodyrng_21d_base_v002_signal,
    f13cr_f13_candle_range_structure_bodyrngz_63d_base_v003_signal,
    f13cr_f13_candle_range_structure_uwick_21d_base_v004_signal,
    f13cr_f13_candle_range_structure_lwick_21d_base_v005_signal,
    f13cr_f13_candle_range_structure_wickskew_21d_base_v006_signal,
    f13cr_f13_candle_range_structure_wickskew_63d_base_v007_signal,
    f13cr_f13_candle_range_structure_cir_5d_base_v008_signal,
    f13cr_f13_candle_range_structure_cir_21d_base_v009_signal,
    f13cr_f13_candle_range_structure_cirz_63d_base_v010_signal,
    f13cr_f13_candle_range_structure_rngpct_21d_base_v011_signal,
    f13cr_f13_candle_range_structure_rngpctz_63d_base_v012_signal,
    f13cr_f13_candle_range_structure_rngexp_21d_base_v013_signal,
    f13cr_f13_candle_range_structure_rngvbody_21d_base_v014_signal,
    f13cr_f13_candle_range_structure_dojifreq_21d_base_v015_signal,
    f13cr_f13_candle_range_structure_dojifreq_63d_base_v016_signal,
    f13cr_f13_candle_range_structure_climax_5d_base_v017_signal,
    f13cr_f13_candle_range_structure_climaxfreq_21d_base_v018_signal,
    f13cr_f13_candle_range_structure_capit_21d_base_v019_signal,
    f13cr_f13_candle_range_structure_maru_21d_base_v020_signal,
    f13cr_f13_candle_range_structure_bodysign_21d_base_v021_signal,
    f13cr_f13_candle_range_structure_sbodyrng_21d_base_v022_signal,
    f13cr_f13_candle_range_structure_sbodyrngz_63d_base_v023_signal,
    f13cr_f13_candle_range_structure_uwickdom_21d_base_v024_signal,
    f13cr_f13_candle_range_structure_lwickdom_21d_base_v025_signal,
    f13cr_f13_candle_range_structure_wickfrac_21d_base_v026_signal,
    f13cr_f13_candle_range_structure_cirdisp_21d_base_v027_signal,
    f13cr_f13_candle_range_structure_rngdisp_21d_base_v028_signal,
    f13cr_f13_candle_range_structure_rngexpstk_base_v029_signal,
    f13cr_f13_candle_range_structure_rngconstk_base_v030_signal,
    f13cr_f13_candle_range_structure_nr7freq_21d_base_v031_signal,
    f13cr_f13_candle_range_structure_wr7freq_21d_base_v032_signal,
    f13cr_f13_candle_range_structure_upclosestr_21d_base_v033_signal,
    f13cr_f13_candle_range_structure_dnclosewk_21d_base_v034_signal,
    f13cr_f13_candle_range_structure_bodyrngrank_21d_base_v035_signal,
    f13cr_f13_candle_range_structure_rngpctrank_21d_base_v036_signal,
    f13cr_f13_candle_range_structure_vwbodyrng_21d_base_v037_signal,
    f13cr_f13_candle_range_structure_vwcir_21d_base_v038_signal,
    f13cr_f13_candle_range_structure_gapinbar_21d_base_v039_signal,
    f13cr_f13_candle_range_structure_openinrng_21d_base_v040_signal,
    f13cr_f13_candle_range_structure_drive_21d_base_v041_signal,
    f13cr_f13_candle_range_structure_pinfreq_21d_base_v042_signal,
    f13cr_f13_candle_range_structure_engulf_21d_base_v043_signal,
    f13cr_f13_candle_range_structure_inside_21d_base_v044_signal,
    f13cr_f13_candle_range_structure_outside_21d_base_v045_signal,
    f13cr_f13_candle_range_structure_rngthrust_21d_base_v046_signal,
    f13cr_f13_candle_range_structure_bodymom_5v21_base_v047_signal,
    f13cr_f13_candle_range_structure_wickmom_5v21_base_v048_signal,
    f13cr_f13_candle_range_structure_climaxup_21d_base_v049_signal,
    f13cr_f13_candle_range_structure_climaxdn_21d_base_v050_signal,
    f13cr_f13_candle_range_structure_rngextreme_base_v051_signal,
    f13cr_f13_candle_range_structure_upshare_21d_base_v052_signal,
    f13cr_f13_candle_range_structure_typskew_21d_base_v053_signal,
    f13cr_f13_candle_range_structure_bodyrun_base_v054_signal,
    f13cr_f13_candle_range_structure_bodydisp_21d_base_v055_signal,
    f13cr_f13_candle_range_structure_rngclust_63d_base_v056_signal,
    f13cr_f13_candle_range_structure_bodyrngspr_5v63_base_v057_signal,
    f13cr_f13_candle_range_structure_wickwt_21d_base_v058_signal,
    f13cr_f13_candle_range_structure_tailbar_21d_base_v059_signal,
    f13cr_f13_candle_range_structure_overnight_21d_base_v060_signal,
    f13cr_f13_candle_range_structure_expregime_21d_base_v061_signal,
    f13cr_f13_candle_range_structure_dojiflare_base_v062_signal,
    f13cr_f13_candle_range_structure_strongclstk_base_v063_signal,
    f13cr_f13_candle_range_structure_weakclstk_base_v064_signal,
    f13cr_f13_candle_range_structure_effort_21d_base_v065_signal,
    f13cr_f13_candle_range_structure_rngdirskew_21d_base_v066_signal,
    f13cr_f13_candle_range_structure_uwickz_21d_base_v067_signal,
    f13cr_f13_candle_range_structure_lwickz_21d_base_v068_signal,
    f13cr_f13_candle_range_structure_spintop_21d_base_v069_signal,
    f13cr_f13_candle_range_structure_trendday_21d_base_v070_signal,
    f13cr_f13_candle_range_structure_squeeze_5v63_base_v071_signal,
    f13cr_f13_candle_range_structure_brentropy_21d_base_v072_signal,
    f13cr_f13_candle_range_structure_clv_21d_base_v073_signal,
    f13cr_f13_candle_range_structure_revbar_21d_base_v074_signal,
    f13cr_f13_candle_range_structure_rngvolconf_21d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_CANDLE_RANGE_STRUCTURE_REGISTRY_001_075 = REGISTRY


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

    print("OK f13_candle_range_structure_base_001_075_claude: %d features pass" % n_features)
