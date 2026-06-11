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


def _f13_true_range(high, low, close):
    pc = close.shift(1)
    a = (high - low)
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


# ============================================================
# body-fill ratio rank over 252d (long-horizon conviction percentile)
def f13cr_f13_candle_range_structure_bodyrank_252d_base_v076_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    sm = _mean(br, 5)
    b = _rank(sm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-in-range smoothed by EMA (persistent buying pressure)
def f13cr_f13_candle_range_structure_cirema_21d_base_v077_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    b = cir.ewm(span=21, min_periods=10).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-in-range displacement: cir minus its slow EMA (pressure shift vs baseline)
def f13cr_f13_candle_range_structure_cirdisp_63d_base_v078_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    sm = _mean(cir, 5)
    b = sm - cir.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick ratio z-scored vs 126d history (extreme overhead rejection)
def f13cr_f13_candle_range_structure_uwickz_126d_base_v079_signal(open, high, low, close):
    uw = _f13_upper_ratio(open, high, low, close)
    sm = _mean(uw, 5)
    b = _z(sm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-wick ratio z-scored vs 126d history (extreme support buying)
def f13cr_f13_candle_range_structure_lwickz_126d_base_v080_signal(open, high, low, close):
    lw = _f13_lower_ratio(open, high, low, close)
    sm = _mean(lw, 5)
    b = _z(sm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wick-skew momentum: change in 21d wick skew over a month (tail-regime shift)
def f13cr_f13_candle_range_structure_wickskewmom_21d_base_v081_signal(open, high, low, close):
    lw = _f13_lower_ratio(open, high, low, close)
    uw = _f13_upper_ratio(open, high, low, close)
    sk = _mean(lw - uw, 21)
    b = sk - sk.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true-range / price (gap-inclusive intraday vol level, 21d)
def f13cr_f13_candle_range_structure_truatr_21d_base_v082_signal(high, low, close):
    tr = _f13_true_range(high, low, close) / close.replace(0, np.nan)
    b = _mean(tr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true-range vs intraday-range ratio: how much gap inflates the bar (21d)
def f13cr_f13_candle_range_structure_gaprng_21d_base_v083_signal(high, low, close):
    tr = _f13_true_range(high, low, close)
    rng = _f13_range(high, low).replace(0, np.nan)
    b = _mean((tr / rng).clip(upper=10.0), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion ratio rank over 126d (where current expansion sits)
def f13cr_f13_candle_range_structure_rngexprank_126d_base_v084_signal(high, low):
    rng = _f13_range(high, low)
    ex = rng / _mean(rng, 21).replace(0, np.nan)
    b = _rank(ex, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-to-body ratio z-scored over 63d (indecision vs conviction extremity)
def f13cr_f13_candle_range_structure_rngbodyz_63d_base_v085_signal(open, high, low, close):
    rng = _f13_range(high, low)
    body = _f13_body_abs(open, close)
    r = (rng / body.replace(0, np.nan)).clip(upper=20.0)
    b = _z(_mean(r, 5), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body ratio vs its 63d average (conviction relative to recent norm)
def f13cr_f13_candle_range_structure_bodyrel_63d_base_v086_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    sm = _mean(br, 5)
    b = sm - _mean(br, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-in-range x range-expansion: strong close on a wide bar (thrust quality, 5d)
def f13cr_f13_candle_range_structure_strongwide_5d_base_v087_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    rng = _f13_range(high, low)
    rz = _z(rng, 63).clip(lower=0)
    b = _mean((cir - 0.5) * rz, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick x range-expansion: rejection on wide bars (distribution, 5d)
def f13cr_f13_candle_range_structure_wickwide_5d_base_v088_signal(open, high, low, close):
    uw = _f13_upper_ratio(open, high, low, close)
    rng = _f13_range(high, low)
    rz = _z(rng, 63).clip(lower=0)
    b = _mean(uw * rz, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional body share of total 21d body movement (trend dominance of bodies)
def f13cr_f13_candle_range_structure_bodydom_21d_base_v089_signal(open, close):
    body = _f13_body(open, close)
    net = body.rolling(21, min_periods=10).sum()
    gross = body.abs().rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = net / gross
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wick share of total 21d range traversal (rejection-heavy regime)
def f13cr_f13_candle_range_structure_wickshare_21d_base_v090_signal(open, high, low, close):
    uw = _f13_upper_wick(open, high, close)
    lw = _f13_lower_wick(open, low, close)
    rng = _f13_range(high, low)
    wsum = (uw + lw).rolling(21, min_periods=10).sum()
    rsum = rng.rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = wsum / rsum
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion acceleration: 5d range-exp minus 21d range-exp (vol turning point)
def f13cr_f13_candle_range_structure_rngexpaccel_base_v091_signal(high, low):
    rng = _f13_range(high, low)
    ex5 = _mean(rng, 5) / _mean(rng, 63).replace(0, np.nan)
    ex21 = _mean(rng, 21) / _mean(rng, 63).replace(0, np.nan)
    b = ex5 - ex21
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson-style range vol (hi/lo) normalized, 21d (intraday vol estimator)
def f13cr_f13_candle_range_structure_parkinson_21d_base_v092_signal(high, low):
    lr = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    pk = (lr ** 2)
    b = np.sqrt(_mean(pk, 21) / (4.0 * np.log(2.0)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass-style estimator using OHLC (21d)
def f13cr_f13_candle_range_structure_garmanklass_21d_base_v093_signal(open, high, low, close):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    co = np.log(close.replace(0, np.nan) / open.replace(0, np.nan)) ** 2
    gk = 0.5 * hl - (2.0 * np.log(2.0) - 1.0) * co
    b = np.sqrt(_mean(gk, 21).clip(lower=0))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# variance-ratio: close-to-close vol vs Parkinson range vol (vol estimator efficiency)
def f13cr_f13_candle_range_structure_rogersat_21d_base_v094_signal(open, high, low, close):
    cc = close.pct_change()
    cc_var = _mean(cc ** 2, 21)
    lr = np.log(high.replace(0, np.nan) / low.replace(0, np.nan)) ** 2
    pk_var = _mean(lr, 21) / (4.0 * np.log(2.0))
    b = cc_var / pk_var.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-to-close vs intraday-range vol ratio (overnight vs intraday vol mix, 21d)
def f13cr_f13_candle_range_structure_ovnratio_21d_base_v095_signal(high, low, close):
    cc = close.pct_change().abs()
    rng = _f13_range(high, low) / close.replace(0, np.nan)
    b = _mean(cc, 21) / _mean(rng, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body sign persistence: autocorrelation of body direction over 63d
def f13cr_f13_candle_range_structure_bodysignac_63d_base_v096_signal(open, close):
    sg = np.sign(close - open)
    def _ac(a):
        a = a[~np.isnan(a)]
        if len(a) < 10:
            return np.nan
        s0 = a[:-1]
        s1 = a[1:]
        if np.std(s0) == 0 or np.std(s1) == 0:
            return np.nan
        return np.corrcoef(s0, s1)[0, 1]
    b = sg.rolling(63, min_periods=30).apply(_ac, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-weighted directional breadth over 21d (size-weighted up vs down candles)
def f13cr_f13_candle_range_structure_updnbreadth_21d_base_v097_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    signed = np.sign(close - open) * br
    b = _mean(signed, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average body size on up days minus down days (which side has bigger candles, 63d)
def f13cr_f13_candle_range_structure_bodyasym_63d_base_v098_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    up = br.where(close > open)
    dn = br.where(close < open)
    b = up.rolling(63, min_periods=21).mean() - dn.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion with volume confirmation z (climactic thrust, 5d)
def f13cr_f13_candle_range_structure_rngvolz_5d_base_v099_signal(high, low, volume):
    rng = _f13_range(high, low)
    rz = _z(rng, 63)
    vz = _z(volume, 63)
    b = _mean(rz * vz, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range coefficient of variation over 21d (range stability/erraticness)
def f13cr_f13_candle_range_structure_rngcv_21d_base_v100_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    b = _std(tr, 21) / _mean(tr, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body ratio coefficient of variation (consistency of conviction, 63d)
def f13cr_f13_candle_range_structure_bodycv_63d_base_v101_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    b = _std(br, 63) / _mean(br, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net wick pressure with volume weighting (heavy-volume tails, 21d)
def f13cr_f13_candle_range_structure_wickvol_21d_base_v102_signal(open, high, low, close, volume):
    lw = _f13_lower_ratio(open, high, low, close)
    uw = _f13_upper_ratio(open, high, low, close)
    vz = _z(volume, 63)
    b = _mean((lw - uw) * vz, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-in-range trend: slope over a quarter (pressure regime drift)
def f13cr_f13_candle_range_structure_cirdrift_63d_base_v103_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    sm = _mean(cir, 21)
    b = sm - sm.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position of close relative to prior-day close range (gap-aware cir, 5d)
def f13cr_f13_candle_range_structure_gapcir_5d_base_v104_signal(high, low, close):
    hi = np.maximum(high, close.shift(1))
    lo = np.minimum(low, close.shift(1))
    cir = (close - lo) / (hi - lo).replace(0, np.nan)
    b = _mean(cir, 5) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wide-range down-close intensity vs wide-range up-close (sell vs buy climax, 63d)
def f13cr_f13_candle_range_structure_climaxbias_63d_base_v105_signal(open, high, low, close):
    rng = _f13_range(high, low)
    rz = _z(rng, 63).clip(lower=0)
    cir = _f13_close_in_range(high, low, close)
    up = (rz * cir).where(close > open, 0.0)
    dn = (rz * (1.0 - cir)).where(close < open, 0.0)
    b = _mean(up - dn, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body midpoint location trend within the bar (body migrating up/down, 63d)
def f13cr_f13_candle_range_structure_bodyloctrend_63d_base_v106_signal(open, high, low, close):
    mid = (open + close) / 2.0
    rng = _f13_range(high, low).replace(0, np.nan)
    loc = (mid - low) / rng
    sm = _mean(loc, 21)
    b = sm - sm.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# max single-day range over 63d vs current price (recent shock memory)
def f13cr_f13_candle_range_structure_maxshock_63d_base_v107_signal(high, low, close):
    rng = _f13_range(high, low)
    mx = rng.rolling(63, min_periods=21).max()
    b = mx / close.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range compression ratio: current 21d avg range vs 252d avg range (long squeeze)
def f13cr_f13_candle_range_structure_longcompress_base_v108_signal(high, low):
    rng = _f13_range(high, low)
    b = _mean(rng, 21) / _mean(rng, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-near-extreme intensity: |cir-0.5| averaged (decisive closes, 21d)
def f13cr_f13_candle_range_structure_decisive_21d_base_v109_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    b = _mean((cir - 0.5).abs(), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper vs lower wick ratio (rejection direction balance, log, 21d)
def f13cr_f13_candle_range_structure_wicklograt_21d_base_v110_signal(open, high, low, close):
    uw = _f13_upper_wick(open, high, close)
    lw = _f13_lower_wick(open, low, close)
    rat = np.log((lw + 1e-6) / (uw + 1e-6))
    b = _mean(rat, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body ratio momentum confirmed by close-in-range agreement (5d)
def f13cr_f13_candle_range_structure_convagree_5d_base_v111_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    cir = _f13_close_in_range(high, low, close)
    b = _mean(br * (cir - 0.5), 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vs-body churn rank over 126d (indecision percentile)
def f13cr_f13_candle_range_structure_churnrank_126d_base_v112_signal(open, high, low, close):
    rng = _f13_range(high, low)
    body = _f13_body_abs(open, close)
    churn = (rng / body.replace(0, np.nan)).clip(upper=20.0)
    b = _rank(_mean(churn, 5), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of range built by overnight gap vs intraday (gap dominance, 21d)
def f13cr_f13_candle_range_structure_gapdom_21d_base_v113_signal(open, high, low, close):
    gap = (open - close.shift(1)).abs()
    intr = _f13_range(high, low)
    b = _mean(gap / (gap + intr).replace(0, np.nan), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# three-bar range contraction: today vs 3d-ago range (rapid squeeze, 21d mean)
def f13cr_f13_candle_range_structure_rng3contract_21d_base_v114_signal(high, low):
    rng = _f13_range(high, low)
    ratio = rng / rng.shift(3).replace(0, np.nan)
    b = _mean(ratio.clip(upper=10.0), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick dominance streak fraction (persistent overhead rejection, 21d)
def f13cr_f13_candle_range_structure_uwickdom_21d_base_v115_signal(open, high, low, close):
    uw = _f13_upper_ratio(open, high, low, close)
    lw = _f13_lower_ratio(open, high, low, close)
    dom = (uw - lw).clip(lower=0)
    b = _mean(dom, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-wick dominance (persistent support buying intensity, 21d)
def f13cr_f13_candle_range_structure_lwickdom_21d_base_v116_signal(open, high, low, close):
    uw = _f13_upper_ratio(open, high, low, close)
    lw = _f13_lower_ratio(open, high, low, close)
    dom = (lw - uw).clip(lower=0)
    b = _mean(dom, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted body ratio (conviction days weighted by participation, 21d)
def f13cr_f13_candle_range_structure_vwbody_21d_base_v117_signal(open, high, low, close, volume):
    br = _f13_body_ratio(open, high, low, close)
    num = (br * volume).rolling(21, min_periods=10).sum()
    den = volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = num / den
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed thrust z-scored vs 63d history (extreme directional candle, 5d)
def f13cr_f13_candle_range_structure_thrustz_63d_base_v118_signal(open, high, low, close):
    body = _f13_body(open, close)
    rng = _f13_range(high, low).replace(0, np.nan)
    thr = body / rng
    b = _z(_mean(thr, 5), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range entropy: dispersion of daily range distribution over 63d (regime randomness)
def f13cr_f13_candle_range_structure_rngentropy_63d_base_v119_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    def _ent(a):
        a = a[~np.isnan(a)]
        if len(a) < 10 or a.sum() <= 0:
            return np.nan
        p = a / a.sum()
        p = p[p > 0]
        return -np.sum(p * np.log(p)) / np.log(len(a))
    b = tr.rolling(63, min_periods=30).apply(_ent, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-in-range percentile rank over 126d (where today's close placement sits)
def f13cr_f13_candle_range_structure_cirmr_63d_base_v120_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    sm = _mean(cir, 5)
    b = _rank(sm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wide-bar reversal: wide range with close back toward midpoint (failed move, 21d)
def f13cr_f13_candle_range_structure_widerev_21d_base_v121_signal(high, low, close):
    rng = _f13_range(high, low)
    rz = _z(rng, 63).clip(lower=0)
    cir = _f13_close_in_range(high, low, close)
    mid_close = 1.0 - (cir - 0.5).abs() * 2.0
    b = _mean(rz * mid_close, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-to-true-range ratio (gap-aware conviction, 21d)
def f13cr_f13_candle_range_structure_bodytruerng_21d_base_v122_signal(open, high, low, close):
    body = _f13_body_abs(open, close)
    tr = _f13_true_range(high, low, close).replace(0, np.nan)
    b = _mean(body / tr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion vs body expansion divergence (range grows, body lags, 21d)
def f13cr_f13_candle_range_structure_rngbodydiverge_base_v123_signal(open, high, low, close):
    rng = _f13_range(high, low)
    body = _f13_body_abs(open, close)
    rex = _mean(rng, 5) / _mean(rng, 63).replace(0, np.nan)
    bex = _mean(body, 5) / _mean(body, 63).replace(0, np.nan)
    b = rex - bex
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of 63d range traversed by net move (efficiency over a quarter)
def f13cr_f13_candle_range_structure_rngeffic_63d_base_v124_signal(high, low, close):
    net = (close - close.shift(63)).abs()
    path = _f13_range(high, low).rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = net / path
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick rejection trend: change in 21d upper-wick over a month (building supply)
def f13cr_f13_candle_range_structure_uwicktrend_21d_base_v125_signal(open, high, low, close):
    uw = _f13_upper_ratio(open, high, low, close)
    sm = _mean(uw, 21)
    b = sm - sm.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-wick support trend: change in 21d lower-wick over a month (building demand)
def f13cr_f13_candle_range_structure_lwicktrend_21d_base_v126_signal(open, high, low, close):
    lw = _f13_lower_ratio(open, high, low, close)
    sm = _mean(lw, 21)
    b = sm - sm.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# small-body-after-wide-bar intensity (exhaustion doji after thrust, 21d)
def f13cr_f13_candle_range_structure_exhdoji_21d_base_v127_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    rng = _f13_range(high, low)
    prior_wide = (_z(rng, 63).shift(1)).clip(lower=0)
    small = (1.0 - br).clip(lower=0)
    b = _mean(small * prior_wide, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range z vs price-move z divergence (volatility without direction, 21d)
def f13cr_f13_candle_range_structure_voldirgap_21d_base_v128_signal(high, low, close):
    rng = _f13_range(high, low) / close.replace(0, np.nan)
    mv = close.pct_change().abs()
    b = _z(_mean(rng, 5), 63) - _z(_mean(mv, 5), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of 21d closes in upper half weighted by body size (committed strength)
def f13cr_f13_candle_range_structure_strongbody_21d_base_v129_signal(open, high, low, close):
    cir = _f13_close_in_range(high, low, close)
    br = _f13_body_ratio(open, high, low, close)
    b = _mean((cir - 0.5) * br, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position skew over 63d (asymmetry of where closes land in bars)
def f13cr_f13_candle_range_structure_cirskew_63d_base_v130_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    b = cir.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body ratio skew over 63d (occasional huge-conviction candles)
def f13cr_f13_candle_range_structure_bodyskew_63d_base_v131_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    b = br.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion with volume divergence (range up, volume not — weak move, 21d)
def f13cr_f13_candle_range_structure_rngvoldiv_21d_base_v132_signal(high, low, volume):
    rng = _f13_range(high, low)
    rz = _z(_mean(rng, 5), 63)
    vz = _z(_mean(volume, 5), 63)
    b = rz - vz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# clustered-wide-bars: 21d mean of (range>1.5x median) magnitude with run weighting
def f13cr_f13_candle_range_structure_wideclust_21d_base_v133_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    med = tr.rolling(63, min_periods=21).median().replace(0, np.nan)
    over = (tr / med - 1.5).clip(lower=0)
    run = over.rolling(3, min_periods=1).sum()
    b = _mean(over * run, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-position relative to 5d range (multi-day close-in-range, swing pressure)
def f13cr_f13_candle_range_structure_cir5d_window_base_v134_signal(high, low, close):
    hi = high.rolling(5, min_periods=3).max()
    lo = low.rolling(5, min_periods=3).min()
    cir = (close - lo) / (hi - lo).replace(0, np.nan)
    b = _mean(cir, 5) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-day (21d) close-in-range position (swing-level range location)
def f13cr_f13_candle_range_structure_cir21d_window_base_v135_signal(high, low, close):
    hi = high.rolling(21, min_periods=10).max()
    lo = low.rolling(21, min_periods=10).min()
    b = (close - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion persistence: EMA of range/avg ratio (sticky vol regime)
def f13cr_f13_candle_range_structure_rngexpema_base_v136_signal(high, low):
    rng = _f13_range(high, low)
    ex = rng / _mean(rng, 63).replace(0, np.nan)
    b = ex.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body direction vs close-in-range disagreement, magnitude-weighted (21d)
def f13cr_f13_candle_range_structure_bodycirdisagree_base_v137_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    cir = _f13_close_in_range(high, low, close)
    body_dir = np.sign(close - open)
    cir_dir = np.sign(cir - 0.5)
    disagree = (body_dir != cir_dir).astype(float)
    mag = disagree * br * (cir - 0.5).abs()
    b = _mean(mag, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range shock recency: bars since last >2x-median range, decayed (21d window)
def f13cr_f13_candle_range_structure_shockrecency_base_v138_signal(high, low, close):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    med = tr.rolling(63, min_periods=21).median().replace(0, np.nan)
    shock = (tr > 2.0 * med).astype(float)
    decay = shock.ewm(span=21, min_periods=5).mean()
    b = decay
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average true range slope over 63d (vol trend, intraday)
def f13cr_f13_candle_range_structure_atrslope_63d_base_v139_signal(high, low, close):
    tr = _f13_true_range(high, low, close) / close.replace(0, np.nan)
    sm = _mean(tr, 21)
    b = sm - sm.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# half-range location of close: upper-third vs lower-third committed-close balance (63d)
def f13cr_f13_candle_range_structure_thirdbalance_63d_base_v140_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    up = (cir - 0.667).clip(lower=0)
    dn = (0.333 - cir).clip(lower=0)
    b = _mean(up - dn, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body+wick interaction: marubozu-ness minus doji-ness net regime (21d)
def f13cr_f13_candle_range_structure_conviction_21d_base_v141_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    maru = (br - 0.6).clip(lower=0)
    doji = (0.2 - br).clip(lower=0)
    b = _mean(maru - doji, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion gated by direction agreement over 5d (clean breakout thrust)
def f13cr_f13_candle_range_structure_cleanbreak_5d_base_v142_signal(open, high, low, close):
    rng = _f13_range(high, low)
    rz = _z(rng, 63).clip(lower=0)
    br = _f13_body_ratio(open, high, low, close)
    b = _mean(rz * br * np.sign(close - open), 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside range vs upside range asymmetry (down-day bars vs up-day bars, 63d)
def f13cr_f13_candle_range_structure_rngdownasym_63d_base_v143_signal(high, low, close, open):
    tr = _f13_range(high, low) / close.replace(0, np.nan)
    dn = tr.where(close < open)
    up = tr.where(close > open)
    b = dn.rolling(63, min_periods=21).mean() - up.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest body candle share of 63d total body movement (one-day-dominated moves)
def f13cr_f13_candle_range_structure_bodyconc_63d_base_v144_signal(open, close):
    body = _f13_body_abs(open, close)
    mx = body.rolling(63, min_periods=21).max()
    tot = body.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = mx / tot
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-in-range volatility regime: rolling std of cir z-scored (pressure instability)
def f13cr_f13_candle_range_structure_cirvolz_63d_base_v145_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    sd = _std(cir, 21)
    b = _z(sd, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tweezers / wick-cluster: matching extreme wicks two days running (reversal, 21d)
def f13cr_f13_candle_range_structure_tweezer_21d_base_v146_signal(open, high, low, close):
    lw = _f13_lower_ratio(open, high, low, close)
    uw = _f13_upper_ratio(open, high, low, close)
    bot_cluster = (lw.clip(lower=0) * lw.shift(1).clip(lower=0))
    top_cluster = (uw.clip(lower=0) * uw.shift(1).clip(lower=0))
    b = _mean(bot_cluster - top_cluster, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-normalized close change (close move per unit of bar range, 5d)
def f13cr_f13_candle_range_structure_closeoverrng_5d_base_v147_signal(high, low, close):
    chg = close.diff()
    rng = _f13_range(high, low).replace(0, np.nan)
    b = _mean(chg / rng, 5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capitulation depth z: weak-close down-bars range z-scored over 126d (deep distress)
def f13cr_f13_candle_range_structure_capitdepthz_126d_base_v148_signal(open, high, low, close):
    rng = _f13_range(high, low)
    cir = _f13_close_in_range(high, low, close)
    cap = (rng * (1.0 - cir)).where(close < open, 0.0)
    sm = _mean(cap, 5)
    b = _z(sm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blow-off depth z: strong-close up-bars range z-scored over 126d (euphoria)
def f13cr_f13_candle_range_structure_blowoffz_126d_base_v149_signal(open, high, low, close):
    rng = _f13_range(high, low)
    cir = _f13_close_in_range(high, low, close)
    bo = (rng * cir).where(close > open, 0.0)
    sm = _mean(bo, 5)
    b = _z(sm, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite candle conviction: body x close-strength x volume, smoothed (21d)
def f13cr_f13_candle_range_structure_composite_21d_base_v150_signal(open, high, low, close, volume):
    br = _f13_body_ratio(open, high, low, close)
    cir = _f13_close_in_range(high, low, close)
    vz = _z(volume, 63)
    sig = br * (cir - 0.5) * np.tanh(vz)
    b = _mean(sig, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f13cr_f13_candle_range_structure_bodyrank_252d_base_v076_signal,
    f13cr_f13_candle_range_structure_cirema_21d_base_v077_signal,
    f13cr_f13_candle_range_structure_cirdisp_63d_base_v078_signal,
    f13cr_f13_candle_range_structure_uwickz_126d_base_v079_signal,
    f13cr_f13_candle_range_structure_lwickz_126d_base_v080_signal,
    f13cr_f13_candle_range_structure_wickskewmom_21d_base_v081_signal,
    f13cr_f13_candle_range_structure_truatr_21d_base_v082_signal,
    f13cr_f13_candle_range_structure_gaprng_21d_base_v083_signal,
    f13cr_f13_candle_range_structure_rngexprank_126d_base_v084_signal,
    f13cr_f13_candle_range_structure_rngbodyz_63d_base_v085_signal,
    f13cr_f13_candle_range_structure_bodyrel_63d_base_v086_signal,
    f13cr_f13_candle_range_structure_strongwide_5d_base_v087_signal,
    f13cr_f13_candle_range_structure_wickwide_5d_base_v088_signal,
    f13cr_f13_candle_range_structure_bodydom_21d_base_v089_signal,
    f13cr_f13_candle_range_structure_wickshare_21d_base_v090_signal,
    f13cr_f13_candle_range_structure_rngexpaccel_base_v091_signal,
    f13cr_f13_candle_range_structure_parkinson_21d_base_v092_signal,
    f13cr_f13_candle_range_structure_garmanklass_21d_base_v093_signal,
    f13cr_f13_candle_range_structure_rogersat_21d_base_v094_signal,
    f13cr_f13_candle_range_structure_ovnratio_21d_base_v095_signal,
    f13cr_f13_candle_range_structure_bodysignac_63d_base_v096_signal,
    f13cr_f13_candle_range_structure_updnbreadth_21d_base_v097_signal,
    f13cr_f13_candle_range_structure_bodyasym_63d_base_v098_signal,
    f13cr_f13_candle_range_structure_rngvolz_5d_base_v099_signal,
    f13cr_f13_candle_range_structure_rngcv_21d_base_v100_signal,
    f13cr_f13_candle_range_structure_bodycv_63d_base_v101_signal,
    f13cr_f13_candle_range_structure_wickvol_21d_base_v102_signal,
    f13cr_f13_candle_range_structure_cirdrift_63d_base_v103_signal,
    f13cr_f13_candle_range_structure_gapcir_5d_base_v104_signal,
    f13cr_f13_candle_range_structure_climaxbias_63d_base_v105_signal,
    f13cr_f13_candle_range_structure_bodyloctrend_63d_base_v106_signal,
    f13cr_f13_candle_range_structure_maxshock_63d_base_v107_signal,
    f13cr_f13_candle_range_structure_longcompress_base_v108_signal,
    f13cr_f13_candle_range_structure_decisive_21d_base_v109_signal,
    f13cr_f13_candle_range_structure_wicklograt_21d_base_v110_signal,
    f13cr_f13_candle_range_structure_convagree_5d_base_v111_signal,
    f13cr_f13_candle_range_structure_churnrank_126d_base_v112_signal,
    f13cr_f13_candle_range_structure_gapdom_21d_base_v113_signal,
    f13cr_f13_candle_range_structure_rng3contract_21d_base_v114_signal,
    f13cr_f13_candle_range_structure_uwickdom_21d_base_v115_signal,
    f13cr_f13_candle_range_structure_lwickdom_21d_base_v116_signal,
    f13cr_f13_candle_range_structure_vwbody_21d_base_v117_signal,
    f13cr_f13_candle_range_structure_thrustz_63d_base_v118_signal,
    f13cr_f13_candle_range_structure_rngentropy_63d_base_v119_signal,
    f13cr_f13_candle_range_structure_cirmr_63d_base_v120_signal,
    f13cr_f13_candle_range_structure_widerev_21d_base_v121_signal,
    f13cr_f13_candle_range_structure_bodytruerng_21d_base_v122_signal,
    f13cr_f13_candle_range_structure_rngbodydiverge_base_v123_signal,
    f13cr_f13_candle_range_structure_rngeffic_63d_base_v124_signal,
    f13cr_f13_candle_range_structure_uwicktrend_21d_base_v125_signal,
    f13cr_f13_candle_range_structure_lwicktrend_21d_base_v126_signal,
    f13cr_f13_candle_range_structure_exhdoji_21d_base_v127_signal,
    f13cr_f13_candle_range_structure_voldirgap_21d_base_v128_signal,
    f13cr_f13_candle_range_structure_strongbody_21d_base_v129_signal,
    f13cr_f13_candle_range_structure_cirskew_63d_base_v130_signal,
    f13cr_f13_candle_range_structure_bodyskew_63d_base_v131_signal,
    f13cr_f13_candle_range_structure_rngvoldiv_21d_base_v132_signal,
    f13cr_f13_candle_range_structure_wideclust_21d_base_v133_signal,
    f13cr_f13_candle_range_structure_cir5d_window_base_v134_signal,
    f13cr_f13_candle_range_structure_cir21d_window_base_v135_signal,
    f13cr_f13_candle_range_structure_rngexpema_base_v136_signal,
    f13cr_f13_candle_range_structure_bodycirdisagree_base_v137_signal,
    f13cr_f13_candle_range_structure_shockrecency_base_v138_signal,
    f13cr_f13_candle_range_structure_atrslope_63d_base_v139_signal,
    f13cr_f13_candle_range_structure_thirdbalance_63d_base_v140_signal,
    f13cr_f13_candle_range_structure_conviction_21d_base_v141_signal,
    f13cr_f13_candle_range_structure_cleanbreak_5d_base_v142_signal,
    f13cr_f13_candle_range_structure_rngdownasym_63d_base_v143_signal,
    f13cr_f13_candle_range_structure_bodyconc_63d_base_v144_signal,
    f13cr_f13_candle_range_structure_cirvolz_63d_base_v145_signal,
    f13cr_f13_candle_range_structure_tweezer_21d_base_v146_signal,
    f13cr_f13_candle_range_structure_closeoverrng_5d_base_v147_signal,
    f13cr_f13_candle_range_structure_capitdepthz_126d_base_v148_signal,
    f13cr_f13_candle_range_structure_blowoffz_126d_base_v149_signal,
    f13cr_f13_candle_range_structure_composite_21d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_CANDLE_RANGE_STRUCTURE_REGISTRY_076_150 = REGISTRY


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

    print("OK f13_candle_range_structure_base_076_150_claude: %d features pass" % n_features)
