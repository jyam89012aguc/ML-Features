import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _ewm(s, span):
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _slope(s, w):
    def _f(a):
        x = np.arange(len(a), dtype=float)
        xm = x.mean()
        d = ((x - xm) ** 2).sum()
        if d == 0:
            return np.nan
        return ((x - xm) * (a - a.mean())).sum() / d
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


# ===== folder domain primitives (candle / range structure) =====
def _f08_range(high, low):
    return (high - low)


def _f08_body(openp, close):
    return (close - openp)


def _f08_body_abs(openp, close):
    return (close - openp).abs()


def _f08_upper_wick(openp, high, close):
    return high - np.maximum(openp, close)


def _f08_lower_wick(openp, low, close):
    return np.minimum(openp, close) - low


def _f08_body_ratio(openp, high, low, close):
    rng = (high - low).replace(0, np.nan)
    return (close - openp).abs() / rng


def _f08_upper_ratio(openp, high, low, close):
    rng = (high - low).replace(0, np.nan)
    return (high - np.maximum(openp, close)) / rng


def _f08_lower_ratio(openp, high, low, close):
    rng = (high - low).replace(0, np.nan)
    return (np.minimum(openp, close) - low) / rng


def _f08_close_pos(high, low, close):
    rng = (high - low).replace(0, np.nan)
    return (close - low) / rng


def _f08_open_pos(openp, high, low):
    rng = (high - low).replace(0, np.nan)
    return (openp - low) / rng


def _f08_true_range(high, low, close):
    pc = close.shift(1)
    a = high - low
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


# ============================================================
# body-ratio EWM fast minus slow (decisiveness regime shift)
def f08cr_f08_candle_range_structure_bodyratregime_base_v076_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    b = _ewm(br, 8) - _ewm(br, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-ratio trend slope over a quarter (decisiveness drift)
def f08cr_f08_candle_range_structure_bodyratslope_63d_base_v077_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    sm = _mean(br, 5)
    b = _slope(sm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-position trend slope over a half-year (intraday-bias drift)
def f08cr_f08_candle_range_structure_closeposslope_126d_base_v078_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    sm = _mean(cp, 5)
    b = _slope(sm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick ratio trend slope over a quarter (rising overhead rejection)
def f08cr_f08_candle_range_structure_uwickslope_63d_base_v079_signal(open, high, low, close):
    uw = _f08_upper_ratio(open, high, low, close)
    sm = _mean(uw, 5)
    b = _slope(sm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-wick ratio trend slope over a quarter (rising support tails)
def f08cr_f08_candle_range_structure_lwickslope_63d_base_v080_signal(open, high, low, close):
    lw = _f08_lower_ratio(open, high, low, close)
    sm = _mean(lw, 5)
    b = _slope(sm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range/close ratio trend slope over a half-year (intraday-volatility drift)
def f08cr_f08_candle_range_structure_rngslope_126d_base_v081_signal(open, high, low, close):
    ratio = _f08_range(high, low) / close.replace(0, np.nan)
    sm = _mean(ratio, 5)
    b = _slope(sm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-ratio dispersion: std of daily body-ratio over a quarter (conviction instability)
def f08cr_f08_candle_range_structure_bodyratdisp_63d_base_v082_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    b = _std(br, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wick-asymmetry dispersion: std of (lower-upper wick) over a quarter
def f08cr_f08_candle_range_structure_wickasymdisp_63d_base_v083_signal(open, high, low, close):
    uw = _f08_upper_ratio(open, high, low, close)
    lw = _f08_lower_ratio(open, high, low, close)
    b = _std(lw - uw, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range coefficient of variation (range instability) over a half-year
def f08cr_f08_candle_range_structure_rngcv_126d_base_v084_signal(open, high, low, close):
    rng = _f08_range(high, low)
    m = _mean(rng, 126).replace(0, np.nan)
    sd = _std(rng, 126)
    b = sd / m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-position percentile rank vs 252d history (relative intraday strength)
def f08cr_f08_candle_range_structure_closeposrank_252d_base_v085_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    sm = _mean(cp, 21)
    b = _rank(sm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wick-asymmetry percentile rank vs 252d history
def f08cr_f08_candle_range_structure_wickasymrank_252d_base_v086_signal(open, high, low, close):
    uw = _f08_upper_ratio(open, high, low, close)
    lw = _f08_lower_ratio(open, high, low, close)
    sm = _mean(lw - uw, 21)
    b = _rank(sm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-size rank vs 126d history (relative conviction magnitude)
def f08cr_f08_candle_range_structure_bodysizerank_126d_base_v087_signal(open, high, low, close):
    ba = _f08_body_abs(open, close) / close.replace(0, np.nan)
    sm = _mean(ba, 21)
    b = _rank(sm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-candle range vs down-candle range asymmetry (where the action happens)
def f08cr_f08_candle_range_structure_updnrngasym_63d_base_v088_signal(open, high, low, close):
    rng = _f08_range(high, low) / close.replace(0, np.nan)
    up = (close > open)
    up_r = rng.where(up)
    dn_r = rng.where(~up)
    b = _mean(up_r, 63) - _mean(dn_r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-position on big-range days only (where price closes when it moves a lot)
def f08cr_f08_candle_range_structure_bigrngclose_63d_base_v089_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    rng = _f08_range(high, low)
    big = (rng >= _mean(rng, 63))
    sel = (cp - 0.5).where(big)
    b = _mean(sel, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-position on small-range days only (quiet-day intraday bias)
def f08cr_f08_candle_range_structure_smallrngclose_63d_base_v090_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    rng = _f08_range(high, low)
    small = (rng < _mean(rng, 63))
    sel = (cp - 0.5).where(small)
    b = _mean(sel, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive higher-high & higher-low structure rate (range-trend up), smoothed
def f08cr_f08_candle_range_structure_hhhlrate_63d_base_v091_signal(open, high, low, close):
    hh = (high > high.shift(1))
    hl = (low > low.shift(1))
    both = (hh & hl).astype(float)
    b = _ewm(both.rolling(63, min_periods=21).mean(), 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive lower-high & lower-low structure rate (range-trend down), smoothed
def f08cr_f08_candle_range_structure_lhllrate_63d_base_v092_signal(open, high, low, close):
    lh = (high < high.shift(1))
    ll = (low < low.shift(1))
    both = (lh & ll).astype(float)
    b = _ewm(both.rolling(63, min_periods=21).mean(), 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inside-bar rate: today's range fully inside yesterday's (compression), smoothed
def f08cr_f08_candle_range_structure_insidebar_63d_base_v093_signal(open, high, low, close):
    inside = ((high <= high.shift(1)) & (low >= low.shift(1))).astype(float)
    b = _ewm(inside.rolling(63, min_periods=21).mean(), 8)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# outside-bar rate: today engulfs yesterday's range (expansion), smoothed
def f08cr_f08_candle_range_structure_outsidebar_63d_base_v094_signal(open, high, low, close):
    outside = ((high >= high.shift(1)) & (low <= low.shift(1))).astype(float)
    b = _ewm(outside.rolling(63, min_periods=21).mean(), 8)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range autocorrelation lag-1 over a quarter (volatility clustering)
def f08cr_f08_candle_range_structure_rngautocorr_63d_base_v095_signal(open, high, low, close):
    rng = _f08_range(high, low) / close.replace(0, np.nan)

    def _ac1(a):
        x = a[:-1]
        y = a[1:]
        if len(x) < 5 or x.std() == 0 or y.std() == 0:
            return np.nan
        return np.corrcoef(x, y)[0, 1]
    b = rng.rolling(63, min_periods=30).apply(_ac1, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-ratio autocorrelation lag-1 over a quarter (decisiveness clustering)
def f08cr_f08_candle_range_structure_bodyautocorr_63d_base_v096_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)

    def _ac1(a):
        x = a[:-1]
        y = a[1:]
        if len(x) < 5 or x.std() == 0 or y.std() == 0:
            return np.nan
        return np.corrcoef(x, y)[0, 1]
    b = br.rolling(63, min_periods=30).apply(_ac1, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-fill structure: open-to-close recovers the overnight gap (fade rate), smoothed
def f08cr_f08_candle_range_structure_gapfade_63d_base_v097_signal(open, high, low, close):
    gap = open - close.shift(1)
    intraday = close - open
    fade = (np.sign(gap) * np.sign(intraday) < 0).astype(float)
    b = _ewm(fade.rolling(63, min_periods=21).mean() - 0.5, 8)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight vs intraday range share trend (where vol migrates), slope
def f08cr_f08_candle_range_structure_overnightshare_126d_base_v098_signal(open, high, low, close):
    intraday = (high - low)
    overnight = (open - close.shift(1)).abs()
    share = overnight / (overnight + intraday).replace(0, np.nan)
    sm = _mean(share, 21)
    b = _slope(sm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body skew over a quarter weighted toward extreme bodies (fat-tailed conviction)
def f08cr_f08_candle_range_structure_bodyfat_63d_base_v099_signal(open, high, low, close):
    amp = (close - open) / close.replace(0, np.nan)
    b = amp.rolling(63, min_periods=21).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range kurtosis over a quarter (range-jump fat tails)
def f08cr_f08_candle_range_structure_rngkurt_63d_base_v100_signal(open, high, low, close):
    rng = _f08_range(high, low) / close.replace(0, np.nan)
    b = rng.rolling(63, min_periods=21).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net body sign × range z (conviction scaled by how unusual the range is)
def f08cr_f08_candle_range_structure_convrngz_21d_base_v101_signal(open, high, low, close):
    sgn = np.sign(close - open)
    rz = _z(_f08_range(high, low), 63)
    b = _mean(sgn * rz, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick minus lower-wick on up days only (failed-rally tails)
def f08cr_f08_candle_range_structure_uprejtail_63d_base_v102_signal(open, high, low, close):
    uw = _f08_upper_ratio(open, high, low, close)
    lw = _f08_lower_ratio(open, high, low, close)
    up = (close > open)
    sel = (uw - lw).where(up)
    b = _mean(sel, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-wick minus upper-wick on down days only (dip-buying tails)
def f08cr_f08_candle_range_structure_dnsupptail_63d_base_v103_signal(open, high, low, close):
    uw = _f08_upper_ratio(open, high, low, close)
    lw = _f08_lower_ratio(open, high, low, close)
    dn = (close < open)
    sel = (lw - uw).where(dn)
    b = _mean(sel, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-to-range ratio EWM volatility (vol-of-decisiveness)
def f08cr_f08_candle_range_structure_bodyratvov_base_v104_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    dev = (br - _ewm(br, 21)).abs()
    b = _ewm(dev, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range EWM-volatility (vol-of-range), normalized by range level
def f08cr_f08_candle_range_structure_rngvov_base_v105_signal(open, high, low, close):
    rng = _f08_range(high, low) / close.replace(0, np.nan)
    dev = (rng - _ewm(rng, 21)).abs()
    b = _ewm(dev, 21) / _ewm(rng, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of range above the open (intraday upside exploration), smoothed
def f08cr_f08_candle_range_structure_upexplore_21d_base_v106_signal(open, high, low, close):
    up_room = (high - open)
    rng = _f08_range(high, low).replace(0, np.nan)
    frac = up_room / rng
    b = _mean(frac, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# two-sided exploration balance: 4*uproom*dnroom/range^2 (both directions probed), smoothed
def f08cr_f08_candle_range_structure_dnexplore_21d_base_v107_signal(open, high, low, close):
    rng = _f08_range(high, low).replace(0, np.nan)
    up_room = (high - open) / rng
    dn_room = (open - low) / rng
    bal = 4.0 * up_room * dn_room
    b = _mean(bal, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday exploration asymmetry: upside-room minus downside-room z, smoothed
def f08cr_f08_candle_range_structure_exploreasym_63d_base_v108_signal(open, high, low, close):
    rng = _f08_range(high, low).replace(0, np.nan)
    up_room = (high - open) / rng
    dn_room = (open - low) / rng
    b = _z(_mean(up_room - dn_room, 5), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close beats prior high rate (intraday breakout closes), smoothed
def f08cr_f08_candle_range_structure_closeoverph_63d_base_v109_signal(open, high, low, close):
    over = (close > high.shift(1)).astype(float)
    b = _ewm(over.rolling(63, min_periods=21).mean(), 8)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close beneath prior low rate (intraday breakdown closes), smoothed
def f08cr_f08_candle_range_structure_closeunderpl_63d_base_v110_signal(open, high, low, close):
    under = (close < low.shift(1)).astype(float)
    b = _ewm(under.rolling(63, min_periods=21).mean(), 8)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-position spread between wide-range and narrow-range days (vol-conditioned bias)
def f08cr_f08_candle_range_structure_dirvolbias_63d_base_v111_signal(open, high, low, close):
    rng = _f08_range(high, low)
    cp = _f08_close_pos(high, low, close)
    med = rng.rolling(63, min_periods=21).median()
    wide = (rng >= med)
    b = _mean(cp.where(wide), 63) - _mean(cp.where(~wide), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# typical-price position vs range (HLC mean position), smoothed
def f08cr_f08_candle_range_structure_typpricepos_21d_base_v112_signal(open, high, low, close):
    rng = _f08_range(high, low).replace(0, np.nan)
    typ = (high + low + close) / 3.0
    pos = (typ - low) / rng
    b = _mean(pos, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted-close position (OHLC weighted price within range), smoothed
def f08cr_f08_candle_range_structure_wclosepos_21d_base_v113_signal(open, high, low, close):
    rng = _f08_range(high, low).replace(0, np.nan)
    wc = (open + high + low + 2.0 * close) / 5.0
    pos = (wc - low) / rng
    b = _mean(pos - 0.5, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body midpoint drift vs range midpoint (where the body centers), smoothed
def f08cr_f08_candle_range_structure_bodymid_21d_base_v114_signal(open, high, low, close):
    rng = _f08_range(high, low).replace(0, np.nan)
    bodymid = (open + close) / 2.0
    rngmid = (high + low) / 2.0
    pos = (bodymid - rngmid) / rng
    b = _mean(pos, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of the month with body in upper half of range (top-heavy bodies)
def f08cr_f08_candle_range_structure_topbody_63d_base_v115_signal(open, high, low, close):
    rng = _f08_range(high, low).replace(0, np.nan)
    bodymid = (open + close) / 2.0
    pos = (bodymid - low) / rng
    excess = (pos - 0.5).clip(lower=0)
    b = excess.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range entropy across three magnitude buckets over a quarter (range-regime spread)
def f08cr_f08_candle_range_structure_rngentropy_63d_base_v116_signal(open, high, low, close):
    rng = _f08_range(high, low) / close.replace(0, np.nan)
    r = _rank(rng, 63) + 0.5
    hi = (r >= 0.6667).astype(float).rolling(63, min_periods=21).mean()
    mi = ((r > 0.3333) & (r < 0.6667)).astype(float).rolling(63, min_periods=21).mean()
    lo = (r <= 0.3333).astype(float).rolling(63, min_periods=21).mean()
    ent = -(hi * np.log(hi + 1e-9) + mi * np.log(mi + 1e-9) + lo * np.log(lo + 1e-9))
    result = _ewm(ent, 8)
    return result.replace([np.inf, -np.inf], np.nan)


# signed body magnitude EWM scaled by inverse vol (risk-adjusted candle drift)
def f08cr_f08_candle_range_structure_riskadjbody_base_v117_signal(open, high, low, close):
    amp = (close - open) / close.replace(0, np.nan)
    vol = _std(amp, 63).replace(0, np.nan)
    b = _ewm(amp, 21) / vol
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of decisive up closes (close in top quartile & up candle), quarter
def f08cr_f08_candle_range_structure_strongup_63d_base_v118_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    up = (close > open)
    strong = (cp - 0.75).clip(lower=0).where(up, 0.0)
    b = strong.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of decisive down closes (close in bottom quartile & down candle), quarter
def f08cr_f08_candle_range_structure_strongdn_63d_base_v119_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    dn = (close < open)
    strong = (0.25 - cp).clip(lower=0).where(dn, 0.0)
    b = strong.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# magnitude gap-continuation: signed gap x intraday body, normalized by close, smoothed
def f08cr_f08_candle_range_structure_gapcont_63d_base_v120_signal(open, high, low, close):
    gap = (open - close.shift(1)) / close.shift(1).replace(0, np.nan)
    intraday = (close - open) / open.replace(0, np.nan)
    prod = np.sign(gap) * intraday
    b = _mean(prod, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# candle body relative to 5-day cumulative body (short-term conviction concentration)
def f08cr_f08_candle_range_structure_bodyconc_21d_base_v121_signal(open, high, low, close):
    ba = _f08_body_abs(open, close)
    cum5 = ba.rolling(5, min_periods=3).sum().replace(0, np.nan)
    conc = ba / cum5
    b = _mean(conc, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range relative to 5-day cumulative range (range concentration in one day)
def f08cr_f08_candle_range_structure_rngconc_21d_base_v122_signal(open, high, low, close):
    rng = _f08_range(high, low)
    cum5 = rng.rolling(5, min_periods=3).sum().replace(0, np.nan)
    conc = rng / cum5
    b = _mean(conc, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wick-asymmetry EWM minus slow EWM (tail-pressure displacement)
def f08cr_f08_candle_range_structure_wickasymdisp_ew_base_v123_signal(open, high, low, close):
    uw = _f08_upper_ratio(open, high, low, close)
    lw = _f08_lower_ratio(open, high, low, close)
    a = lw - uw
    b = _ewm(a, 10) - _ewm(a, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of range traversed by the body's path relative to net (intrabar churn)
def f08cr_f08_candle_range_structure_intrabarchurn_21d_base_v124_signal(open, high, low, close):
    rng = _f08_range(high, low)
    ba = _f08_body_abs(open, close)
    churn = (rng - ba) / rng.replace(0, np.nan)
    b = _z(_mean(churn, 5), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional candle agreement with prior day (continuation), magnitude-weighted
def f08cr_f08_candle_range_structure_contmag_63d_base_v125_signal(open, high, low, close):
    amp = (close - open) / close.replace(0, np.nan)
    agree = np.sign(amp) * np.sign(amp.shift(1)) * (amp.abs() + amp.shift(1).abs())
    b = _mean(agree, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion clustering: streak-weighted range z, EWM
def f08cr_f08_candle_range_structure_rngexpcluster_base_v126_signal(open, high, low, close):
    rng = _f08_range(high, low)
    rz = _z(rng, 63)
    pos = (rz > 0).astype(float)
    grp = (pos == 0).cumsum()
    streak = pos.groupby(grp).cumsum()
    b = _ewm(rz * streak, 15)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick to body ratio (overhead pressure per unit conviction), smoothed
def f08cr_f08_candle_range_structure_uwickbody_21d_base_v127_signal(open, high, low, close):
    uw = _f08_upper_wick(open, high, close).clip(lower=0)
    ba = _f08_body_abs(open, close).replace(0, np.nan)
    ratio = uw / ba
    b = _mean(np.log1p(ratio), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-wick to body ratio (support pressure per unit conviction), smoothed
def f08cr_f08_candle_range_structure_lwickbody_21d_base_v128_signal(open, high, low, close):
    lw = _f08_lower_wick(open, low, close).clip(lower=0)
    ba = _f08_body_abs(open, close).replace(0, np.nan)
    ratio = lw / ba
    b = _mean(np.log1p(ratio), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-position momentum over a quarter (slow intraday-strength acceleration-as-level)
def f08cr_f08_candle_range_structure_closeposmom_63d_base_v129_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    m = _mean(cp, 21)
    b = m - m.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-amplitude trend slope over a quarter (drift in signed intraday move)
def f08cr_f08_candle_range_structure_bodyampslope_63d_base_v130_signal(open, high, low, close):
    amp = (close - open) / close.replace(0, np.nan)
    sm = _mean(amp, 5)
    b = _slope(sm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close vs body-midpoint within range (did close finish above the body center), smoothed
def f08cr_f08_candle_range_structure_closetyppremium_21d_base_v131_signal(open, high, low, close):
    rng = _f08_range(high, low).replace(0, np.nan)
    cp = (close - low) / rng
    bodymid = ((open + close) / 2.0 - low) / rng
    b = _mean(cp - bodymid, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of doji-to-trend transitions over a quarter (indecision-to-decision flips)
def f08cr_f08_candle_range_structure_dojibreak_63d_base_v132_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    was_doji = (br.shift(1) <= 0.2)
    now_trend = (br >= 0.6)
    trans = (was_doji & now_trend).astype(float)
    b = _ewm(trans.rolling(63, min_periods=21).mean(), 8)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-range ratio harmonic mean over a month (penalizes indecisive days)
def f08cr_f08_candle_range_structure_bodyharm_21d_base_v133_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close).clip(lower=1e-4)
    inv = 1.0 / br
    b = 1.0 / _mean(inv, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest single-day range in last quarter relative to typical (range outlier presence)
def f08cr_f08_candle_range_structure_rngmaxrel_63d_base_v134_signal(open, high, low, close):
    rng = _f08_range(high, low) / close.replace(0, np.nan)
    mx = rng.rolling(63, min_periods=21).max()
    md = _mean(rng, 63).replace(0, np.nan)
    b = mx / md
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smallest single-day range in last quarter relative to typical (compression presence)
def f08cr_f08_candle_range_structure_rngminrel_63d_base_v135_signal(open, high, low, close):
    rng = _f08_range(high, low) / close.replace(0, np.nan)
    mn = rng.rolling(63, min_periods=21).min()
    md = _mean(rng, 63).replace(0, np.nan)
    b = mn / md
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed close-position weighted by body-ratio, EWM (fast conviction-close)
def f08cr_f08_candle_range_structure_convclose_ew_base_v136_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    br = _f08_body_ratio(open, high, low, close)
    sig = (2.0 * cp - 1.0) * br
    b = _ewm(sig, 12)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net wick pressure normalized by range, ranked vs 126d history
def f08cr_f08_candle_range_structure_wickpressrank_126d_base_v137_signal(open, high, low, close):
    uw = _f08_upper_wick(open, high, close)
    lw = _f08_lower_wick(open, low, close)
    rng = _f08_range(high, low).replace(0, np.nan)
    net = (lw - uw) / rng
    sm = _mean(net, 21)
    b = _rank(sm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of trend continuation candles (close beyond prior close in body dir), quarter
def f08cr_f08_candle_range_structure_trendcont_63d_base_v138_signal(open, high, low, close):
    cont = (np.sign(close - close.shift(1)) == np.sign(close - open)).astype(float)
    b = _ewm(cont.rolling(63, min_periods=21).mean() - 0.5, 8)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-ratio weighted by relative volume of range (range-conviction product), z
def f08cr_f08_candle_range_structure_rngconvz_63d_base_v139_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    rng = _f08_range(high, low)
    rngrel = rng / _mean(rng, 63).replace(0, np.nan)
    prod = br * rngrel
    b = _z(_mean(prod, 5), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-position dispersion change over a quarter (intraday-bias stabilizing/destabilizing)
def f08cr_f08_candle_range_structure_closedispmom_63d_base_v140_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    d = _std(cp, 63)
    b = d - d.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of bodies larger than the prior body (escalating conviction), smoothed
def f08cr_f08_candle_range_structure_bodyescalate_63d_base_v141_signal(open, high, low, close):
    ba = _f08_body_abs(open, close)
    esc = (ba > ba.shift(1)).astype(float)
    b = _ewm(esc.rolling(63, min_periods=21).mean() - 0.5, 8)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of ranges larger than the prior range (escalating volatility), smoothed
def f08cr_f08_candle_range_structure_rngescalate_63d_base_v142_signal(open, high, low, close):
    rng = _f08_range(high, low)
    esc = (rng > rng.shift(1)).astype(float)
    b = _ewm(esc.rolling(63, min_periods=21).mean() - 0.5, 8)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick ratio EWM displacement (overhead-rejection regime shift)
def f08cr_f08_candle_range_structure_uwickregime_base_v143_signal(open, high, low, close):
    uw = _f08_upper_ratio(open, high, low, close)
    b = _ewm(uw, 8) - _ewm(uw, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-wick ratio EWM displacement (support-tail regime shift)
def f08cr_f08_candle_range_structure_lwickregime_base_v144_signal(open, high, low, close):
    lw = _f08_lower_ratio(open, high, low, close)
    b = _ewm(lw, 8) - _ewm(lw, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range vs body spread z over a half-year (sustained churn vs trend posture)
def f08cr_f08_candle_range_structure_churnposture_126d_base_v145_signal(open, high, low, close):
    rng = _f08_range(high, low)
    ba = _f08_body_abs(open, close)
    spread = (rng - ba) / close.replace(0, np.nan)
    b = _z(_mean(spread, 21), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-position skew-adjusted bias (mean minus median over a quarter)
def f08cr_f08_candle_range_structure_closeposskewbias_63d_base_v146_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    m = _mean(cp, 63)
    med = cp.rolling(63, min_periods=21).median()
    b = m - med
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# two-day body reversal rate: large opposite bodies back-to-back (whipsaw), smoothed
def f08cr_f08_candle_range_structure_whipsaw_63d_base_v147_signal(open, high, low, close):
    amp = (close - open) / close.replace(0, np.nan)
    big = amp.abs() > _std(amp, 63)
    opp = (np.sign(amp) * np.sign(amp.shift(1)) < 0)
    whip = (big & big.shift(1) & opp).astype(float)
    b = _ewm(whip.rolling(63, min_periods=21).mean(), 8)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-ratio percentile within its own day-of-range bucket trend, ranked
def f08cr_f08_candle_range_structure_bodyrelrank_126d_base_v148_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    b = _rank(_ewm(br, 10), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday range center of mass: how high the typical price sits, slope over quarter
def f08cr_f08_candle_range_structure_typposslope_63d_base_v149_signal(open, high, low, close):
    rng = _f08_range(high, low).replace(0, np.nan)
    typ = (high + low + close) / 3.0
    pos = (typ - low) / rng
    sm = _mean(pos, 5)
    b = _slope(sm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite candle-strength: signed body minus net overhead-rejection (wick-driven), smoothed
def f08cr_f08_candle_range_structure_candlestrength_21d_base_v150_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    uw = _f08_upper_ratio(open, high, low, close)
    lw = _f08_lower_ratio(open, high, low, close)
    comp = np.sign(close - open) * br - (uw - lw)
    b = _z(_mean(comp, 5), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08cr_f08_candle_range_structure_bodyratregime_base_v076_signal,
    f08cr_f08_candle_range_structure_bodyratslope_63d_base_v077_signal,
    f08cr_f08_candle_range_structure_closeposslope_126d_base_v078_signal,
    f08cr_f08_candle_range_structure_uwickslope_63d_base_v079_signal,
    f08cr_f08_candle_range_structure_lwickslope_63d_base_v080_signal,
    f08cr_f08_candle_range_structure_rngslope_126d_base_v081_signal,
    f08cr_f08_candle_range_structure_bodyratdisp_63d_base_v082_signal,
    f08cr_f08_candle_range_structure_wickasymdisp_63d_base_v083_signal,
    f08cr_f08_candle_range_structure_rngcv_126d_base_v084_signal,
    f08cr_f08_candle_range_structure_closeposrank_252d_base_v085_signal,
    f08cr_f08_candle_range_structure_wickasymrank_252d_base_v086_signal,
    f08cr_f08_candle_range_structure_bodysizerank_126d_base_v087_signal,
    f08cr_f08_candle_range_structure_updnrngasym_63d_base_v088_signal,
    f08cr_f08_candle_range_structure_bigrngclose_63d_base_v089_signal,
    f08cr_f08_candle_range_structure_smallrngclose_63d_base_v090_signal,
    f08cr_f08_candle_range_structure_hhhlrate_63d_base_v091_signal,
    f08cr_f08_candle_range_structure_lhllrate_63d_base_v092_signal,
    f08cr_f08_candle_range_structure_insidebar_63d_base_v093_signal,
    f08cr_f08_candle_range_structure_outsidebar_63d_base_v094_signal,
    f08cr_f08_candle_range_structure_rngautocorr_63d_base_v095_signal,
    f08cr_f08_candle_range_structure_bodyautocorr_63d_base_v096_signal,
    f08cr_f08_candle_range_structure_gapfade_63d_base_v097_signal,
    f08cr_f08_candle_range_structure_overnightshare_126d_base_v098_signal,
    f08cr_f08_candle_range_structure_bodyfat_63d_base_v099_signal,
    f08cr_f08_candle_range_structure_rngkurt_63d_base_v100_signal,
    f08cr_f08_candle_range_structure_convrngz_21d_base_v101_signal,
    f08cr_f08_candle_range_structure_uprejtail_63d_base_v102_signal,
    f08cr_f08_candle_range_structure_dnsupptail_63d_base_v103_signal,
    f08cr_f08_candle_range_structure_bodyratvov_base_v104_signal,
    f08cr_f08_candle_range_structure_rngvov_base_v105_signal,
    f08cr_f08_candle_range_structure_upexplore_21d_base_v106_signal,
    f08cr_f08_candle_range_structure_dnexplore_21d_base_v107_signal,
    f08cr_f08_candle_range_structure_exploreasym_63d_base_v108_signal,
    f08cr_f08_candle_range_structure_closeoverph_63d_base_v109_signal,
    f08cr_f08_candle_range_structure_closeunderpl_63d_base_v110_signal,
    f08cr_f08_candle_range_structure_dirvolbias_63d_base_v111_signal,
    f08cr_f08_candle_range_structure_typpricepos_21d_base_v112_signal,
    f08cr_f08_candle_range_structure_wclosepos_21d_base_v113_signal,
    f08cr_f08_candle_range_structure_bodymid_21d_base_v114_signal,
    f08cr_f08_candle_range_structure_topbody_63d_base_v115_signal,
    f08cr_f08_candle_range_structure_rngentropy_63d_base_v116_signal,
    f08cr_f08_candle_range_structure_riskadjbody_base_v117_signal,
    f08cr_f08_candle_range_structure_strongup_63d_base_v118_signal,
    f08cr_f08_candle_range_structure_strongdn_63d_base_v119_signal,
    f08cr_f08_candle_range_structure_gapcont_63d_base_v120_signal,
    f08cr_f08_candle_range_structure_bodyconc_21d_base_v121_signal,
    f08cr_f08_candle_range_structure_rngconc_21d_base_v122_signal,
    f08cr_f08_candle_range_structure_wickasymdisp_ew_base_v123_signal,
    f08cr_f08_candle_range_structure_intrabarchurn_21d_base_v124_signal,
    f08cr_f08_candle_range_structure_contmag_63d_base_v125_signal,
    f08cr_f08_candle_range_structure_rngexpcluster_base_v126_signal,
    f08cr_f08_candle_range_structure_uwickbody_21d_base_v127_signal,
    f08cr_f08_candle_range_structure_lwickbody_21d_base_v128_signal,
    f08cr_f08_candle_range_structure_closeposmom_63d_base_v129_signal,
    f08cr_f08_candle_range_structure_bodyampslope_63d_base_v130_signal,
    f08cr_f08_candle_range_structure_closetyppremium_21d_base_v131_signal,
    f08cr_f08_candle_range_structure_dojibreak_63d_base_v132_signal,
    f08cr_f08_candle_range_structure_bodyharm_21d_base_v133_signal,
    f08cr_f08_candle_range_structure_rngmaxrel_63d_base_v134_signal,
    f08cr_f08_candle_range_structure_rngminrel_63d_base_v135_signal,
    f08cr_f08_candle_range_structure_convclose_ew_base_v136_signal,
    f08cr_f08_candle_range_structure_wickpressrank_126d_base_v137_signal,
    f08cr_f08_candle_range_structure_trendcont_63d_base_v138_signal,
    f08cr_f08_candle_range_structure_rngconvz_63d_base_v139_signal,
    f08cr_f08_candle_range_structure_closedispmom_63d_base_v140_signal,
    f08cr_f08_candle_range_structure_bodyescalate_63d_base_v141_signal,
    f08cr_f08_candle_range_structure_rngescalate_63d_base_v142_signal,
    f08cr_f08_candle_range_structure_uwickregime_base_v143_signal,
    f08cr_f08_candle_range_structure_lwickregime_base_v144_signal,
    f08cr_f08_candle_range_structure_churnposture_126d_base_v145_signal,
    f08cr_f08_candle_range_structure_closeposskewbias_63d_base_v146_signal,
    f08cr_f08_candle_range_structure_whipsaw_63d_base_v147_signal,
    f08cr_f08_candle_range_structure_bodyrelrank_126d_base_v148_signal,
    f08cr_f08_candle_range_structure_typposslope_63d_base_v149_signal,
    f08cr_f08_candle_range_structure_candlestrength_21d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_CANDLE_RANGE_STRUCTURE_REGISTRY_076_150 = REGISTRY


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

    print("OK f08_candle_range_structure_base_076_150_claude: %d features pass" % n_features)
