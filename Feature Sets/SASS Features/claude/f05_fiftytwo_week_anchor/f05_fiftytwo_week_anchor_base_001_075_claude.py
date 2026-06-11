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


# ===== folder domain primitives (52-week / multi-year anchoring) =====
def _f05_prox_high(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return close / hi.replace(0, np.nan)


def _f05_prox_low(close, w):
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return close / lo.replace(0, np.nan)


def _f05_range_pos(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return (close - lo) / (hi - lo).replace(0, np.nan)


def _f05_drawdown(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return close / hi.replace(0, np.nan) - 1.0


def _f05_recovery(close, w):
    lo = close.rolling(w, min_periods=max(1, w // 2)).min()
    return close / lo.replace(0, np.nan) - 1.0


def _f05_anchor_gap(close, w):
    hi = close.rolling(w, min_periods=max(1, w // 2)).max()
    return np.log(close.replace(0, np.nan) / hi.replace(0, np.nan))


def _f05_days_since_high(close, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmax(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


def _f05_days_since_low(close, w):
    def _f(a):
        return (len(a) - 1 - int(np.argmin(a))) / float(len(a))
    return close.rolling(w, min_periods=max(1, w // 2)).apply(_f, raw=True)


# ============================================================
# proximity to 252d high
def f05fw_f05_fiftytwo_week_anchor_proxhi_252d_base_v001_signal(closeadj):
    b = _f05_prox_high(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity to 504d high, z-scored vs its own 252d history (de-trended level)
def f05fw_f05_fiftytwo_week_anchor_proxhi_504d_base_v002_signal(closeadj):
    p = _f05_prox_high(closeadj, 504)
    b = _z(p, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-year anchor memory: close vs the 1260d high as it stood one year ago
def f05fw_f05_fiftytwo_week_anchor_proxhi_1260d_base_v003_signal(closeadj):
    hi1260_lag = _rmax(closeadj, 1260).shift(252)
    b = np.log(closeadj.replace(0, np.nan) / hi1260_lag.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity to 252d low
def f05fw_f05_fiftytwo_week_anchor_proxlo_252d_base_v004_signal(closeadj):
    b = _f05_prox_low(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity to 504d low, z-scored vs its own 252d history
def f05fw_f05_fiftytwo_week_anchor_proxlo_504d_base_v005_signal(closeadj):
    p = _f05_prox_low(closeadj, 504)
    b = _z(p, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity to 1260d low, percentile-ranked vs its own 504d history
def f05fw_f05_fiftytwo_week_anchor_proxlo_1260d_base_v006_signal(closeadj):
    p = _f05_prox_low(closeadj, 1260)
    b = p.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring gap mean-reversion: 252d gap minus its own 63d average
def f05fw_f05_fiftytwo_week_anchor_anchgap_252d_base_v007_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 252)
    b = g - g.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring gap 504d mean-reversion vs its 126d average
def f05fw_f05_fiftytwo_week_anchor_anchgap_504d_base_v008_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 504)
    b = g - g.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring gap 1260d mean-reversion vs its 252d average (multi-year)
def f05fw_f05_fiftytwo_week_anchor_anchgap_1260d_base_v009_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 1260)
    b = g - g.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# underwater duration: fraction of the last year spent >5% below the 252d high
def f05fw_f05_fiftytwo_week_anchor_dd_252d_base_v010_signal(closeadj):
    roll_peak = closeadj.rolling(252, min_periods=126).max()
    underwater = closeadj / roll_peak.replace(0, np.nan) - 1.0
    deep = (underwater <= -0.05).astype(float)
    dur = deep.rolling(252, min_periods=126).mean()
    b = dur + 2.0 * underwater.rolling(21, min_periods=10).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# avg underwater depth (pain index) over the trailing 504d window
def f05fw_f05_fiftytwo_week_anchor_dd_504d_base_v011_signal(closeadj):
    roll_peak = closeadj.rolling(504, min_periods=252).max()
    underwater = closeadj / roll_peak.replace(0, np.nan) - 1.0
    b = underwater.rolling(504, min_periods=252).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery off 252d low scaled by elapsed time since that low (recovery rate)
def f05fw_f05_fiftytwo_week_anchor_recov_252d_base_v012_signal(closeadj):
    rec = _f05_recovery(closeadj, 252)
    dsl = _f05_days_since_low(closeadj, 252).replace(0, np.nan)
    b = rec / dsl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery off 504d low scaled by elapsed time since that low
def f05fw_f05_fiftytwo_week_anchor_recov_504d_base_v013_signal(closeadj):
    rec = _f05_recovery(closeadj, 504)
    dsl = _f05_days_since_low(closeadj, 504).replace(0, np.nan)
    b = rec / dsl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery off 1260d low scaled by elapsed time since that low
def f05fw_f05_fiftytwo_week_anchor_recov_1260d_base_v014_signal(closeadj):
    rec = _f05_recovery(closeadj, 1260)
    dsl = _f05_days_since_low(closeadj, 1260).replace(0, np.nan)
    b = rec / dsl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# % of 52w range (position within 252d range)
def f05fw_f05_fiftytwo_week_anchor_rngpos_252d_base_v015_signal(closeadj):
    b = _f05_range_pos(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# % of 504d range, z-scored vs its own 126d history (de-trended anchor position)
def f05fw_f05_fiftytwo_week_anchor_rngpos_504d_base_v016_signal(closeadj):
    rp = _f05_range_pos(closeadj, 504)
    b = _z(rp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# % of 1260d range, percentile-ranked vs its own 504d history (multi-year)
def f05fw_f05_fiftytwo_week_anchor_rngpos_1260d_base_v017_signal(closeadj):
    rp = _f05_range_pos(closeadj, 1260)
    b = rp.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since 252d high (staleness of the anchor)
def f05fw_f05_fiftytwo_week_anchor_dsh_252d_base_v018_signal(closeadj):
    b = _f05_days_since_high(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since 504d high
def f05fw_f05_fiftytwo_week_anchor_dsh_504d_base_v019_signal(closeadj):
    b = _f05_days_since_high(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since 252d low
def f05fw_f05_fiftytwo_week_anchor_dsl_252d_base_v020_signal(closeadj):
    b = _f05_days_since_low(closeadj, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since 504d low
def f05fw_f05_fiftytwo_week_anchor_dsl_504d_base_v021_signal(closeadj):
    b = _f05_days_since_low(closeadj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true-range 52w position (intraday hi/lo) z-scored vs its 126d history
def f05fw_f05_fiftytwo_week_anchor_hlrngpos_252d_base_v022_signal(closeadj, high, low):
    hi = high.rolling(252, min_periods=126).max()
    lo = low.rolling(252, min_periods=126).min()
    rp = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    b = _z(rp, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-high drawdown gap relative to the close-based drawdown (true-high premium)
def f05fw_f05_fiftytwo_week_anchor_hidd_252d_base_v023_signal(closeadj, high):
    hi_true = high.rolling(252, min_periods=126).max()
    hi_close = closeadj.rolling(252, min_periods=126).max()
    b = (hi_true - hi_close) / hi_close.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-low recovery gap relative to close-based low (true-low discount)
def f05fw_f05_fiftytwo_week_anchor_lorecov_252d_base_v024_signal(closeadj, low):
    lo_true = low.rolling(252, min_periods=126).min()
    lo_close = closeadj.rolling(252, min_periods=126).min()
    b = (lo_close - lo_true) / lo_close.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position z-scored vs own 252d history (anchoring extremity)
def f05fw_f05_fiftytwo_week_anchor_rngposz_252d_base_v025_signal(closeadj):
    rp = _f05_range_pos(closeadj, 252)
    b = _z(rp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring gap z-scored vs own history
def f05fw_f05_fiftytwo_week_anchor_anchgapz_252d_base_v026_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 252)
    b = _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# spread: 252d range-pos minus 1260d range-pos (short anchor vs long anchor)
def f05fw_f05_fiftytwo_week_anchor_rngposspr_252v1260_base_v027_signal(closeadj):
    s = _f05_range_pos(closeadj, 252)
    l = _f05_range_pos(closeadj, 1260)
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown asymmetry: 252d drawdown relative to the deeper 504d drawdown (ratio)
def f05fw_f05_fiftytwo_week_anchor_ddspr_252v504_base_v028_signal(closeadj):
    s = _f05_drawdown(closeadj, 252)
    l = _f05_drawdown(closeadj, 504)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# V-shape balance change: how the recovery/drawdown balance shifted over a quarter
def f05fw_f05_fiftytwo_week_anchor_vshape_252d_base_v029_signal(closeadj):
    rec = _f05_recovery(closeadj, 252)
    dd = _f05_drawdown(closeadj, 252).abs()
    bal = (rec - dd) / (rec + dd).replace(0, np.nan)
    b = bal - bal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity-to-high momentum: change in proximity over a quarter
def f05fw_f05_fiftytwo_week_anchor_proxhimom_252d_base_v030_signal(closeadj):
    p = _f05_prox_high(closeadj, 252)
    b = p - p.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-52w-high frequency over the last quarter, weighted by proximity depth
def f05fw_f05_fiftytwo_week_anchor_newhifreq_252d_base_v031_signal(closeadj):
    hi = closeadj.rolling(252, min_periods=126).max()
    is_high = (closeadj >= hi * 0.99999).astype(float)
    freq = is_high.rolling(63, min_periods=21).mean()
    prox = closeadj / hi.replace(0, np.nan)
    b = freq + 0.25 * prox
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# new-52w-low frequency over the last quarter, weighted by proximity depth
def f05fw_f05_fiftytwo_week_anchor_newlofreq_252d_base_v032_signal(closeadj):
    lo = closeadj.rolling(252, min_periods=126).min()
    is_low = (closeadj <= lo * 1.00001).astype(float)
    freq = is_low.rolling(63, min_periods=21).mean()
    prox = lo.replace(0, np.nan) / closeadj.replace(0, np.nan)
    b = freq + 0.25 * prox
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring gap per unit of risk, percentile-ranked vs its own 252d history
def f05fw_f05_fiftytwo_week_anchor_gapvol_252d_base_v033_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    ratio = g / vol.replace(0, np.nan)
    b = ratio.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# risk-adjusted recovery z-scored vs its own history (de-trended)
def f05fw_f05_fiftytwo_week_anchor_recovvol_252d_base_v034_signal(closeadj):
    rec = _f05_recovery(closeadj, 252)
    vol = closeadj.pct_change().rolling(63, min_periods=21).std()
    ratio = rec / vol.replace(0, np.nan)
    b = _z(ratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# compression of the 504d anchoring gap relative to its 252d typical depth
def f05fw_f05_fiftytwo_week_anchor_gapsignmag_504d_base_v035_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 504)
    typ = g.rolling(252, min_periods=126).mean()
    b = np.sign(g) * (g.abs() ** 0.5) - np.sign(typ) * (typ.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position rank vs cross-time history (percentile of where in range)
def f05fw_f05_fiftytwo_week_anchor_rngpoprank_252d_base_v036_signal(closeadj):
    rp = _f05_range_pos(closeadj, 252)
    b = rp.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance to 252d high in ATR units, change over a quarter (approach/retreat speed)
def f05fw_f05_fiftytwo_week_anchor_gapatr_252d_base_v037_signal(closeadj, high, low):
    hi = closeadj.rolling(252, min_periods=126).max()
    atr = (high - low).rolling(21, min_periods=5).mean()
    ratio = (closeadj - hi) / atr.replace(0, np.nan)
    b = ratio - ratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance between price and 252d low relative to ATR
def f05fw_f05_fiftytwo_week_anchor_lowgapatr_252d_base_v038_signal(closeadj, high, low):
    lo = closeadj.rolling(252, min_periods=126).min()
    atr = (high - low).rolling(21, min_periods=5).mean()
    b = (closeadj - lo) / atr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mid-range skew momentum: how the 252d midpoint position moved over a month
def f05fw_f05_fiftytwo_week_anchor_midskew_252d_base_v039_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    mid = (hi + lo) / 2.0
    skew = (closeadj - mid) / (hi - lo).replace(0, np.nan)
    b = skew - skew.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how fast the 1260d high is climbing (new-high creation rate, log-slope of rolling max)
def f05fw_f05_fiftytwo_week_anchor_midskew_1260d_base_v040_signal(closeadj):
    hi = _rmax(closeadj, 1260)
    b = np.log(hi.replace(0, np.nan) / hi.shift(63).replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity-to-high persistence: avg distance-above-95%-band when near the high
def f05fw_f05_fiftytwo_week_anchor_nearhipersist_252d_base_v041_signal(closeadj):
    hi = closeadj.rolling(252, min_periods=126).max()
    excess = (closeadj / hi.replace(0, np.nan) - 0.95).clip(lower=0)
    b = excess.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity-to-low persistence: avg distance-below-105%-band when near the low
def f05fw_f05_fiftytwo_week_anchor_nearlopersist_252d_base_v042_signal(closeadj):
    lo = closeadj.rolling(252, min_periods=126).min()
    excess = (1.05 - closeadj / lo.replace(0, np.nan)).clip(lower=0)
    b = excess.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed anchoring-gap momentum (bounded change in the anchoring gap)
def f05fw_f05_fiftytwo_week_anchor_gaptanh_252d_base_v043_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 252)
    chg = g - g.shift(21)
    b = np.tanh(20.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery off low relative to total range traveled (path normalization)
def f05fw_f05_fiftytwo_week_anchor_recovrng_504d_base_v044_signal(closeadj):
    lo = _rmin(closeadj, 504)
    hi = _rmax(closeadj, 504)
    b = (closeadj - lo) / (hi - lo).replace(0, np.nan) * (closeadj / lo.replace(0, np.nan) - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown depth x time-since-high (deep & stale anchor)
def f05fw_f05_fiftytwo_week_anchor_ddstale_252d_base_v045_signal(closeadj):
    dd = _f05_drawdown(closeadj, 252)
    dsh = _f05_days_since_high(closeadj, 252)
    b = dd * dsh
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range position change over a month (anchoring momentum)
def f05fw_f05_fiftytwo_week_anchor_rngposchg_504d_base_v046_signal(closeadj):
    rp = _f05_range_pos(closeadj, 504)
    b = rp - rp.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# is the 252d high also the 504d high? ratio of the two highs (anchor freshness)
def f05fw_f05_fiftytwo_week_anchor_proxhispr_252v504_base_v047_signal(closeadj):
    hi252 = _rmax(closeadj, 252)
    hi504 = _rmax(closeadj, 504)
    fresh = hi252 / hi504.replace(0, np.nan)
    b = _z(fresh, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# persistence of fresh-anchor regime: fraction of last quarter the 252d high == 504d high
def f05fw_f05_fiftytwo_week_anchor_anchdist_252d_base_v048_signal(closeadj):
    hi252 = _rmax(closeadj, 252)
    hi504 = _rmax(closeadj, 504)
    is_fresh = (hi252 >= hi504 * 0.99999).astype(float)
    raw = is_fresh.rolling(63, min_periods=21).mean()
    dd = _f05_drawdown(closeadj, 252)
    b = raw + 0.5 * dd
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# span of the multi-year range: where the 1260d high sits above the 252d low
def f05fw_f05_fiftytwo_week_anchor_anchdist_1260d_base_v049_signal(closeadj):
    hi1260 = _rmax(closeadj, 1260)
    lo252 = _rmin(closeadj, 252)
    b = np.log(hi1260.replace(0, np.nan) / lo252.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how stretched the 252d high is above the 252d mean (anchor extension)
def f05fw_f05_fiftytwo_week_anchor_hiextend_252d_base_v050_signal(closeadj):
    hi = _rmax(closeadj, 252)
    mn = _mean(closeadj, 252)
    b = (hi - mn) / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how stretched the 252d low is below the 252d mean
def f05fw_f05_fiftytwo_week_anchor_loextend_252d_base_v051_signal(closeadj):
    lo = _rmin(closeadj, 252)
    mn = _mean(closeadj, 252)
    b = (mn - lo) / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range amplitude (52w high-low spread) normalized by price
def f05fw_f05_fiftytwo_week_anchor_amplitude_252d_base_v052_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    b = (hi - lo) / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range amplitude 1260d
def f05fw_f05_fiftytwo_week_anchor_amplitude_1260d_base_v053_signal(closeadj):
    hi = _rmax(closeadj, 1260)
    lo = _rmin(closeadj, 1260)
    b = (hi - lo) / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# top-hug convexity change: how the squared upper-range bias shifted over a month
def f05fw_f05_fiftytwo_week_anchor_tophug_252d_base_v054_signal(closeadj):
    rp = _f05_range_pos(closeadj, 252)
    conv = np.sign(rp - 0.5) * (rp - 0.5) ** 2 * 4.0
    b = conv - conv.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# long anchor gap per unit of risk, z-scored vs its 252d history (de-trended)
def f05fw_f05_fiftytwo_week_anchor_longgapvol_1260d_base_v055_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 1260)
    vol = closeadj.pct_change().rolling(126, min_periods=63).std()
    ratio = g / vol.replace(0, np.nan)
    b = ratio - ratio.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# headroom above the prior 252d high, z-scored vs its own 63d history (de-trended)
def f05fw_f05_fiftytwo_week_anchor_hibreakext_252d_base_v056_signal(closeadj):
    prior_hi = closeadj.shift(1).rolling(252, min_periods=126).max()
    raw = closeadj / prior_hi.replace(0, np.nan) - 1.0
    b = _z(raw, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cushion above the prior 252d low, z-scored vs its own 63d history (de-trended)
def f05fw_f05_fiftytwo_week_anchor_lobreakext_252d_base_v057_signal(closeadj):
    prior_lo = closeadj.shift(1).rolling(252, min_periods=126).min()
    raw = closeadj / prior_lo.replace(0, np.nan) - 1.0
    b = -_z(raw, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range position smoothed (persistent anchor position)
def f05fw_f05_fiftytwo_week_anchor_rngposema_252d_base_v058_signal(closeadj):
    rp = _f05_range_pos(closeadj, 252)
    b = rp.ewm(span=42, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# difference: range-pos minus its own slow EMA (anchor displacement)
def f05fw_f05_fiftytwo_week_anchor_rngposdisp_252d_base_v059_signal(closeadj):
    rp = _f05_range_pos(closeadj, 252)
    b = rp - rp.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery off 252d low, smoothed and ranked
def f05fw_f05_fiftytwo_week_anchor_recovrank_252d_base_v060_signal(closeadj):
    rec = _f05_recovery(closeadj, 252)
    b = rec.rolling(504, min_periods=126).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multi-anchor disagreement: spread between nearest and farthest high-proximity
def f05fw_f05_fiftytwo_week_anchor_multinearhi_base_v061_signal(closeadj):
    h1 = closeadj.rolling(252, min_periods=126).max()
    h2 = closeadj.rolling(504, min_periods=252).max()
    h3 = closeadj.rolling(1260, min_periods=504).max()
    p1 = closeadj / h1.replace(0, np.nan)
    p2 = closeadj / h2.replace(0, np.nan)
    p3 = closeadj / h3.replace(0, np.nan)
    stacked = pd.concat([p1, p2, p3], axis=1)
    b = stacked.max(axis=1) - stacked.min(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# drawdown-episode frequency: how often price dips >10% below the 252d high
def f05fw_f05_fiftytwo_week_anchor_multidd_base_v062_signal(closeadj):
    dd = _f05_drawdown(closeadj, 252)
    in_dd = (dd <= -0.10).astype(float)
    entries = ((in_dd == 1) & (in_dd.shift(1) == 0)).astype(float)
    b = entries.rolling(252, min_periods=126).sum() + dd.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring gap acceleration of recovery: recovery now vs recovery a quarter ago
def f05fw_f05_fiftytwo_week_anchor_recovmom_504d_base_v063_signal(closeadj):
    rec = _f05_recovery(closeadj, 504)
    b = rec - rec.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of the last year spent in the upper third of the 52w range
def f05fw_f05_fiftytwo_week_anchor_uppertime_252d_base_v064_signal(closeadj):
    rp = _f05_range_pos(closeadj, 252)
    upper = (rp >= 0.6667).astype(float)
    b = upper.rolling(252, min_periods=126).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# entries into the lower third of the 52w range over the last year (capitulation count)
def f05fw_f05_fiftytwo_week_anchor_lowertime_252d_base_v065_signal(closeadj):
    rp = _f05_range_pos(closeadj, 252)
    lower = (rp <= 0.3333).astype(float)
    entries = ((lower == 1) & (lower.shift(1) == 0)).astype(float)
    rate = entries.rolling(252, min_periods=126).sum()
    depth = (0.3333 - rp).clip(lower=0).rolling(63, min_periods=21).mean()
    b = rate + 10.0 * depth
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchoring gap relative to the gap one year ago (year-over-year anchor change)
def f05fw_f05_fiftytwo_week_anchor_gapyoy_252d_base_v066_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 252)
    b = g - g.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-high 52w proximity (true highs), z-scored vs its own 126d history
def f05fw_f05_fiftytwo_week_anchor_trueproxhi_252d_base_v067_signal(closeadj, high):
    hi = high.rolling(252, min_periods=126).max()
    p = closeadj / hi.replace(0, np.nan)
    b = _z(p, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-low 52w proximity (true lows), percentile-ranked vs its 252d history
def f05fw_f05_fiftytwo_week_anchor_trueproxlo_252d_base_v068_signal(closeadj, low):
    lo = low.rolling(252, min_periods=126).min()
    p = closeadj / lo.replace(0, np.nan)
    b = p.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchor gap measured to 1260d high but in 504d-vol units (deep value anchor)
def f05fw_f05_fiftytwo_week_anchor_deepanchz_1260d_base_v069_signal(closeadj):
    g = _f05_anchor_gap(closeadj, 1260)
    b = _z(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position dispersion across 252/504/1260 (anchor disagreement)
def f05fw_f05_fiftytwo_week_anchor_rngposdisp_multi_base_v070_signal(closeadj):
    p1 = _f05_range_pos(closeadj, 252)
    p2 = _f05_range_pos(closeadj, 504)
    p3 = _f05_range_pos(closeadj, 1260)
    b = pd.concat([p1, p2, p3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# how quickly drawdown is deepening (drawdown delta over a month)
def f05fw_f05_fiftytwo_week_anchor_ddvelocity_252d_base_v071_signal(closeadj):
    dd = _f05_drawdown(closeadj, 252)
    b = dd - dd.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proximity-to-high weighted by how long it has held (sticky leadership)
def f05fw_f05_fiftytwo_week_anchor_stickytop_252d_base_v072_signal(closeadj):
    rp = _f05_range_pos(closeadj, 252)
    persist = (rp >= 0.8).astype(float).rolling(63, min_periods=21).mean()
    b = rp * persist
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 504d mid scaled by amplitude, smoothed (long anchoring bias)
def f05fw_f05_fiftytwo_week_anchor_midskewsm_504d_base_v073_signal(closeadj):
    hi = _rmax(closeadj, 504)
    lo = _rmin(closeadj, 504)
    mid = (hi + lo) / 2.0
    raw = (closeadj - mid) / (hi - lo).replace(0, np.nan)
    b = raw.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# combined V-recovery quality: recovery off low x time-since-low (matured rebound)
def f05fw_f05_fiftytwo_week_anchor_maturerebound_252d_base_v074_signal(closeadj):
    rec = _f05_recovery(closeadj, 252)
    dsl = _f05_days_since_low(closeadj, 252)
    b = rec * dsl
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# anchor-balance momentum: change in the 504d log-gap balance over a quarter
def f05fw_f05_fiftytwo_week_anchor_anchbalance_252d_base_v075_signal(closeadj):
    ghi = (-_f05_anchor_gap(closeadj, 504)).clip(lower=0)
    glo = np.log(closeadj.replace(0, np.nan) / _rmin(closeadj, 504).replace(0, np.nan)).clip(lower=0)
    bal = (glo - ghi) / (glo + ghi).replace(0, np.nan)
    b = bal - bal.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f05fw_f05_fiftytwo_week_anchor_proxhi_252d_base_v001_signal,
    f05fw_f05_fiftytwo_week_anchor_proxhi_504d_base_v002_signal,
    f05fw_f05_fiftytwo_week_anchor_proxhi_1260d_base_v003_signal,
    f05fw_f05_fiftytwo_week_anchor_proxlo_252d_base_v004_signal,
    f05fw_f05_fiftytwo_week_anchor_proxlo_504d_base_v005_signal,
    f05fw_f05_fiftytwo_week_anchor_proxlo_1260d_base_v006_signal,
    f05fw_f05_fiftytwo_week_anchor_anchgap_252d_base_v007_signal,
    f05fw_f05_fiftytwo_week_anchor_anchgap_504d_base_v008_signal,
    f05fw_f05_fiftytwo_week_anchor_anchgap_1260d_base_v009_signal,
    f05fw_f05_fiftytwo_week_anchor_dd_252d_base_v010_signal,
    f05fw_f05_fiftytwo_week_anchor_dd_504d_base_v011_signal,
    f05fw_f05_fiftytwo_week_anchor_recov_252d_base_v012_signal,
    f05fw_f05_fiftytwo_week_anchor_recov_504d_base_v013_signal,
    f05fw_f05_fiftytwo_week_anchor_recov_1260d_base_v014_signal,
    f05fw_f05_fiftytwo_week_anchor_rngpos_252d_base_v015_signal,
    f05fw_f05_fiftytwo_week_anchor_rngpos_504d_base_v016_signal,
    f05fw_f05_fiftytwo_week_anchor_rngpos_1260d_base_v017_signal,
    f05fw_f05_fiftytwo_week_anchor_dsh_252d_base_v018_signal,
    f05fw_f05_fiftytwo_week_anchor_dsh_504d_base_v019_signal,
    f05fw_f05_fiftytwo_week_anchor_dsl_252d_base_v020_signal,
    f05fw_f05_fiftytwo_week_anchor_dsl_504d_base_v021_signal,
    f05fw_f05_fiftytwo_week_anchor_hlrngpos_252d_base_v022_signal,
    f05fw_f05_fiftytwo_week_anchor_hidd_252d_base_v023_signal,
    f05fw_f05_fiftytwo_week_anchor_lorecov_252d_base_v024_signal,
    f05fw_f05_fiftytwo_week_anchor_rngposz_252d_base_v025_signal,
    f05fw_f05_fiftytwo_week_anchor_anchgapz_252d_base_v026_signal,
    f05fw_f05_fiftytwo_week_anchor_rngposspr_252v1260_base_v027_signal,
    f05fw_f05_fiftytwo_week_anchor_ddspr_252v504_base_v028_signal,
    f05fw_f05_fiftytwo_week_anchor_vshape_252d_base_v029_signal,
    f05fw_f05_fiftytwo_week_anchor_proxhimom_252d_base_v030_signal,
    f05fw_f05_fiftytwo_week_anchor_newhifreq_252d_base_v031_signal,
    f05fw_f05_fiftytwo_week_anchor_newlofreq_252d_base_v032_signal,
    f05fw_f05_fiftytwo_week_anchor_gapvol_252d_base_v033_signal,
    f05fw_f05_fiftytwo_week_anchor_recovvol_252d_base_v034_signal,
    f05fw_f05_fiftytwo_week_anchor_gapsignmag_504d_base_v035_signal,
    f05fw_f05_fiftytwo_week_anchor_rngpoprank_252d_base_v036_signal,
    f05fw_f05_fiftytwo_week_anchor_gapatr_252d_base_v037_signal,
    f05fw_f05_fiftytwo_week_anchor_lowgapatr_252d_base_v038_signal,
    f05fw_f05_fiftytwo_week_anchor_midskew_252d_base_v039_signal,
    f05fw_f05_fiftytwo_week_anchor_midskew_1260d_base_v040_signal,
    f05fw_f05_fiftytwo_week_anchor_nearhipersist_252d_base_v041_signal,
    f05fw_f05_fiftytwo_week_anchor_nearlopersist_252d_base_v042_signal,
    f05fw_f05_fiftytwo_week_anchor_gaptanh_252d_base_v043_signal,
    f05fw_f05_fiftytwo_week_anchor_recovrng_504d_base_v044_signal,
    f05fw_f05_fiftytwo_week_anchor_ddstale_252d_base_v045_signal,
    f05fw_f05_fiftytwo_week_anchor_rngposchg_504d_base_v046_signal,
    f05fw_f05_fiftytwo_week_anchor_proxhispr_252v504_base_v047_signal,
    f05fw_f05_fiftytwo_week_anchor_anchdist_252d_base_v048_signal,
    f05fw_f05_fiftytwo_week_anchor_anchdist_1260d_base_v049_signal,
    f05fw_f05_fiftytwo_week_anchor_hiextend_252d_base_v050_signal,
    f05fw_f05_fiftytwo_week_anchor_loextend_252d_base_v051_signal,
    f05fw_f05_fiftytwo_week_anchor_amplitude_252d_base_v052_signal,
    f05fw_f05_fiftytwo_week_anchor_amplitude_1260d_base_v053_signal,
    f05fw_f05_fiftytwo_week_anchor_tophug_252d_base_v054_signal,
    f05fw_f05_fiftytwo_week_anchor_longgapvol_1260d_base_v055_signal,
    f05fw_f05_fiftytwo_week_anchor_hibreakext_252d_base_v056_signal,
    f05fw_f05_fiftytwo_week_anchor_lobreakext_252d_base_v057_signal,
    f05fw_f05_fiftytwo_week_anchor_rngposema_252d_base_v058_signal,
    f05fw_f05_fiftytwo_week_anchor_rngposdisp_252d_base_v059_signal,
    f05fw_f05_fiftytwo_week_anchor_recovrank_252d_base_v060_signal,
    f05fw_f05_fiftytwo_week_anchor_multinearhi_base_v061_signal,
    f05fw_f05_fiftytwo_week_anchor_multidd_base_v062_signal,
    f05fw_f05_fiftytwo_week_anchor_recovmom_504d_base_v063_signal,
    f05fw_f05_fiftytwo_week_anchor_uppertime_252d_base_v064_signal,
    f05fw_f05_fiftytwo_week_anchor_lowertime_252d_base_v065_signal,
    f05fw_f05_fiftytwo_week_anchor_gapyoy_252d_base_v066_signal,
    f05fw_f05_fiftytwo_week_anchor_trueproxhi_252d_base_v067_signal,
    f05fw_f05_fiftytwo_week_anchor_trueproxlo_252d_base_v068_signal,
    f05fw_f05_fiftytwo_week_anchor_deepanchz_1260d_base_v069_signal,
    f05fw_f05_fiftytwo_week_anchor_rngposdisp_multi_base_v070_signal,
    f05fw_f05_fiftytwo_week_anchor_ddvelocity_252d_base_v071_signal,
    f05fw_f05_fiftytwo_week_anchor_stickytop_252d_base_v072_signal,
    f05fw_f05_fiftytwo_week_anchor_midskewsm_504d_base_v073_signal,
    f05fw_f05_fiftytwo_week_anchor_maturerebound_252d_base_v074_signal,
    f05fw_f05_fiftytwo_week_anchor_anchbalance_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F05_FIFTYTWO_WEEK_ANCHOR_REGISTRY_001_075 = REGISTRY


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

    print("OK f05_fiftytwo_week_anchor_base_001_075_claude: %d features pass" % n_features)
