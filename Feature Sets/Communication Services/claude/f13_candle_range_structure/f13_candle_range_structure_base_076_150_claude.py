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


# ===== folder domain primitives (candle / range structure) =====
def _f13_range(high, low):
    return (high - low)


def _f13_body(open, close):
    return (close - open)


def _f13_body_abs(open, close):
    return (close - open).abs()


def _f13_body_ratio(open, high, low, close):
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
    rng = (high - low).replace(0, np.nan)
    return (close - low) / rng


def _f13_range_pct(high, low, close):
    return (high - low) / close.replace(0, np.nan)


def _f13_clv(high, low, close):
    rng = (high - low).replace(0, np.nan)
    return ((close - low) - (high - close)) / rng


def _f13_truerange(high, low, close):
    pc = close.shift(1)
    a = (high - low)
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


# ============================================================
# 63d body/range mean (slower decisiveness regime level)
def f13cr_f13_candle_range_structure_bodyrng_63d_base_v076_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    b = _mean(br, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d body/range mean (semiannual decisiveness)
def f13cr_f13_candle_range_structure_bodyrng_126d_base_v077_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    b = _mean(br, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true-range as % of close, 21d mean (gap-inclusive range intensity)
def f13cr_f13_candle_range_structure_trpct_21d_base_v078_signal(high, low, close):
    tr = _f13_truerange(high, low, close)
    b = _mean(tr / close.replace(0, np.nan), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true-range vs intraday-range gap (overnight contribution to true range), 21d
def f13cr_f13_candle_range_structure_trgap_21d_base_v079_signal(high, low, close):
    tr = _f13_truerange(high, low, close)
    rng = _f13_range(high, low)
    b = _mean((tr - rng) / close.replace(0, np.nan), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-in-range 63d mean centered (slow close strength)
def f13cr_f13_candle_range_structure_cir_63d_base_v080_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    b = _mean(cir, 63) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-in-range 126d mean centered
def f13cr_f13_candle_range_structure_cir_126d_base_v081_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    b = _mean(cir, 126) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick ratio 63d (slow rejection pressure)
def f13cr_f13_candle_range_structure_uwick_63d_base_v082_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    b = _mean(uw, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-wick ratio 63d (slow demand support)
def f13cr_f13_candle_range_structure_lwick_63d_base_v083_signal(open, high, low, close):
    lw = _f13_lower_wick_ratio(open, high, low, close)
    b = _mean(lw, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CLV 21d mean (accumulation/distribution per bar)
def f13cr_f13_candle_range_structure_clv_21d_base_v084_signal(high, low, close):
    clv = _f13_clv(high, low, close)
    b = _mean(clv, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted CLV 63d (slow accumulation/distribution weighted by participation)
def f13cr_f13_candle_range_structure_clv_63d_base_v085_signal(high, low, close, volume):
    clv = _f13_clv(high, low, close)
    num = (clv * volume).rolling(63, min_periods=21).sum()
    den = volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = num / den
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range% 63d mean (slow range intensity)
def f13cr_f13_candle_range_structure_rngpct_63d_base_v086_signal(high, low, close):
    rp = _f13_range_pct(high, low, close)
    b = _mean(rp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range% 126d mean
def f13cr_f13_candle_range_structure_rngpct_126d_base_v087_signal(high, low, close):
    rp = _f13_range_pct(high, low, close)
    b = _mean(rp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range% vol-of-vol: std of range% over 63d normalized by its mean (range instability)
def f13cr_f13_candle_range_structure_rngcov_63d_base_v088_signal(high, low, close):
    rp = _f13_range_pct(high, low, close)
    b = _std(rp, 63) / _mean(rp, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body/range coefficient of variation 63d (decisiveness consistency)
def f13cr_f13_candle_range_structure_brcov_63d_base_v089_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    b = _std(br, 63) / _mean(br, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# two-bar body overlap: fraction of today's body overlapping yesterday's body, 21d
def f13cr_f13_candle_range_structure_bodyoverlap_21d_base_v090_signal(open, close):
    lo = pd.concat([open, close], axis=1).min(axis=1)
    hi = pd.concat([open, close], axis=1).max(axis=1)
    ov = (pd.concat([hi, hi.shift(1)], axis=1).min(axis=1)
          - pd.concat([lo, lo.shift(1)], axis=1).max(axis=1)).clip(lower=0)
    rng = (hi - lo).replace(0, np.nan)
    b = _mean(ov / rng, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# two-bar range overlap (congestion/consolidation), 21d
def f13cr_f13_candle_range_structure_rngoverlap_21d_base_v091_signal(high, low):
    ov = (pd.concat([high, high.shift(1)], axis=1).min(axis=1)
          - pd.concat([low, low.shift(1)], axis=1).max(axis=1)).clip(lower=0)
    rng = (high - low).replace(0, np.nan)
    b = _mean(ov / rng, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-up frequency-weighted magnitude: open above prior high (true gap up), 21d
def f13cr_f13_candle_range_structure_gapup_21d_base_v092_signal(open, high):
    gap = ((open - high.shift(1)) / high.shift(1).replace(0, np.nan)).clip(lower=0)
    b = _mean(gap, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-down magnitude: open below prior low (true gap down), 21d
def f13cr_f13_candle_range_structure_gapdn_21d_base_v093_signal(open, low):
    gap = ((low.shift(1) - open) / low.shift(1).replace(0, np.nan)).clip(lower=0)
    b = _mean(gap, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-fill tendency weighted by retracement depth: how far gaps closed back, 21d
def f13cr_f13_candle_range_structure_gapfill_21d_base_v094_signal(open, high, low, close):
    pc = close.shift(1)
    gap = (open - pc)
    retrace = (open - close) / gap.where(gap.abs() > 0)
    retrace = retrace.clip(lower=-1, upper=2)
    b = _mean(retrace, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-fade magnitude: opposing intraday move scaled by gap size, 21d mean
def f13cr_f13_candle_range_structure_gapfade_21d_base_v095_signal(open, close):
    pc = close.shift(1)
    gap = (open - pc) / pc.replace(0, np.nan)
    intraday = (close - open) / open.replace(0, np.nan)
    fade = (-np.sign(gap) * intraday).where(gap.abs() > 0)
    b = _mean(fade, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wick symmetry: |uw - lw| over range (one-sided tail bias), 21d mean
def f13cr_f13_candle_range_structure_wickasym_21d_base_v096_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    b = _mean((uw - lw).abs(), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rejection/demand ratio: upper-wick sum over lower-wick sum, 63d (log)
def f13cr_f13_candle_range_structure_totwick_63d_base_v097_signal(open, high, low, close):
    uw = _f13_upper_wick(open, high, low, close)
    lw = _f13_lower_wick(open, high, low, close)
    us = uw.rolling(63, min_periods=21).sum()
    ls = lw.rolling(63, min_periods=21).sum()
    b = np.log((us + 1e-9) / (ls + 1e-9))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-in-range trend: 21d cir mean minus 63d cir mean (closing-strength momentum)
def f13cr_f13_candle_range_structure_cirtrend_base_v098_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    b = _mean(cir, 21) - _mean(cir, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body/range trend: 21d vs 126d decisiveness momentum
def f13cr_f13_candle_range_structure_brtrend_base_v099_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    b = _mean(br, 21) - _mean(br, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-volume elasticity: corr of daily range with volume over 63d (confirmation)
def f13cr_f13_candle_range_structure_rngvolcorr_63d_base_v100_signal(high, low, volume):
    rng = _f13_range(high, low)
    cov = (rng * volume).rolling(63, min_periods=21).mean() - _mean(rng, 63) * _mean(volume, 63)
    b = cov / (_std(rng, 63) * _std(volume, 63)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close-strength-volume corr: do strong closes come on volume? 63d
def f13cr_f13_candle_range_structure_cirvolcorr_63d_base_v101_signal(high, low, close, volume):
    cir = _f13_close_in_range(high, low, close)
    cov = (cir * volume).rolling(63, min_periods=21).mean() - _mean(cir, 63) * _mean(volume, 63)
    b = cov / (_std(cir, 63) * _std(volume, 63)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted range expansion: big-range bars' volume share, 21d
def f13cr_f13_candle_range_structure_vwrngexp_21d_base_v102_signal(high, low, volume):
    rngz = _z(_f13_range(high, low), 63)
    wide = (rngz > 1.0).astype(float)
    num = (wide * volume).rolling(21, min_periods=5).sum()
    den = volume.rolling(21, min_periods=5).sum().replace(0, np.nan)
    b = num / den
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest single-bar range in last 21d relative to median range (shock magnitude)
def f13cr_f13_candle_range_structure_rngshock_21d_base_v103_signal(high, low, close):
    rp = _f13_range_pct(high, low, close)
    b = _rmax(rp, 21) / rp.rolling(63, min_periods=21).median().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smallest single-bar range in last 21d relative to median (squeeze depth)
def f13cr_f13_candle_range_structure_rngsqueeze_21d_base_v104_signal(high, low, close):
    rp = _f13_range_pct(high, low, close)
    b = _rmin(rp, 21) / rp.rolling(63, min_periods=21).median().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-to-truerange ratio (decisiveness incl. gaps), 21d
def f13cr_f13_candle_range_structure_bodytr_21d_base_v105_signal(open, high, low, close):
    body = _f13_body_abs(open, close)
    tr = _f13_truerange(high, low, close).replace(0, np.nan)
    b = _mean(body / tr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional close-in-range persistence: autocorr of cir over 63d
def f13cr_f13_candle_range_structure_cirautocorr_63d_base_v106_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    lag = cir.shift(1)
    cov = (cir * lag).rolling(63, min_periods=21).mean() - _mean(cir, 63) * _mean(lag, 63)
    b = cov / (_std(cir, 63) * _std(lag, 63)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range mean-reversion: corr of range change with prior range level (contraction tendency), 63d
def f13cr_f13_candle_range_structure_rngmeanrev_63d_base_v107_signal(high, low):
    rng = _f13_range(high, low)
    dr = rng.diff()
    lag = rng.shift(1)
    cov = (dr * lag).rolling(63, min_periods=21).mean() - _mean(dr, 63) * _mean(lag, 63)
    b = cov / (_std(dr, 63) * _std(lag, 63)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 63d that were strong-close (cir>0.6) bars with above-avg volume
def f13cr_f13_candle_range_structure_strongvol_63d_base_v108_signal(high, low, close, volume):
    cir = _f13_close_in_range(high, low, close)
    vavg = _mean(volume, 63)
    strong = ((cir > 0.6).astype(float)) * (volume / vavg.replace(0, np.nan))
    b = _mean(strong, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weak-close-on-volume fraction (distribution), 63d
def f13cr_f13_candle_range_structure_weakvol_63d_base_v109_signal(high, low, close, volume):
    cir = _f13_close_in_range(high, low, close)
    vavg = _mean(volume, 63)
    weak = ((cir < 0.4).astype(float)) * (volume / vavg.replace(0, np.nan))
    b = _mean(weak, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-percentile rank vs 504d history (long-horizon range regime)
def f13cr_f13_candle_range_structure_rngrank_504d_base_v110_signal(high, low, close):
    rp = _f13_range_pct(high, low, close)
    m = _mean(rp, 21)
    b = _rank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# directional range skew over 63d: signed-body weighted range share
def f13cr_f13_candle_range_structure_dirrng_63d_base_v111_signal(open, high, low, close):
    sgn = np.sign(close - open)
    rngz = _z(_f13_range(high, low), 126)
    b = _mean(sgn * rngz, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wick imbalance trend: 21d wick skew minus 63d wick skew (rotation of pressure)
def f13cr_f13_candle_range_structure_wicktrend_base_v112_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    sk = lw - uw
    b = _mean(sk, 21) - _mean(sk, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper-wick rejection at new local highs: uw when high == 21d high, 63d mean
def f13cr_f13_candle_range_structure_rejhi_63d_base_v113_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    at_hi = (high >= _rmax(high, 21)).astype(float)
    num = (uw * at_hi).rolling(63, min_periods=21).sum()
    den = at_hi.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = num / den
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-wick demand at new local lows: lw when low == 21d low, 63d mean
def f13cr_f13_candle_range_structure_demlo_63d_base_v114_signal(open, high, low, close):
    lw = _f13_lower_wick_ratio(open, high, low, close)
    at_lo = (low <= _rmin(low, 21)).astype(float)
    num = (lw * at_lo).rolling(63, min_periods=21).sum()
    den = at_lo.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = num / den
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion clustering: std of range-z over 21d (burstiness)
def f13cr_f13_candle_range_structure_rngburst_21d_base_v115_signal(high, low):
    rngz = _z(_f13_range(high, low), 63)
    b = _std(rngz, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-magnitude (|body|/close) 21d mean (raw candle thrust)
def f13cr_f13_candle_range_structure_bodymag_21d_base_v116_signal(open, close):
    bm = (close - open).abs() / close.replace(0, np.nan)
    b = _mean(bm, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed body magnitude 21d (net directional thrust)
def f13cr_f13_candle_range_structure_sbodymag_21d_base_v117_signal(open, close):
    sbm = (close - open) / close.replace(0, np.nan)
    b = _mean(sbm, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-magnitude z vs 126d (thrust extremity), 21d mean
def f13cr_f13_candle_range_structure_bodymagz_base_v118_signal(open, close):
    bm = (close - open).abs() / close.replace(0, np.nan)
    b = _z(bm, 126).rolling(21, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last 63d where close > open (up-candle prevalence)
def f13cr_f13_candle_range_structure_upcandle_63d_base_v119_signal(open, close):
    up = (close > open).astype(float)
    depth = ((close - open) / close.replace(0, np.nan)).clip(lower=0)
    b = _mean(up, 63) + 3.0 * _mean(depth, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# opening drive: where open sits vs prior close, normalized by range, 21d
def f13cr_f13_candle_range_structure_opendrive_21d_base_v120_signal(open, high, low, close):
    rng = (high - low).replace(0, np.nan)
    od = (open - close.shift(1)) / rng
    b = _mean(od, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday recovery: how far close recovered off the low vs the open's distance to low, 21d
def f13cr_f13_candle_range_structure_intrarecov_21d_base_v121_signal(open, high, low, close):
    bot_dist = (open - low)
    rec = (close - low)
    ratio = (rec - bot_dist) / (high - low).replace(0, np.nan)
    b = _mean(ratio, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# bar-shape entropy: dispersion across {body, uw, lw} shares within bar, 21d
def f13cr_f13_candle_range_structure_shapeentropy_21d_base_v122_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    comp = pd.concat([br, uw, lw], axis=1)
    ent = comp.std(axis=1)
    b = _mean(ent, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-of-closes within bar consistency: 1 - dispersion of cir, 63d (closing discipline)
def f13cr_f13_candle_range_structure_closedisc_63d_base_v123_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    b = 1.0 - _std(cir, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-weighted CLV trend (participation-backed accumulation momentum), 21d vs 63d
def f13cr_f13_candle_range_structure_clvtrend_base_v124_signal(high, low, close, volume):
    clv = _f13_clv(high, low, close)

    def _vwclv(w):
        num = (clv * volume).rolling(w, min_periods=max(5, w // 2)).sum()
        den = volume.rolling(w, min_periods=max(5, w // 2)).sum().replace(0, np.nan)
        return num / den
    b = _vwclv(21) - _vwclv(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# CLV z vs 126d (accumulation extremity), 21d mean
def f13cr_f13_candle_range_structure_clvz_base_v125_signal(high, low, close):
    clv = _f13_clv(high, low, close)
    b = _z(clv, 126).rolling(21, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of range built before the close vs after (close-vs-extreme distance), 21d
def f13cr_f13_candle_range_structure_closetoext_21d_base_v126_signal(high, low, close):
    to_hi = (high - close)
    to_lo = (close - low)
    rng = (high - low).replace(0, np.nan)
    nearest = pd.concat([to_hi, to_lo], axis=1).min(axis=1) / rng
    b = _mean(nearest, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# big-range-day directional bias: signed CLV on wide-range bars, 63d
def f13cr_f13_candle_range_structure_widebias_63d_base_v127_signal(high, low, close):
    clv = _f13_clv(high, low, close)
    rngz = _z(_f13_range(high, low), 63)
    wide = (rngz > 1.0).astype(float)
    num = (clv * wide).rolling(63, min_periods=21).sum()
    den = wide.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = num / den
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range trend slope proxy: 5d avg range minus 21d avg range over 21d-avg (normalized)
def f13cr_f13_candle_range_structure_rngslopeprox_base_v128_signal(high, low):
    rng = _f13_range(high, low)
    b = (_mean(rng, 5) - _mean(rng, 21)) / _mean(rng, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# doji-after-trend: small body following a wide-range bar, 21d (exhaustion proxy)
def f13cr_f13_candle_range_structure_exhaust_21d_base_v129_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    rngz = _z(_f13_range(high, low), 63)
    prev_wide = (rngz.shift(1) > 1.0).astype(float)
    small = (0.25 - br).clip(lower=0)
    b = _mean(prev_wide * small, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# three-bar momentum of close-in-range (short closing-strength acceleration), 21d
def f13cr_f13_candle_range_structure_cir3mom_21d_base_v130_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    b = _mean(cir - cir.shift(3), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion vs body expansion divergence: range grows faster than body, 21d
def f13cr_f13_candle_range_structure_rngbodydiv_21d_base_v131_signal(open, high, low, close):
    rng = _f13_range(high, low)
    body = _f13_body_abs(open, close)
    rg = _mean(rng, 5) / _mean(rng, 21).replace(0, np.nan)
    bg = _mean(body, 5) / _mean(body, 21).replace(0, np.nan)
    b = rg - bg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume-per-range z (effort/result) 63d level
def f13cr_f13_candle_range_structure_effort_63d_base_v132_signal(high, low, close, volume):
    rp = _f13_range_pct(high, low, close).replace(0, np.nan)
    eff = volume / rp
    b = _z(eff, 126).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# climactic-bar count 63d: range-z>2 and vol-z>2 blended with intensity
def f13cr_f13_candle_range_structure_climaxcnt_63d_base_v133_signal(high, low, volume):
    rngz = _z(_f13_range(high, low), 126)
    volz = _z(volume, 126)
    clim = ((rngz > 2.0) & (volz > 2.0)).astype(float)
    inten = (rngz.clip(lower=0) * volz.clip(lower=0))
    b = _mean(clim, 63) + 0.1 * _mean(inten, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absolute close-in-range extremity (how often closes near a bar edge), 63d
def f13cr_f13_candle_range_structure_edgeclose_63d_base_v134_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    edge = (cir - 0.5).abs() * 2.0
    b = _mean(edge, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range autocorrelation regime change: 21d range-clustering minus 63d (vol-cluster shift)
def f13cr_f13_candle_range_structure_clustshift_base_v135_signal(high, low):
    rng = _f13_range(high, low)
    lag = rng.shift(1)
    def _ac(w):
        cov = (rng * lag).rolling(w, min_periods=max(10, w // 2)).mean() - _mean(rng, w) * _mean(lag, w)
        return cov / (_std(rng, w) * _std(lag, w)).replace(0, np.nan)
    b = _ac(21) - _ac(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close vs 3-bar typical-price center: close above/below recent HLC mean, 21d
def f13cr_f13_candle_range_structure_clvtyp_21d_base_v136_signal(high, low, close):
    typ = (high + low + close) / 3.0
    center = typ.rolling(3, min_periods=2).mean()
    rng = _f13_range(high, low).rolling(3, min_periods=2).mean().replace(0, np.nan)
    b = _mean((close - center) / rng, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wide-range up vs wide-range down asymmetry, 63d (which side gets the big bars)
def f13cr_f13_candle_range_structure_wideasym_63d_base_v137_signal(open, high, low, close):
    rngz = _z(_f13_range(high, low), 63)
    up = ((close > open) & (rngz > 1.0)).astype(float)
    dn = ((close < open) & (rngz > 1.0)).astype(float)
    b = _mean(up - dn, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-range ratio percentile over 504d (long decisiveness regime)
def f13cr_f13_candle_range_structure_brrank_504d_base_v138_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    m = _mean(br, 63)
    b = _rank(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# consecutive narrow-range squeeze pressure: 5d avg range vs 126d avg range
def f13cr_f13_candle_range_structure_squeeze_5v126_base_v139_signal(high, low):
    rng = _f13_range(high, low)
    b = _mean(rng, 5) / _mean(rng, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# realized-range vol: 21d std of true-range%/close (range-volatility)
def f13cr_f13_candle_range_structure_rangevol_21d_base_v140_signal(high, low, close):
    tr = _f13_truerange(high, low, close) / close.replace(0, np.nan)
    b = _std(tr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upper vs lower excursion balance from open: (high-open) vs (open-low), 63d
def f13cr_f13_candle_range_structure_excbal_63d_base_v141_signal(open, high, low):
    up = (high - open)
    dn = (open - low)
    rng = (high - low).replace(0, np.nan)
    b = _mean((up - dn) / rng, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-in-bar magnitude 63d: |open - prior close| / true range
def f13cr_f13_candle_range_structure_gapinbar_63d_base_v142_signal(open, high, low, close):
    tr = _f13_truerange(high, low, close).replace(0, np.nan)
    g = (open - close.shift(1)).abs() / tr
    b = _mean(g.clip(upper=3), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# closing-strength dispersion regime: 63d std of cir minus its 252d median std
def f13cr_f13_candle_range_structure_cirvolreg_base_v143_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    s = _std(cir, 63)
    b = s - s.rolling(252, min_periods=126).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of range above prior close (overnight-anchored upside), 21d
def f13cr_f13_candle_range_structure_overup_21d_base_v144_signal(high, low, close):
    pc = close.shift(1)
    rng = (high - low).replace(0, np.nan)
    up = (high - pc).clip(lower=0) / rng
    b = _mean(up.clip(upper=3), 21) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body acceleration proxy: signed body 5d mean minus 21d mean over range scale
def f13cr_f13_candle_range_structure_bodyaccel_base_v145_signal(open, high, low, close):
    rng = (high - low).replace(0, np.nan)
    sbr = (close - open) / rng
    b = _mean(sbr, 5) - 2.0 * _mean(sbr, 21) + _mean(sbr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# wide-bar volume confirmation ratio: vol on wide bars vs vol on narrow bars, 63d
def f13cr_f13_candle_range_structure_volconfratio_63d_base_v146_signal(high, low, volume):
    rngz = _z(_f13_range(high, low), 63)
    wide = (rngz > 0.5)
    narrow = (rngz < -0.5)
    vw = volume.where(wide).rolling(63, min_periods=15).mean()
    vn = volume.where(narrow).rolling(63, min_periods=15).mean().replace(0, np.nan)
    b = vw / vn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# closing momentum quality: signed CLV times body/range (decisive accumulation), 21d
def f13cr_f13_candle_range_structure_clvquality_21d_base_v147_signal(open, high, low, close):
    clv = _f13_clv(high, low, close)
    br = _f13_body_ratio(open, high, low, close)
    b = _mean(clv * br, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tail-heaviness: kurtosis of range% over 63d (fat-tailed range regime)
def f13cr_f13_candle_range_structure_rngkurt_63d_base_v148_signal(high, low, close):
    rp = _f13_range_pct(high, low, close)
    b = rp.rolling(63, min_periods=21).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-direction skew: skew of signed body/range over 63d (asymmetric thrust)
def f13cr_f13_candle_range_structure_bodyskew_63d_base_v149_signal(open, high, low, close):
    rng = (high - low).replace(0, np.nan)
    sbr = (close - open) / rng
    b = sbr.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined exhaustion: wide-range + long opposing wick + volume, 63d intensity
def f13cr_f13_candle_range_structure_exhcombo_63d_base_v150_signal(open, high, low, close, volume):
    rngz = _z(_f13_range(high, low), 126).clip(lower=0)
    uw = _f13_upper_wick_ratio(open, high, low, close)
    volz = _z(volume, 126).clip(lower=0)
    combo = rngz * uw * volz
    b = _mean(combo, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f13cr_f13_candle_range_structure_bodyrng_63d_base_v076_signal,
    f13cr_f13_candle_range_structure_bodyrng_126d_base_v077_signal,
    f13cr_f13_candle_range_structure_trpct_21d_base_v078_signal,
    f13cr_f13_candle_range_structure_trgap_21d_base_v079_signal,
    f13cr_f13_candle_range_structure_cir_63d_base_v080_signal,
    f13cr_f13_candle_range_structure_cir_126d_base_v081_signal,
    f13cr_f13_candle_range_structure_uwick_63d_base_v082_signal,
    f13cr_f13_candle_range_structure_lwick_63d_base_v083_signal,
    f13cr_f13_candle_range_structure_clv_21d_base_v084_signal,
    f13cr_f13_candle_range_structure_clv_63d_base_v085_signal,
    f13cr_f13_candle_range_structure_rngpct_63d_base_v086_signal,
    f13cr_f13_candle_range_structure_rngpct_126d_base_v087_signal,
    f13cr_f13_candle_range_structure_rngcov_63d_base_v088_signal,
    f13cr_f13_candle_range_structure_brcov_63d_base_v089_signal,
    f13cr_f13_candle_range_structure_bodyoverlap_21d_base_v090_signal,
    f13cr_f13_candle_range_structure_rngoverlap_21d_base_v091_signal,
    f13cr_f13_candle_range_structure_gapup_21d_base_v092_signal,
    f13cr_f13_candle_range_structure_gapdn_21d_base_v093_signal,
    f13cr_f13_candle_range_structure_gapfill_21d_base_v094_signal,
    f13cr_f13_candle_range_structure_gapfade_21d_base_v095_signal,
    f13cr_f13_candle_range_structure_wickasym_21d_base_v096_signal,
    f13cr_f13_candle_range_structure_totwick_63d_base_v097_signal,
    f13cr_f13_candle_range_structure_cirtrend_base_v098_signal,
    f13cr_f13_candle_range_structure_brtrend_base_v099_signal,
    f13cr_f13_candle_range_structure_rngvolcorr_63d_base_v100_signal,
    f13cr_f13_candle_range_structure_cirvolcorr_63d_base_v101_signal,
    f13cr_f13_candle_range_structure_vwrngexp_21d_base_v102_signal,
    f13cr_f13_candle_range_structure_rngshock_21d_base_v103_signal,
    f13cr_f13_candle_range_structure_rngsqueeze_21d_base_v104_signal,
    f13cr_f13_candle_range_structure_bodytr_21d_base_v105_signal,
    f13cr_f13_candle_range_structure_cirautocorr_63d_base_v106_signal,
    f13cr_f13_candle_range_structure_rngmeanrev_63d_base_v107_signal,
    f13cr_f13_candle_range_structure_strongvol_63d_base_v108_signal,
    f13cr_f13_candle_range_structure_weakvol_63d_base_v109_signal,
    f13cr_f13_candle_range_structure_rngrank_504d_base_v110_signal,
    f13cr_f13_candle_range_structure_dirrng_63d_base_v111_signal,
    f13cr_f13_candle_range_structure_wicktrend_base_v112_signal,
    f13cr_f13_candle_range_structure_rejhi_63d_base_v113_signal,
    f13cr_f13_candle_range_structure_demlo_63d_base_v114_signal,
    f13cr_f13_candle_range_structure_rngburst_21d_base_v115_signal,
    f13cr_f13_candle_range_structure_bodymag_21d_base_v116_signal,
    f13cr_f13_candle_range_structure_sbodymag_21d_base_v117_signal,
    f13cr_f13_candle_range_structure_bodymagz_base_v118_signal,
    f13cr_f13_candle_range_structure_upcandle_63d_base_v119_signal,
    f13cr_f13_candle_range_structure_opendrive_21d_base_v120_signal,
    f13cr_f13_candle_range_structure_intrarecov_21d_base_v121_signal,
    f13cr_f13_candle_range_structure_shapeentropy_21d_base_v122_signal,
    f13cr_f13_candle_range_structure_closedisc_63d_base_v123_signal,
    f13cr_f13_candle_range_structure_clvtrend_base_v124_signal,
    f13cr_f13_candle_range_structure_clvz_base_v125_signal,
    f13cr_f13_candle_range_structure_closetoext_21d_base_v126_signal,
    f13cr_f13_candle_range_structure_widebias_63d_base_v127_signal,
    f13cr_f13_candle_range_structure_rngslopeprox_base_v128_signal,
    f13cr_f13_candle_range_structure_exhaust_21d_base_v129_signal,
    f13cr_f13_candle_range_structure_cir3mom_21d_base_v130_signal,
    f13cr_f13_candle_range_structure_rngbodydiv_21d_base_v131_signal,
    f13cr_f13_candle_range_structure_effort_63d_base_v132_signal,
    f13cr_f13_candle_range_structure_climaxcnt_63d_base_v133_signal,
    f13cr_f13_candle_range_structure_edgeclose_63d_base_v134_signal,
    f13cr_f13_candle_range_structure_clustshift_base_v135_signal,
    f13cr_f13_candle_range_structure_clvtyp_21d_base_v136_signal,
    f13cr_f13_candle_range_structure_wideasym_63d_base_v137_signal,
    f13cr_f13_candle_range_structure_brrank_504d_base_v138_signal,
    f13cr_f13_candle_range_structure_squeeze_5v126_base_v139_signal,
    f13cr_f13_candle_range_structure_rangevol_21d_base_v140_signal,
    f13cr_f13_candle_range_structure_excbal_63d_base_v141_signal,
    f13cr_f13_candle_range_structure_gapinbar_63d_base_v142_signal,
    f13cr_f13_candle_range_structure_cirvolreg_base_v143_signal,
    f13cr_f13_candle_range_structure_overup_21d_base_v144_signal,
    f13cr_f13_candle_range_structure_bodyaccel_base_v145_signal,
    f13cr_f13_candle_range_structure_volconfratio_63d_base_v146_signal,
    f13cr_f13_candle_range_structure_clvquality_21d_base_v147_signal,
    f13cr_f13_candle_range_structure_rngkurt_63d_base_v148_signal,
    f13cr_f13_candle_range_structure_bodyskew_63d_base_v149_signal,
    f13cr_f13_candle_range_structure_exhcombo_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_CANDLE_RANGE_STRUCTURE_REGISTRY_076_150 = REGISTRY


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

    print("OK f13_candle_range_structure_base_076_150_claude: %d features pass" % n_features)
