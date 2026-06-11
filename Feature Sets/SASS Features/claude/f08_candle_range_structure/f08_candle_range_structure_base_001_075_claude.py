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


def _f08_dir(openp, close):
    return np.sign(close - openp)


def _f08_true_range(high, low, close):
    pc = close.shift(1)
    a = high - low
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _f08_clip01(s):
    return s.clip(lower=0.0, upper=1.0)


# ============================================================
# body/range ratio level (mean over a month) — candle decisiveness
def f08cr_f08_candle_range_structure_bodyrat_21d_base_v001_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    b = _mean(br, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body/range ratio z-scored vs its own 63d history (decisiveness extremity)
def f08cr_f08_candle_range_structure_bodyratz_63d_base_v002_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    b = _z(br, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick ratio level (mean over a month) — rejection from above
def f08cr_f08_candle_range_structure_uwick_21d_base_v003_signal(open, high, low, close):
    uw = _f08_upper_ratio(open, high, low, close)
    b = _mean(uw, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-wick ratio level (mean over a month) — buying support tails
def f08cr_f08_candle_range_structure_lwick_21d_base_v004_signal(open, high, low, close):
    lw = _f08_lower_ratio(open, high, low, close)
    b = _mean(lw, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wick asymmetry: lower minus upper wick ratio (net tail pressure), smoothed
def f08cr_f08_candle_range_structure_wickasym_21d_base_v005_signal(open, high, low, close):
    uw = _f08_upper_ratio(open, high, low, close)
    lw = _f08_lower_ratio(open, high, low, close)
    b = _mean(lw - uw, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close position within day range (mean over a month) — where buyers close
def f08cr_f08_candle_range_structure_closepos_21d_base_v006_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    b = _mean(cp, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-position z-scored vs its own 63d history
def f08cr_f08_candle_range_structure_closeposz_63d_base_v007_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    b = _z(cp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# doji frequency: smoothed softness of bodies (continuous indecision proxy) over a quarter
def f08cr_f08_candle_range_structure_dojifreq_21d_base_v008_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    soft = (0.25 - br).clip(lower=0) / 0.25
    b = soft.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-size z-score: today's absolute body vs its own 63d distribution
def f08cr_f08_candle_range_structure_bodyz_63d_base_v009_signal(open, high, low, close):
    ba = _f08_body_abs(open, close)
    b = _z(ba, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion vs body: range/body ratio (indecision wide-range days)
def f08cr_f08_candle_range_structure_rngvsbody_21d_base_v010_signal(open, high, low, close):
    rng = _f08_range(high, low)
    ba = _f08_body_abs(open, close)
    ratio = rng / ba.replace(0, np.nan)
    b = _mean(ratio, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-low range vs close (intraday volatility share), smoothed
def f08cr_f08_candle_range_structure_hlvsclose_21d_base_v011_signal(open, high, low, close):
    rng = _f08_range(high, low)
    ratio = rng / close.replace(0, np.nan)
    b = _mean(ratio, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# candle direction up-streak length (consecutive up-close-vs-open days)
def f08cr_f08_candle_range_structure_upstreak_base_v012_signal(open, close):
    up = (close > open).astype(float)
    grp = (up == 0).cumsum()
    streak = up.groupby(grp).cumsum()
    b = _ewm(streak, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# candle direction hit-rate: up-candle fraction over a quarter, smoothed continuous
def f08cr_f08_candle_range_structure_uphit_63d_base_v013_signal(open, close):
    up = (close > open).astype(float)
    hr = up.rolling(63, min_periods=21).mean() - 0.5
    b = _ewm(hr, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional run persistence: same-sign-as-prior rate over a quarter, smoothed
def f08cr_f08_candle_range_structure_dirpersist_63d_base_v014_signal(open, close):
    d = np.sign(close - open)
    same = (d * d.shift(1) > 0).astype(float)
    b = _ewm(same.rolling(63, min_periods=21).mean() - 0.5, 8)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body z-score weighted by direction (signed decisiveness)
def f08cr_f08_candle_range_structure_signbodyz_63d_base_v015_signal(open, high, low, close):
    ba = _f08_body_abs(open, close)
    z = _z(ba, 63)
    b = np.sign(close - open) * z
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick minus lower-wick scaled by body (rejection-vs-support net)
def f08cr_f08_candle_range_structure_wicknetbody_21d_base_v016_signal(open, high, low, close):
    uw = _f08_upper_wick(open, high, close)
    lw = _f08_lower_wick(open, low, close)
    ba = _f08_body_abs(open, close).replace(0, np.nan)
    ratio = (uw - lw) / ba
    b = _mean(ratio, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# closing-in-upper-third intensity: excess of close-pos above 2/3 over a quarter
def f08cr_f08_candle_range_structure_topclose_21d_base_v017_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    top = (cp - 0.6667).clip(lower=0)
    b = top.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# closing-in-lower-third intensity: excess of close-pos below 1/3 over a quarter
def f08cr_f08_candle_range_structure_botclose_21d_base_v018_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    bot = (0.3333 - cp).clip(lower=0)
    b = bot.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion: today's range vs its own 21d average (volatility burst)
def f08cr_f08_candle_range_structure_rngexp_21d_base_v019_signal(open, high, low, close):
    rng = _f08_range(high, low)
    avg = _mean(rng, 21).replace(0, np.nan)
    b = rng / avg - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range z-scored vs its own 63d history
def f08cr_f08_candle_range_structure_rngz_63d_base_v020_signal(open, high, low, close):
    rng = _f08_range(high, low)
    b = _z(rng, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body share of range trend: change in body-ratio mean over a quarter
def f08cr_f08_candle_range_structure_bodyratmom_63d_base_v021_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    m = _mean(br, 21)
    b = m - m.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marubozu intensity: excess body-ratio above 0.8 (decisive full-body) over a quarter
def f08cr_f08_candle_range_structure_marubozu_21d_base_v022_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    maru = (br - 0.8).clip(lower=0)
    b = maru.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-position dispersion (std of where price closes in range) over a quarter
def f08cr_f08_candle_range_structure_closeposdisp_63d_base_v023_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    b = _std(cp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick ratio z-scored vs its own 63d history (overhead-rejection spike)
def f08cr_f08_candle_range_structure_uwickz_63d_base_v024_signal(open, high, low, close):
    uw = _f08_upper_ratio(open, high, low, close)
    b = _z(uw, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-wick ratio z-scored vs its own 63d history (support-tail spike)
def f08cr_f08_candle_range_structure_lwickz_63d_base_v025_signal(open, high, low, close):
    lw = _f08_lower_ratio(open, high, low, close)
    b = _z(lw, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net candle direction × body-ratio (conviction-weighted direction), smoothed
def f08cr_f08_candle_range_structure_convdir_21d_base_v026_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    conv = np.sign(close - open) * br
    b = _mean(conv, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-expansion-without-body: wide range but small body (churn detector)
def f08cr_f08_candle_range_structure_churn_21d_base_v027_signal(open, high, low, close):
    rng = _f08_range(high, low)
    ba = _f08_body_abs(open, close)
    rngz = _z(rng, 63)
    brat = _f08_body_ratio(open, high, low, close)
    churn = rngz * (1.0 - brat)
    b = _mean(churn, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# open-position in range mean (where the day opens relative to its hi/lo)
def f08cr_f08_candle_range_structure_openpos_21d_base_v028_signal(open, high, low):
    op = _f08_open_pos(open, high, low)
    b = _mean(op, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday reversal tail: opposing-wick share (close pulled back from its extreme)
def f08cr_f08_candle_range_structure_intraeff_21d_base_v029_signal(open, high, low, close):
    rng = _f08_range(high, low).replace(0, np.nan)
    up = (close >= open)
    # for up candles the opposing tail is the upper wick (faded high); for down, lower wick
    uw = high - np.maximum(open, close)
    lw = np.minimum(open, close) - low
    opp = uw.where(up, lw)
    rev = opp / rng
    b = _mean(rev, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# direction-balance momentum: change in up-candle hit-rate over a quarter
def f08cr_f08_candle_range_structure_uphitmom_63d_base_v030_signal(open, close):
    up = (close > open).astype(float)
    hr = up.rolling(63, min_periods=21).mean()
    b = hr - hr.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# down-streak length (consecutive down candles), smoothed
def f08cr_f08_candle_range_structure_downstreak_base_v031_signal(open, close):
    dn = (close < open).astype(float)
    grp = (dn == 0).cumsum()
    streak = dn.groupby(grp).cumsum()
    b = _ewm(streak, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed streak: current up-streak minus current down-streak (running tug)
def f08cr_f08_candle_range_structure_streaknet_base_v032_signal(open, close):
    up = (close > open).astype(float)
    dn = (close < open).astype(float)
    ug = (up == 0).cumsum()
    dg = (dn == 0).cumsum()
    us = up.groupby(ug).cumsum()
    ds = dn.groupby(dg).cumsum()
    b = _ewm(us - ds, 15)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wick symmetry product: 4*upper*lower / range^2 (balanced two-sided shadows), smoothed
def f08cr_f08_candle_range_structure_wicktot_21d_base_v033_signal(open, high, low, close):
    uw = _f08_upper_ratio(open, high, low, close)
    lw = _f08_lower_ratio(open, high, low, close)
    sym = 4.0 * uw * lw
    b = _mean(sym, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-ratio asymmetry: skew of body-ratio distribution over a quarter
def f08cr_f08_candle_range_structure_bodyratskew_63d_base_v034_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    b = br.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-position skew over a quarter (asymmetry of intraday closes)
def f08cr_f08_candle_range_structure_closeposskew_63d_base_v035_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    b = cp.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion streak: consecutive days of range above its 21d avg
def f08cr_f08_candle_range_structure_rngexpstreak_base_v036_signal(open, high, low, close):
    rng = _f08_range(high, low)
    avg = _mean(rng, 21)
    exp = (rng > avg).astype(float)
    grp = (exp == 0).cumsum()
    streak = exp.groupby(grp).cumsum()
    b = _ewm(streak, 15)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range contraction intensity: how far range sits below its 63d avg, over a quarter
def f08cr_f08_candle_range_structure_rngcontr_21d_base_v037_signal(open, high, low, close):
    rng = _f08_range(high, low)
    avg = _mean(rng, 63).replace(0, np.nan)
    contr = (1.0 - rng / avg).clip(lower=0)
    b = contr.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap component of true range: how much TR exceeds the intraday range (overnight share)
def f08cr_f08_candle_range_structure_trshare_21d_base_v038_signal(open, high, low, close):
    tr = _f08_true_range(high, low, close)
    rng = _f08_range(high, low)
    gapshare = (tr - rng) / tr.replace(0, np.nan)
    b = _mean(gapshare, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wick asymmetry z-scored (extremity of net tail pressure)
def f08cr_f08_candle_range_structure_wickasymz_63d_base_v039_signal(open, high, low, close):
    uw = _f08_upper_ratio(open, high, low, close)
    lw = _f08_lower_ratio(open, high, low, close)
    b = _z(lw - uw, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-ratio percentile rank vs its own 252d history
def f08cr_f08_candle_range_structure_bodyratrank_252d_base_v040_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    m = _mean(br, 21)
    b = _rank(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional consistency: |mean(sign)| over a quarter (trend cohesion of candles)
def f08cr_f08_candle_range_structure_dircohesion_63d_base_v041_signal(open, close):
    d = np.sign(close - open)
    b = _ewm(_mean(d, 63).abs(), 8)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average signed body amplitude (close-open / close), smoothed
def f08cr_f08_candle_range_structure_bodyamp_21d_base_v042_signal(open, high, low, close):
    amp = (close - open) / close.replace(0, np.nan)
    b = _mean(amp, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body amplitude dispersion (intraday move volatility) over a quarter
def f08cr_f08_candle_range_structure_bodyampdisp_63d_base_v043_signal(open, high, low, close):
    amp = (close - open) / close.replace(0, np.nan)
    b = _std(amp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-low range trend: change in hl/close ratio over a quarter
def f08cr_f08_candle_range_structure_hlrngmom_63d_base_v044_signal(open, high, low, close):
    ratio = _f08_range(high, low) / close.replace(0, np.nan)
    m = _mean(ratio, 21)
    b = m - m.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick dominance intensity: (upper - body - lower) positive excess / range, quarter
def f08cr_f08_candle_range_structure_uwickdom_21d_base_v045_signal(open, high, low, close):
    uw = _f08_upper_wick(open, high, close)
    lw = _f08_lower_wick(open, low, close)
    ba = _f08_body_abs(open, close)
    rng = _f08_range(high, low).replace(0, np.nan)
    dom = (uw - lw - ba).clip(lower=0) / rng
    b = dom.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-wick dominance intensity: hammer-like support excess / range, over a quarter
def f08cr_f08_candle_range_structure_lwickdom_21d_base_v046_signal(open, high, low, close):
    uw = _f08_upper_wick(open, high, close)
    lw = _f08_lower_wick(open, low, close)
    ba = _f08_body_abs(open, close)
    rng = _f08_range(high, low).replace(0, np.nan)
    dom = (lw - uw - ba).clip(lower=0) / rng
    b = dom.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-position momentum: change in mean close-position over a month
def f08cr_f08_candle_range_structure_closeposmom_21d_base_v047_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    m = _mean(cp, 21)
    b = m - m.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed body-decisiveness shock (bounded change in body-ratio over a week)
def f08cr_f08_candle_range_structure_rngshock_tanh_base_v048_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    sm = _mean(br, 5)
    chg = sm - sm.shift(5)
    b = np.tanh(8.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# doji-cluster intensity: doji frequency × inverse body-ratio (deep indecision)
def f08cr_f08_candle_range_structure_dojiclust_21d_base_v049_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    freq = (br <= 0.15).astype(float).rolling(21, min_periods=10).mean()
    smallness = (1.0 - _mean(br, 21))
    b = freq * smallness
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# open-to-close drive vs full range, signed by where open sat (fade-from-open), smoothed
def f08cr_f08_candle_range_structure_closebias_21d_base_v050_signal(open, high, low, close):
    rng = _f08_range(high, low).replace(0, np.nan)
    # distance the close traveled away from the open, normalized by range
    drive = (close - open) / rng
    # weight by how extreme the open was (open near a wick gives stronger fade context)
    op = _f08_open_pos(open, high, low)
    signal = drive * (op - 0.5)
    b = _mean(signal, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-expansion vs body-expansion divergence (range grows, body flat)
def f08cr_f08_candle_range_structure_rngbodydiv_63d_base_v051_signal(open, high, low, close):
    rng = _f08_range(high, low)
    ba = _f08_body_abs(open, close)
    rz = _z(rng, 63)
    bz = _z(ba, 63)
    b = _mean(rz - bz, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bullish full-body intensity: body-ratio on up candles only, over a quarter
def f08cr_f08_candle_range_structure_bullmaru_21d_base_v052_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    up = (close > open)
    maru = br.where(up, 0.0)
    b = maru.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bearish full-body intensity: body-ratio on down candles only, over a quarter
def f08cr_f08_candle_range_structure_bearmaru_21d_base_v053_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    dn = (close < open)
    maru = br.where(dn, 0.0)
    b = maru.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body normalized by trailing ATR (today's conviction vs typical-day range), smoothed
def f08cr_f08_candle_range_structure_bodyvstr_21d_base_v054_signal(open, high, low, close):
    tr = _f08_true_range(high, low, close)
    atr = _mean(tr, 21).replace(0, np.nan)
    ratio = (close - open).abs() / atr
    b = _mean(ratio, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range/close ratio percentile rank vs its 252d history (relative wideness)
def f08cr_f08_candle_range_structure_rngrank_252d_base_v055_signal(open, high, low, close):
    ratio = _f08_range(high, low) / close.replace(0, np.nan)
    m = _mean(ratio, 21)
    b = _rank(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick to lower-wick log ratio, smoothed (tail balance, log-symmetric)
def f08cr_f08_candle_range_structure_wicklogratio_21d_base_v056_signal(open, high, low, close):
    uw = _f08_upper_wick(open, high, close).clip(lower=0) + 1e-6
    lw = _f08_lower_wick(open, low, close).clip(lower=0) + 1e-6
    lr = np.log(uw / lw)
    b = _mean(lr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# candle-body EWM (exponentially weighted decisiveness, fast-reacting)
def f08cr_f08_candle_range_structure_bodyratew_base_v057_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    b = _ewm(br, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-position EWM minus its slow EWM (intraday-bias displacement)
def f08cr_f08_candle_range_structure_closeposdisp_ew_base_v058_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    b = _ewm(cp, 10) - _ewm(cp, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-amplitude lag-1 autocorrelation over a quarter (intraday move persistence)
def f08cr_f08_candle_range_structure_dirflip_63d_base_v059_signal(open, high, low, close):
    amp = (close - open) / close.replace(0, np.nan)

    def _ac1(a):
        x = a[:-1]
        y = a[1:]
        if len(x) < 5:
            return np.nan
        sx = x.std()
        sy = y.std()
        if sx == 0 or sy == 0:
            return np.nan
        return np.corrcoef(x, y)[0, 1]
    b = amp.rolling(63, min_periods=30).apply(_ac1, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position of close weighted by range size (big-day conviction)
def f08cr_f08_candle_range_structure_bigdayclose_63d_base_v060_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close) - 0.5
    w = _z(_f08_range(high, low), 63)
    b = _mean(cp * w, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average body-to-range ratio on up days minus on down days (asymmetric decisiveness)
def f08cr_f08_candle_range_structure_updnbodyasym_63d_base_v061_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    up = (close > open)
    up_br = br.where(up)
    dn_br = br.where(~up)
    b = _mean(up_br, 63) - _mean(dn_br, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion magnitude on direction days (signed volatility burst)
def f08cr_f08_candle_range_structure_signedrngexp_21d_base_v062_signal(open, high, low, close):
    rng = _f08_range(high, low)
    avg = _mean(rng, 21).replace(0, np.nan)
    exp = rng / avg - 1.0
    b = _mean(np.sign(close - open) * exp, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-size coefficient-of-variation (instability of intraday conviction)
def f08cr_f08_candle_range_structure_bodycv_63d_base_v063_signal(open, high, low, close):
    ba = _f08_body_abs(open, close)
    m = _mean(ba, 63).replace(0, np.nan)
    sd = _std(ba, 63)
    b = sd / m
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# peak upper-wick ratio over a quarter (worst overhead-rejection day, smoothed)
def f08cr_f08_candle_range_structure_uwickfreq_21d_base_v064_signal(open, high, low, close):
    uw = _f08_upper_ratio(open, high, low, close)
    pk = uw.rolling(63, min_periods=21).max()
    b = _ewm(pk, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# peak lower-wick ratio over a quarter (deepest support-tail day, smoothed)
def f08cr_f08_candle_range_structure_lwickfreq_21d_base_v065_signal(open, high, low, close):
    lw = _f08_lower_ratio(open, high, low, close)
    pk = lw.rolling(63, min_periods=21).max()
    b = _ewm(pk, 10)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-position trend slope (OLS) over a quarter (drifting intraday bias)
def f08cr_f08_candle_range_structure_closeposslope_63d_base_v066_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)

    def _slope(a):
        x = np.arange(len(a), dtype=float)
        xm = x.mean()
        d = ((x - xm) ** 2).sum()
        if d == 0:
            return np.nan
        return ((x - xm) * (a - a.mean())).sum() / d
    b = cp.rolling(63, min_periods=21).apply(_slope, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-body share: today's body relative to its open-to-prior-close gap context
def f08cr_f08_candle_range_structure_intrarng_share_21d_base_v067_signal(open, high, low, close):
    intraday = (high - low)
    overnight = (open - close.shift(1)).abs()
    ratio = intraday / (intraday + overnight).replace(0, np.nan)
    b = _mean(ratio, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net wick (lower-upper) percentile rank vs its 252d history
def f08cr_f08_candle_range_structure_wicknetrank_252d_base_v068_signal(open, high, low, close):
    uw = _f08_upper_ratio(open, high, low, close)
    lw = _f08_lower_ratio(open, high, low, close)
    m = _mean(lw - uw, 21)
    b = _rank(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# trend-bar intensity: body-ratio excess above 0.5 (decisive-day strength), quarter
def f08cr_f08_candle_range_structure_trendbar_21d_base_v069_signal(open, high, low, close):
    br = _f08_body_ratio(open, high, low, close)
    tb = (br - 0.5).clip(lower=0)
    b = tb.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# candle efficiency ratio: net body sum vs total range sum over a quarter (path cleanliness)
def f08cr_f08_candle_range_structure_cleanmove_21d_base_v070_signal(open, high, low, close):
    body = (close - open)
    rng = _f08_range(high, low)
    net = body.rolling(63, min_periods=21).sum().abs()
    tot = rng.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = net / tot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# day-over-day range acceleration rank vs 126d history (range jerk posture)
def f08cr_f08_candle_range_structure_rngexprank_126d_base_v071_signal(open, high, low, close):
    rng = _f08_range(high, low)
    accel = rng / rng.shift(1).replace(0, np.nan)
    sm = _ewm(accel, 5)
    b = _rank(sm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shadow imbalance: larger wick over smaller wick (one-sided-tail index), smoothed
def f08cr_f08_candle_range_structure_indecision_21d_base_v072_signal(open, high, low, close):
    uw = _f08_upper_wick(open, high, close).clip(lower=0)
    lw = _f08_lower_wick(open, low, close).clip(lower=0)
    bigw = np.maximum(uw, lw)
    smallw = np.minimum(uw, lw) + 1e-6
    idx = bigw / smallw
    b = _mean(np.log1p(idx), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional body momentum: signed body-amplitude EWM (intraday drift)
def f08cr_f08_candle_range_structure_bodydrift_ew_base_v073_signal(open, high, low, close):
    amp = (close - open) / close.replace(0, np.nan)
    b = _ewm(amp, 15)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position entropy proxy: how spread closes are across thirds over a quarter
def f08cr_f08_candle_range_structure_closeposentropy_63d_base_v074_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    top = (cp >= 0.6667).astype(float).rolling(63, min_periods=21).mean()
    mid = ((cp > 0.3333) & (cp < 0.6667)).astype(float).rolling(63, min_periods=21).mean()
    bot = (cp <= 0.3333).astype(float).rolling(63, min_periods=21).mean()
    ent = -(top * np.log(top + 1e-9) + mid * np.log(mid + 1e-9) + bot * np.log(bot + 1e-9))
    result = ent
    return result.replace([np.inf, -np.inf], np.nan)


# net intraday pressure: (2*close_pos - 1) × body-ratio, smoothed (conviction-close)
def f08cr_f08_candle_range_structure_netpressure_21d_base_v075_signal(open, high, low, close):
    cp = _f08_close_pos(high, low, close)
    br = _f08_body_ratio(open, high, low, close)
    pressure = (2.0 * cp - 1.0) * br
    b = _mean(pressure, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08cr_f08_candle_range_structure_bodyrat_21d_base_v001_signal,
    f08cr_f08_candle_range_structure_bodyratz_63d_base_v002_signal,
    f08cr_f08_candle_range_structure_uwick_21d_base_v003_signal,
    f08cr_f08_candle_range_structure_lwick_21d_base_v004_signal,
    f08cr_f08_candle_range_structure_wickasym_21d_base_v005_signal,
    f08cr_f08_candle_range_structure_closepos_21d_base_v006_signal,
    f08cr_f08_candle_range_structure_closeposz_63d_base_v007_signal,
    f08cr_f08_candle_range_structure_dojifreq_21d_base_v008_signal,
    f08cr_f08_candle_range_structure_bodyz_63d_base_v009_signal,
    f08cr_f08_candle_range_structure_rngvsbody_21d_base_v010_signal,
    f08cr_f08_candle_range_structure_hlvsclose_21d_base_v011_signal,
    f08cr_f08_candle_range_structure_upstreak_base_v012_signal,
    f08cr_f08_candle_range_structure_uphit_63d_base_v013_signal,
    f08cr_f08_candle_range_structure_dirpersist_63d_base_v014_signal,
    f08cr_f08_candle_range_structure_signbodyz_63d_base_v015_signal,
    f08cr_f08_candle_range_structure_wicknetbody_21d_base_v016_signal,
    f08cr_f08_candle_range_structure_topclose_21d_base_v017_signal,
    f08cr_f08_candle_range_structure_botclose_21d_base_v018_signal,
    f08cr_f08_candle_range_structure_rngexp_21d_base_v019_signal,
    f08cr_f08_candle_range_structure_rngz_63d_base_v020_signal,
    f08cr_f08_candle_range_structure_bodyratmom_63d_base_v021_signal,
    f08cr_f08_candle_range_structure_marubozu_21d_base_v022_signal,
    f08cr_f08_candle_range_structure_closeposdisp_63d_base_v023_signal,
    f08cr_f08_candle_range_structure_uwickz_63d_base_v024_signal,
    f08cr_f08_candle_range_structure_lwickz_63d_base_v025_signal,
    f08cr_f08_candle_range_structure_convdir_21d_base_v026_signal,
    f08cr_f08_candle_range_structure_churn_21d_base_v027_signal,
    f08cr_f08_candle_range_structure_openpos_21d_base_v028_signal,
    f08cr_f08_candle_range_structure_intraeff_21d_base_v029_signal,
    f08cr_f08_candle_range_structure_uphitmom_63d_base_v030_signal,
    f08cr_f08_candle_range_structure_downstreak_base_v031_signal,
    f08cr_f08_candle_range_structure_streaknet_base_v032_signal,
    f08cr_f08_candle_range_structure_wicktot_21d_base_v033_signal,
    f08cr_f08_candle_range_structure_bodyratskew_63d_base_v034_signal,
    f08cr_f08_candle_range_structure_closeposskew_63d_base_v035_signal,
    f08cr_f08_candle_range_structure_rngexpstreak_base_v036_signal,
    f08cr_f08_candle_range_structure_rngcontr_21d_base_v037_signal,
    f08cr_f08_candle_range_structure_trshare_21d_base_v038_signal,
    f08cr_f08_candle_range_structure_wickasymz_63d_base_v039_signal,
    f08cr_f08_candle_range_structure_bodyratrank_252d_base_v040_signal,
    f08cr_f08_candle_range_structure_dircohesion_63d_base_v041_signal,
    f08cr_f08_candle_range_structure_bodyamp_21d_base_v042_signal,
    f08cr_f08_candle_range_structure_bodyampdisp_63d_base_v043_signal,
    f08cr_f08_candle_range_structure_hlrngmom_63d_base_v044_signal,
    f08cr_f08_candle_range_structure_uwickdom_21d_base_v045_signal,
    f08cr_f08_candle_range_structure_lwickdom_21d_base_v046_signal,
    f08cr_f08_candle_range_structure_closeposmom_21d_base_v047_signal,
    f08cr_f08_candle_range_structure_rngshock_tanh_base_v048_signal,
    f08cr_f08_candle_range_structure_dojiclust_21d_base_v049_signal,
    f08cr_f08_candle_range_structure_closebias_21d_base_v050_signal,
    f08cr_f08_candle_range_structure_rngbodydiv_63d_base_v051_signal,
    f08cr_f08_candle_range_structure_bullmaru_21d_base_v052_signal,
    f08cr_f08_candle_range_structure_bearmaru_21d_base_v053_signal,
    f08cr_f08_candle_range_structure_bodyvstr_21d_base_v054_signal,
    f08cr_f08_candle_range_structure_rngrank_252d_base_v055_signal,
    f08cr_f08_candle_range_structure_wicklogratio_21d_base_v056_signal,
    f08cr_f08_candle_range_structure_bodyratew_base_v057_signal,
    f08cr_f08_candle_range_structure_closeposdisp_ew_base_v058_signal,
    f08cr_f08_candle_range_structure_dirflip_63d_base_v059_signal,
    f08cr_f08_candle_range_structure_bigdayclose_63d_base_v060_signal,
    f08cr_f08_candle_range_structure_updnbodyasym_63d_base_v061_signal,
    f08cr_f08_candle_range_structure_signedrngexp_21d_base_v062_signal,
    f08cr_f08_candle_range_structure_bodycv_63d_base_v063_signal,
    f08cr_f08_candle_range_structure_uwickfreq_21d_base_v064_signal,
    f08cr_f08_candle_range_structure_lwickfreq_21d_base_v065_signal,
    f08cr_f08_candle_range_structure_closeposslope_63d_base_v066_signal,
    f08cr_f08_candle_range_structure_intrarng_share_21d_base_v067_signal,
    f08cr_f08_candle_range_structure_wicknetrank_252d_base_v068_signal,
    f08cr_f08_candle_range_structure_trendbar_21d_base_v069_signal,
    f08cr_f08_candle_range_structure_cleanmove_21d_base_v070_signal,
    f08cr_f08_candle_range_structure_rngexprank_126d_base_v071_signal,
    f08cr_f08_candle_range_structure_indecision_21d_base_v072_signal,
    f08cr_f08_candle_range_structure_bodydrift_ew_base_v073_signal,
    f08cr_f08_candle_range_structure_closeposentropy_63d_base_v074_signal,
    f08cr_f08_candle_range_structure_netpressure_21d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_CANDLE_RANGE_STRUCTURE_REGISTRY_001_075 = REGISTRY


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

    print("OK f08_candle_range_structure_base_001_075_claude: %d features pass" % n_features)
