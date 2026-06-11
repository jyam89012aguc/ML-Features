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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


# ===== folder domain primitives (candle / range structure) =====
def _f13_range(high, low):
    # full intraday range (true daily range proxy, unadjusted)
    return (high - low)


def _f13_body(open_, close):
    return (close - open_)


def _f13_body_abs(open_, close):
    return (close - open_).abs()


def _f13_upper_wick(open_, high, close):
    top = np.maximum(open_, close)
    return (high - top)


def _f13_lower_wick(open_, low, close):
    bot = np.minimum(open_, close)
    return (bot - low)


def _f13_body_ratio(open_, high, low, close):
    rng = (high - low).replace(0, np.nan)
    return (close - open_).abs() / rng


def _f13_close_in_range(high, low, close):
    rng = (high - low).replace(0, np.nan)
    return (close - low) / rng


def _f13_upper_ratio(open_, high, low, close):
    rng = (high - low).replace(0, np.nan)
    return (high - np.maximum(open_, close)) / rng


def _f13_lower_ratio(open_, high, low, close):
    rng = (high - low).replace(0, np.nan)
    return (np.minimum(open_, close) - low) / rng


def _f13_doji(open_, high, low, close, thresh=0.1):
    return (_f13_body_ratio(open_, high, low, close) < thresh).astype(float)


# ============================================================
# body fill ratio (|close-open|/range) — conviction of the candle
def f13cr_f13_candle_range_structure_bodyratio_1d_base_v001_signal(open, high, low, close):
    b = _f13_body_ratio(open, high, low, close)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5d mean body-fill ratio (sustained directional conviction)
def f13cr_f13_candle_range_structure_bodyratio_5d_base_v002_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    b = _mean(br, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean body-fill ratio, z-scored vs its own 63d history
def f13cr_f13_candle_range_structure_bodyratio_21d_base_v003_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    m = _mean(br, 21)
    b = _z(m, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-in-range (where close sits in the day's bar) — buying pressure
def f13cr_f13_candle_range_structure_cir_1d_base_v004_signal(high, low, close):
    b = _f13_close_in_range(high, low, close) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5d mean close-in-range (sustained close strength)
def f13cr_f13_candle_range_structure_cir_5d_base_v005_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    b = _mean(cir, 5) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean close-in-range z-scored vs 63d history
def f13cr_f13_candle_range_structure_cir_21d_base_v006_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    b = _z(_mean(cir, 21), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick ratio (rejection from highs) — distribution/selling tails
def f13cr_f13_candle_range_structure_uwick_1d_base_v007_signal(open, high, low, close):
    b = _f13_upper_ratio(open, high, low, close)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5d mean upper-wick ratio (persistent overhead supply)
def f13cr_f13_candle_range_structure_uwick_5d_base_v008_signal(open, high, low, close):
    uw = _f13_upper_ratio(open, high, low, close)
    b = _mean(uw, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-wick ratio (rejection from lows) — demand/support tails
def f13cr_f13_candle_range_structure_lwick_1d_base_v009_signal(open, high, low, close):
    b = _f13_lower_ratio(open, high, low, close)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 5d mean lower-wick ratio (persistent support buying)
def f13cr_f13_candle_range_structure_lwick_5d_base_v010_signal(open, high, low, close):
    lw = _f13_lower_ratio(open, high, low, close)
    b = _mean(lw, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wick asymmetry: lower-wick minus upper-wick ratio (demand vs supply)
def f13cr_f13_candle_range_structure_wickskew_1d_base_v011_signal(open, high, low, close):
    lw = _f13_lower_ratio(open, high, low, close)
    uw = _f13_upper_ratio(open, high, low, close)
    b = lw - uw
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean wick asymmetry (regime of tail buying vs selling)
def f13cr_f13_candle_range_structure_wickskew_21d_base_v012_signal(open, high, low, close):
    lw = _f13_lower_ratio(open, high, low, close)
    uw = _f13_upper_ratio(open, high, low, close)
    b = _mean(lw - uw, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion: today's range vs its 21d average (range breakout)
def f13cr_f13_candle_range_structure_rngexp_21d_base_v013_signal(high, low):
    rng = _f13_range(high, low)
    b = rng / _mean(rng, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion vs 63d average (medium-term volatility shock)
def f13cr_f13_candle_range_structure_rngexp_63d_base_v014_signal(high, low):
    rng = _f13_range(high, low)
    b = rng / _mean(rng, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion vs body: big range but small body = indecision/churn
def f13cr_f13_candle_range_structure_rngvsbody_5d_base_v015_signal(open, high, low, close):
    rng = _f13_range(high, low)
    body = _f13_body_abs(open, close)
    ratio = rng / body.replace(0, np.nan)
    b = _mean(ratio.clip(upper=20.0), 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# doji-ness over 21d: avg (1 - body ratio) blended with hard doji count (indecision)
def f13cr_f13_candle_range_structure_dojifreq_21d_base_v016_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    soft = (1.0 - br).clip(lower=0)
    d = (br < 0.1).astype(float)
    b = _mean(soft, 21) + 0.5 * _mean(d, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# doji-ness over 63d (longer indecision regime, magnitude-weighted)
def f13cr_f13_candle_range_structure_dojifreq_63d_base_v017_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    soft = (1.0 - br).clip(lower=0)
    d = (br < 0.1).astype(float)
    b = _mean(soft, 63) + 0.5 * _mean(d, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# climactic candle: large range x high volume (exhaustion/capitulation thrust)
def f13cr_f13_candle_range_structure_climax_5d_base_v018_signal(high, low, volume):
    rng = _f13_range(high, low)
    rz = _z(rng, 63)
    vz = _z(volume, 63)
    clim = rz.clip(lower=0) * vz.clip(lower=0)
    b = _mean(clim, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capitulation candle: wide-range down day closing near low on heavy volume
def f13cr_f13_candle_range_structure_capit_5d_base_v019_signal(open, high, low, close, volume):
    rng = _f13_range(high, low)
    cir = _f13_close_in_range(high, low, close)
    down = (close < open).astype(float)
    rz = _z(rng, 63).clip(lower=0)
    vz = _z(volume, 63).clip(lower=0)
    cap = down * (1.0 - cir) * rz * vz
    b = _mean(cap, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exhaustion-up candle: wide-range up day closing near high on heavy volume (blowoff)
def f13cr_f13_candle_range_structure_exhup_5d_base_v020_signal(open, high, low, close, volume):
    rng = _f13_range(high, low)
    cir = _f13_close_in_range(high, low, close)
    up = (close > open).astype(float)
    rz = _z(rng, 63).clip(lower=0)
    vz = _z(volume, 63).clip(lower=0)
    ex = up * cir * rz * vz
    b = _mean(ex, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# pin-bar / hammer strength over 21d: lower-wick-heavy small-body candles (magnitude)
def f13cr_f13_candle_range_structure_hammerfreq_21d_base_v021_signal(open, high, low, close):
    lw = _f13_lower_ratio(open, high, low, close)
    br = _f13_body_ratio(open, high, low, close)
    score = (lw * (1.0 - br)).where(lw > br, 0.0)
    b = _mean(score, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shooting-star strength over 21d: upper-wick-heavy small-body candles (magnitude)
def f13cr_f13_candle_range_structure_starfreq_21d_base_v022_signal(open, high, low, close):
    uw = _f13_upper_ratio(open, high, low, close)
    br = _f13_body_ratio(open, high, low, close)
    score = (uw * (1.0 - br)).where(uw > br, 0.0)
    b = _mean(score, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marubozu strength over 21d: full-body candles weighted by body-fill (magnitude)
def f13cr_f13_candle_range_structure_marufreq_21d_base_v023_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    score = (br - 0.6).clip(lower=0)
    b = _mean(score, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional marubozu skew: signed body-fill on strong-body days (21d)
def f13cr_f13_candle_range_structure_maruskew_21d_base_v024_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    strong = (br - 0.6).clip(lower=0)
    signed = np.sign(close - open) * strong
    b = _mean(signed, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true-range normalized by close (intraday volatility level)
def f13cr_f13_candle_range_structure_atrpct_21d_base_v025_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    b = _mean(tr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR%/63d z-scored — intraday range regime extremity
def f13cr_f13_candle_range_structure_atrpctz_63d_base_v026_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    m = _mean(tr, 21)
    b = _z(m, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range contraction streak x depth: consecutive below-avg days scaled by compression
def f13cr_f13_candle_range_structure_contractstrk_base_v027_signal(high, low):
    rng = _f13_range(high, low)
    avg = _mean(rng, 21)
    below = (rng < avg).astype(float)
    grp = (below == 0).cumsum()
    streak = below.groupby(grp).cumsum()
    depth = (1.0 - rng / avg.replace(0, np.nan)).clip(lower=0)
    b = streak * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion streak x magnitude: consecutive above-avg days scaled by overshoot
def f13cr_f13_candle_range_structure_expandstrk_base_v028_signal(high, low):
    rng = _f13_range(high, low)
    avg = _mean(rng, 21)
    above = (rng > avg).astype(float)
    grp = (above == 0).cumsum()
    streak = above.groupby(grp).cumsum()
    over = (rng / avg.replace(0, np.nan) - 1.0).clip(lower=0)
    b = streak * over
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-in-range momentum: change over 5 days (pressure shift)
def f13cr_f13_candle_range_structure_cirmom_5d_base_v029_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    sm = _mean(cir, 5)
    b = sm - sm.shift(5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-fill ratio rank over 126d (where current conviction sits historically)
def f13cr_f13_candle_range_structure_bodyrank_126d_base_v030_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    sm = _mean(br, 5)
    b = _rank(sm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spinning-top strength (21d): small body with balanced two-sided wicks (magnitude)
def f13cr_f13_candle_range_structure_spintopfreq_21d_base_v031_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    uw = _f13_upper_ratio(open, high, low, close)
    lw = _f13_lower_ratio(open, high, low, close)
    balance = np.minimum(uw, lw)
    score = (1.0 - br).clip(lower=0) * balance
    b = _mean(score, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net wick balance weighted by range size (big-bar tails matter more)
def f13cr_f13_candle_range_structure_wickwt_21d_base_v032_signal(open, high, low, close):
    lw = _f13_lower_wick(open, low, close)
    uw = _f13_upper_wick(open, high, close)
    net = (lw - uw) / close.replace(0, np.nan)
    b = _mean(net, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position of the body midpoint within the bar (body location)
def f13cr_f13_candle_range_structure_bodyloc_5d_base_v033_signal(open, high, low, close):
    mid = (open + close) / 2.0
    rng = _f13_range(high, low).replace(0, np.nan)
    loc = (mid - low) / rng
    b = _mean(loc, 5) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday return (close vs open) normalized by range — clean directional thrust
def f13cr_f13_candle_range_structure_thrust_5d_base_v034_signal(open, high, low, close):
    body = _f13_body(open, close)
    rng = _f13_range(high, low).replace(0, np.nan)
    thr = body / rng
    b = _mean(thr, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of close-in-range over 21d (consistency of close placement)
def f13cr_f13_candle_range_structure_cirdisp_21d_base_v035_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    b = _std(cir, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vs-body churn z: high-range/low-body indecision regime (21d z)
def f13cr_f13_candle_range_structure_churnz_21d_base_v036_signal(open, high, low, close):
    rng = _f13_range(high, low)
    body = _f13_body_abs(open, close)
    churn = rng / body.replace(0, np.nan)
    sm = _mean(churn.clip(upper=20.0), 21)
    b = _z(sm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# climactic-day intensity over 21d: range x volume excess over their 63d medians
def f13cr_f13_candle_range_structure_climaxcnt_21d_base_v037_signal(high, low, volume):
    rng = _f13_range(high, low)
    rmed = rng.rolling(63, min_periods=21).median().replace(0, np.nan)
    vmed = volume.rolling(63, min_periods=21).median().replace(0, np.nan)
    rex = (rng / rmed - 1.0).clip(lower=0)
    vex = (volume / vmed - 1.0).clip(lower=0)
    b = _mean(rex * vex, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capitulation intensity over 21d: down weak-close wide-range heavy-volume magnitude
def f13cr_f13_candle_range_structure_capitcnt_21d_base_v038_signal(open, high, low, close, volume):
    rng = _f13_range(high, low)
    cir = _f13_close_in_range(high, low, close)
    rmed = rng.rolling(63, min_periods=21).median().replace(0, np.nan)
    vmed = volume.rolling(63, min_periods=21).median().replace(0, np.nan)
    down = (close < open).astype(float)
    weak = (0.4 - cir).clip(lower=0)
    rex = (rng / rmed - 1.0).clip(lower=0)
    vex = (volume / vmed - 1.0).clip(lower=0)
    b = _mean(down * weak * rex * vex, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted close-in-range (heavy-volume days vote on pressure)
def f13cr_f13_candle_range_structure_vwcir_21d_base_v039_signal(high, low, close, volume):
    cir = _f13_close_in_range(high, low, close)
    num = (cir * volume).rolling(21, min_periods=10).sum()
    den = volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = num / den - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-adjusted body: today's close change relative to gap-extended true range (5d)
def f13cr_f13_candle_range_structure_truebody_5d_base_v040_signal(open, high, low, close):
    tr = np.maximum(high, close.shift(1)) - np.minimum(low, close.shift(1))
    body = (close - close.shift(1)).abs()
    ratio = body / tr.replace(0, np.nan)
    b = _mean(ratio, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inside-bar compression over 21d: how far today's range nests inside yesterday's
def f13cr_f13_candle_range_structure_insidebar_21d_base_v041_signal(high, low):
    rng = (high - low)
    prng = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    inside = ((high < high.shift(1)) & (low > low.shift(1)))
    shrink = (1.0 - rng / prng).clip(lower=0).where(inside, 0.0)
    b = _mean(shrink, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# outside-bar expansion over 21d: how far today's range engulfs yesterday's
def f13cr_f13_candle_range_structure_outsidebar_21d_base_v042_signal(high, low):
    rng = (high - low)
    prng = (high.shift(1) - low.shift(1)).replace(0, np.nan)
    outside = ((high > high.shift(1)) & (low < low.shift(1)))
    grow = (rng / prng - 1.0).clip(lower=0).where(outside, 0.0)
    b = _mean(grow, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bullish-engulfing strength over 21d: up body engulfs prior down body (magnitude)
def f13cr_f13_candle_range_structure_bullengulf_21d_base_v043_signal(open, close):
    eng = ((close > open) & (close.shift(1) < open.shift(1)) &
           (close > open.shift(1)) & (open < close.shift(1)))
    pbody = (open.shift(1) - close.shift(1)).abs().replace(0, np.nan)
    mag = ((close - open) / pbody).where(eng, 0.0)
    b = _mean(mag, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bearish-engulfing strength over 21d (magnitude)
def f13cr_f13_candle_range_structure_bearengulf_21d_base_v044_signal(open, close):
    eng = ((close < open) & (close.shift(1) > open.shift(1)) &
           (close < open.shift(1)) & (open > close.shift(1)))
    pbody = (close.shift(1) - open.shift(1)).abs().replace(0, np.nan)
    mag = ((open - close) / pbody).where(eng, 0.0)
    b = _mean(mag, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range skewness over 21d: are big-range days dominated by spikes (fat tails)
def f13cr_f13_candle_range_structure_rngskew_21d_base_v045_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    b = tr.rolling(21, min_periods=10).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range kurtosis over 63d: peakedness / outlier-bar tendency
def f13cr_f13_candle_range_structure_rngkurt_63d_base_v046_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    b = tr.rolling(63, min_periods=21).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest single-bar range share of 21d total range (concentration)
def f13cr_f13_candle_range_structure_rngconc_21d_base_v047_signal(high, low):
    rng = _f13_range(high, low)
    mx = rng.rolling(21, min_periods=10).max()
    tot = rng.rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = mx / tot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-fill consistency: negative dispersion of body ratio (steady conviction)
def f13cr_f13_candle_range_structure_bodyconsist_21d_base_v048_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    b = -_std(br, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net thrust accumulation: sum of body/range over 21d (directional dominance)
def f13cr_f13_candle_range_structure_netthrust_21d_base_v049_signal(open, high, low, close):
    body = _f13_body(open, close)
    rng = _f13_range(high, low).replace(0, np.nan)
    thr = body / rng
    b = thr.rolling(21, min_periods=10).sum() / 21.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-day close-in-range vs down-day close-in-range spread (asymmetric pressure)
def f13cr_f13_candle_range_structure_ciras_63d_base_v050_signal(open, high, low, close):
    cir = _f13_close_in_range(high, low, close)
    up = cir.where(close > open)
    dn = cir.where(close < open)
    b = up.rolling(63, min_periods=21).mean() - dn.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion with up-direction: bull range thrust (21d mean)
def f13cr_f13_candle_range_structure_bullexp_21d_base_v051_signal(open, high, low, close):
    rng = _f13_range(high, low)
    rz = _z(rng, 63).clip(lower=0)
    up = (close > open).astype(float)
    b = _mean(rz * up, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion with down-direction: bear range thrust (21d mean)
def f13cr_f13_candle_range_structure_bearexp_21d_base_v052_signal(open, high, low, close):
    rng = _f13_range(high, low)
    rz = _z(rng, 63).clip(lower=0)
    dn = (close < open).astype(float)
    b = _mean(rz * dn, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wick-dominance: total wick length vs total range over 21d (rejection regime)
def f13cr_f13_candle_range_structure_wickdom_21d_base_v053_signal(open, high, low, close):
    uw = _f13_upper_wick(open, high, close)
    lw = _f13_lower_wick(open, low, close)
    rng = _f13_range(high, low)
    wd = (uw + lw) / rng.replace(0, np.nan)
    b = _mean(wd, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick rank over 126d (extreme overhead rejection)
def f13cr_f13_candle_range_structure_uwickrank_126d_base_v054_signal(open, high, low, close):
    uw = _f13_upper_ratio(open, high, low, close)
    sm = _mean(uw, 5)
    b = _rank(sm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-wick rank over 126d (extreme support buying)
def f13cr_f13_candle_range_structure_lwickrank_126d_base_v055_signal(open, high, low, close):
    lw = _f13_lower_ratio(open, high, low, close)
    sm = _mean(lw, 5)
    b = _rank(sm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-expansion-from-squeeze: range exp now after a contraction (squeeze break)
def f13cr_f13_candle_range_structure_squeezebreak_base_v056_signal(high, low):
    rng = _f13_range(high, low)
    avg = _mean(rng, 21)
    minr = rng.rolling(21, min_periods=10).min()
    compressed = (minr / avg.replace(0, np.nan))
    cur = rng / avg.replace(0, np.nan)
    b = cur * (1.0 - compressed.clip(upper=1.0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight gap absorbed: intraday move that fades the gap direction (5d)
def f13cr_f13_candle_range_structure_gapfade_5d_base_v057_signal(open, close):
    gap = open / close.shift(1).replace(0, np.nan) - 1.0
    intraday = close / open.replace(0, np.nan) - 1.0
    fade = -np.sign(gap) * intraday
    b = _mean(fade, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# thrust confirmed by volume z (single composite, 5d smooth)
def f13cr_f13_candle_range_structure_thrustvol_5d_base_v058_signal(open, high, low, close, volume):
    body = _f13_body(open, close)
    rng = _f13_range(high, low).replace(0, np.nan)
    thr = body / rng
    vz = _z(volume, 63)
    b = _mean(thr * vz, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range autocorrelation (1-lag) over 63d: range clustering/persistence
def f13cr_f13_candle_range_structure_rngautocorr_63d_base_v059_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    def _ac(a):
        a = a[~np.isnan(a)]
        if len(a) < 10:
            return np.nan
        s0 = a[:-1]
        s1 = a[1:]
        if np.std(s0) == 0 or np.std(s1) == 0:
            return np.nan
        return np.corrcoef(s0, s1)[0, 1]
    b = tr.rolling(63, min_periods=30).apply(_ac, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# doji-after-trend: small-body-ness weighted by preceding directional run (reversal)
def f13cr_f13_candle_range_structure_dojirev_21d_base_v060_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    small = (1.0 - br).clip(lower=0)
    body = _f13_body(open, close)
    run = np.sign(body).rolling(5, min_periods=3).mean().abs()
    b = _mean(small * run, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-to-range ratio drift: 21d body ratio change over a quarter (regime drift)
def f13cr_f13_candle_range_structure_bodydrift_63d_base_v061_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    sm = _mean(br, 21)
    b = sm - sm.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-volume close-in-range minus low-volume (smart-money close strength)
def f13cr_f13_candle_range_structure_hvcir_63d_base_v062_signal(high, low, close, volume):
    cir = _f13_close_in_range(high, low, close)
    vmed = volume.rolling(63, min_periods=21).median()
    hv = cir.where(volume > vmed)
    lv = cir.where(volume <= vmed)
    b = hv.rolling(63, min_periods=21).mean() - lv.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion momentum: 5d range avg vs 21d range avg ratio (acceleration)
def f13cr_f13_candle_range_structure_rngmomratio_base_v063_signal(high, low):
    rng = _f13_range(high, low)
    b = _mean(rng, 5) / _mean(rng, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range efficiency: net 21d close move vs total path of daily ranges
def f13cr_f13_candle_range_structure_rngeffic_21d_base_v064_signal(high, low, close):
    net = (close - close.shift(21)).abs()
    path = _f13_range(high, low).rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = net / path
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tight-range depth over 21d: magnitude of compression below median range
def f13cr_f13_candle_range_structure_tightrun_21d_base_v065_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    med = tr.rolling(63, min_periods=21).median().replace(0, np.nan)
    tight = (0.6 - tr / med).clip(lower=0)
    b = _mean(tight, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wide-range overshoot over 21d (volatility-shock magnitude above 2x median)
def f13cr_f13_candle_range_structure_widebarcnt_21d_base_v066_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    med = tr.rolling(63, min_periods=21).median().replace(0, np.nan)
    wide = (tr / med - 2.0).clip(lower=0)
    b = _mean(wide, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# strong-close intensity over 21d: magnitude of close above 0.7 of bar (count-friendly)
def f13cr_f13_candle_range_structure_closehighfreq_21d_base_v067_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    nh = (cir - 0.7).clip(lower=0)
    b = _mean(nh, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weak-close intensity over 21d: magnitude of close below 0.3 of bar (distress)
def f13cr_f13_candle_range_structure_closelowfreq_21d_base_v068_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    nl = (0.3 - cir).clip(lower=0)
    b = _mean(nl, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intrabar reversal: distance from extreme reached back to close (round-trip, 5d)
def f13cr_f13_candle_range_structure_intrabar_5d_base_v069_signal(open, high, low, close):
    rng = _f13_range(high, low).replace(0, np.nan)
    # if up day, how far it pulled back from the high; if down, bounce off the low
    up = (close >= open)
    pullback = ((high - close) / rng).where(up, (close - low) / rng)
    signed = np.sign(close - open) * pullback
    b = _mean(signed, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# failed-thrust intensity over 21d: wide up-bar upper-wick rejection magnitude
def f13cr_f13_candle_range_structure_failthrust_21d_base_v070_signal(open, high, low, close):
    rng = _f13_range(high, low)
    rz = _z(rng, 63).clip(lower=0)
    uw = _f13_upper_ratio(open, high, low, close)
    up = (close > open).astype(float)
    score = rz * (uw - 0.4).clip(lower=0) * up
    b = _mean(score, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# effort-vs-result: volume per unit of range, z-scored (churn = high effort, low result)
def f13cr_f13_candle_range_structure_effortresult_21d_base_v071_signal(high, low, close, volume):
    rng = _f13_range(high, low) / close.replace(0, np.nan)
    eff = volume / rng.replace(0, np.nan)
    b = _z(_mean(eff, 5), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body ratio interaction with volume z: conviction confirmed by volume (5d)
def f13cr_f13_candle_range_structure_bodyvolconf_5d_base_v072_signal(open, high, low, close, volume):
    br = _f13_body_ratio(open, high, low, close)
    vz = _z(volume, 63)
    b = _mean(br * vz, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# push-vs-tail: net body thrust minus wick-skew (body push vs tail rejection, 21d)
def f13cr_f13_candle_range_structure_pushvstail_21d_base_v073_signal(open, high, low, close):
    body = _f13_body(open, close)
    rng = _f13_range(high, low).replace(0, np.nan)
    thr = _mean(body / rng, 21)
    lw = _f13_lower_ratio(open, high, low, close)
    uw = _f13_upper_ratio(open, high, low, close)
    skew = _mean(lw - uw, 21)
    b = thr - skew
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# climactic-range percentile rank over 252d (where today's range sits long-term)
def f13cr_f13_candle_range_structure_rngpctl_252d_base_v074_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    b = _rank(tr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capitulation-then-recovery: heavy-volume weak-close day followed by strong close (21d)
def f13cr_f13_candle_range_structure_capitrecov_21d_base_v075_signal(open, high, low, close, volume):
    rng = _f13_range(high, low)
    cir = _f13_close_in_range(high, low, close)
    vz = _z(volume, 63)
    cap = ((cir < 0.25) & (close < open) & (vz > 1.0)).astype(float)
    strong_next = (cir.shift(-1) > 0.6).astype(float)
    sig = (cap * strong_next).fillna(0.0)
    b = _mean(sig * (rng / _mean(rng, 21).replace(0, np.nan)), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f13cr_f13_candle_range_structure_bodyratio_1d_base_v001_signal,
    f13cr_f13_candle_range_structure_bodyratio_5d_base_v002_signal,
    f13cr_f13_candle_range_structure_bodyratio_21d_base_v003_signal,
    f13cr_f13_candle_range_structure_cir_1d_base_v004_signal,
    f13cr_f13_candle_range_structure_cir_5d_base_v005_signal,
    f13cr_f13_candle_range_structure_cir_21d_base_v006_signal,
    f13cr_f13_candle_range_structure_uwick_1d_base_v007_signal,
    f13cr_f13_candle_range_structure_uwick_5d_base_v008_signal,
    f13cr_f13_candle_range_structure_lwick_1d_base_v009_signal,
    f13cr_f13_candle_range_structure_lwick_5d_base_v010_signal,
    f13cr_f13_candle_range_structure_wickskew_1d_base_v011_signal,
    f13cr_f13_candle_range_structure_wickskew_21d_base_v012_signal,
    f13cr_f13_candle_range_structure_rngexp_21d_base_v013_signal,
    f13cr_f13_candle_range_structure_rngexp_63d_base_v014_signal,
    f13cr_f13_candle_range_structure_rngvsbody_5d_base_v015_signal,
    f13cr_f13_candle_range_structure_dojifreq_21d_base_v016_signal,
    f13cr_f13_candle_range_structure_dojifreq_63d_base_v017_signal,
    f13cr_f13_candle_range_structure_climax_5d_base_v018_signal,
    f13cr_f13_candle_range_structure_capit_5d_base_v019_signal,
    f13cr_f13_candle_range_structure_exhup_5d_base_v020_signal,
    f13cr_f13_candle_range_structure_hammerfreq_21d_base_v021_signal,
    f13cr_f13_candle_range_structure_starfreq_21d_base_v022_signal,
    f13cr_f13_candle_range_structure_marufreq_21d_base_v023_signal,
    f13cr_f13_candle_range_structure_maruskew_21d_base_v024_signal,
    f13cr_f13_candle_range_structure_atrpct_21d_base_v025_signal,
    f13cr_f13_candle_range_structure_atrpctz_63d_base_v026_signal,
    f13cr_f13_candle_range_structure_contractstrk_base_v027_signal,
    f13cr_f13_candle_range_structure_expandstrk_base_v028_signal,
    f13cr_f13_candle_range_structure_cirmom_5d_base_v029_signal,
    f13cr_f13_candle_range_structure_bodyrank_126d_base_v030_signal,
    f13cr_f13_candle_range_structure_spintopfreq_21d_base_v031_signal,
    f13cr_f13_candle_range_structure_wickwt_21d_base_v032_signal,
    f13cr_f13_candle_range_structure_bodyloc_5d_base_v033_signal,
    f13cr_f13_candle_range_structure_thrust_5d_base_v034_signal,
    f13cr_f13_candle_range_structure_cirdisp_21d_base_v035_signal,
    f13cr_f13_candle_range_structure_churnz_21d_base_v036_signal,
    f13cr_f13_candle_range_structure_climaxcnt_21d_base_v037_signal,
    f13cr_f13_candle_range_structure_capitcnt_21d_base_v038_signal,
    f13cr_f13_candle_range_structure_vwcir_21d_base_v039_signal,
    f13cr_f13_candle_range_structure_truebody_5d_base_v040_signal,
    f13cr_f13_candle_range_structure_insidebar_21d_base_v041_signal,
    f13cr_f13_candle_range_structure_outsidebar_21d_base_v042_signal,
    f13cr_f13_candle_range_structure_bullengulf_21d_base_v043_signal,
    f13cr_f13_candle_range_structure_bearengulf_21d_base_v044_signal,
    f13cr_f13_candle_range_structure_rngskew_21d_base_v045_signal,
    f13cr_f13_candle_range_structure_rngkurt_63d_base_v046_signal,
    f13cr_f13_candle_range_structure_rngconc_21d_base_v047_signal,
    f13cr_f13_candle_range_structure_bodyconsist_21d_base_v048_signal,
    f13cr_f13_candle_range_structure_netthrust_21d_base_v049_signal,
    f13cr_f13_candle_range_structure_ciras_63d_base_v050_signal,
    f13cr_f13_candle_range_structure_bullexp_21d_base_v051_signal,
    f13cr_f13_candle_range_structure_bearexp_21d_base_v052_signal,
    f13cr_f13_candle_range_structure_wickdom_21d_base_v053_signal,
    f13cr_f13_candle_range_structure_uwickrank_126d_base_v054_signal,
    f13cr_f13_candle_range_structure_lwickrank_126d_base_v055_signal,
    f13cr_f13_candle_range_structure_squeezebreak_base_v056_signal,
    f13cr_f13_candle_range_structure_gapfade_5d_base_v057_signal,
    f13cr_f13_candle_range_structure_thrustvol_5d_base_v058_signal,
    f13cr_f13_candle_range_structure_rngautocorr_63d_base_v059_signal,
    f13cr_f13_candle_range_structure_dojirev_21d_base_v060_signal,
    f13cr_f13_candle_range_structure_bodydrift_63d_base_v061_signal,
    f13cr_f13_candle_range_structure_hvcir_63d_base_v062_signal,
    f13cr_f13_candle_range_structure_rngmomratio_base_v063_signal,
    f13cr_f13_candle_range_structure_rngeffic_21d_base_v064_signal,
    f13cr_f13_candle_range_structure_tightrun_21d_base_v065_signal,
    f13cr_f13_candle_range_structure_widebarcnt_21d_base_v066_signal,
    f13cr_f13_candle_range_structure_closehighfreq_21d_base_v067_signal,
    f13cr_f13_candle_range_structure_closelowfreq_21d_base_v068_signal,
    f13cr_f13_candle_range_structure_intrabar_5d_base_v069_signal,
    f13cr_f13_candle_range_structure_failthrust_21d_base_v070_signal,
    f13cr_f13_candle_range_structure_effortresult_21d_base_v071_signal,
    f13cr_f13_candle_range_structure_bodyvolconf_5d_base_v072_signal,
    f13cr_f13_candle_range_structure_pushvstail_21d_base_v073_signal,
    f13cr_f13_candle_range_structure_rngpctl_252d_base_v074_signal,
    f13cr_f13_candle_range_structure_capitrecov_21d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_CANDLE_RANGE_STRUCTURE_REGISTRY_001_075 = REGISTRY


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

    print("OK f13_candle_range_structure_base_001_075_claude: %d features pass" % n_features)
