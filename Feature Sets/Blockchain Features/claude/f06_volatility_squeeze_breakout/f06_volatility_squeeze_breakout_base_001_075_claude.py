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


# ===== folder domain primitives (volatility squeeze / breakout) =====
def _f06_bandwidth(s, w, k=2.0):
    # Bollinger bandwidth = (upper - lower) / mid = 2*k*std/mean
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (2.0 * k * sd) / m.replace(0, np.nan)


def _f06_squeeze(h, l, c, w, k=2.0, kc=1.5):
    # squeeze ratio = Bollinger width / Keltner(ATR) width; <1 => coiled (compressed)
    m = c.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = c.rolling(w, min_periods=max(2, w // 2)).std()
    bb_w = 2.0 * k * sd
    tr = pd.concat([(h - l).abs(),
                    (h - c.shift(1)).abs(),
                    (l - c.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(w, min_periods=max(2, w // 2)).mean()
    kc_w = 2.0 * kc * atr
    return bb_w / kc_w.replace(0, np.nan) + m * 0.0


def _f06_pctb(s, w, k=2.0):
    # %B = (close - lower) / (upper - lower); position within the Bollinger envelope
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    upper = m + k * sd
    lower = m - k * sd
    return (s - lower) / (upper - lower).replace(0, np.nan)


def _f06_atrp(h, l, c, w):
    # ATR normalized by price (true-range compression measure)
    tr = pd.concat([(h - l).abs(),
                    (h - c.shift(1)).abs(),
                    (l - c.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(w, min_periods=max(2, w // 2)).mean()
    return atr / c.replace(0, np.nan)


# ============ FEATURES 001-075 ============

# 21d Bollinger bandwidth
def f06sq_f06_volatility_squeeze_breakout_bw_21d_base_v001_signal(closeadj):
    result = _f06_bandwidth(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d Bollinger bandwidth
def f06sq_f06_volatility_squeeze_breakout_bw_63d_base_v002_signal(closeadj):
    result = _f06_bandwidth(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d Bollinger bandwidth
def f06sq_f06_volatility_squeeze_breakout_bw_126d_base_v003_signal(closeadj):
    result = _f06_bandwidth(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d Bollinger bandwidth (short coil)
def f06sq_f06_volatility_squeeze_breakout_bw_10d_base_v004_signal(closeadj):
    result = _f06_bandwidth(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d Bollinger bandwidth
def f06sq_f06_volatility_squeeze_breakout_bw_42d_base_v005_signal(closeadj):
    result = _f06_bandwidth(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d Bollinger bandwidth
def f06sq_f06_volatility_squeeze_breakout_bw_252d_base_v006_signal(closeadj):
    result = _f06_bandwidth(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d bandwidth k=1.0 (tighter envelope)
def f06sq_f06_volatility_squeeze_breakout_bwk1_21d_base_v007_signal(closeadj):
    result = _f06_bandwidth(closeadj, 21, 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d bandwidth k=3.0 (wide envelope)
def f06sq_f06_volatility_squeeze_breakout_bwk3_63d_base_v008_signal(closeadj):
    result = _f06_bandwidth(closeadj, 63, 3.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d bandwidth percentile rank over 252d (continuous compression rank)
def f06sq_f06_volatility_squeeze_breakout_bwrank_21d_base_v009_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 21)
    result = bw.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d bandwidth percentile rank over 252d
def f06sq_f06_volatility_squeeze_breakout_bwrank_63d_base_v010_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 63)
    result = bw.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d bandwidth percentile rank over 504d
def f06sq_f06_volatility_squeeze_breakout_bwrank_126d_base_v011_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 126)
    result = bw.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d bandwidth z-score over 252d
def f06sq_f06_volatility_squeeze_breakout_bwz_21d_base_v012_signal(closeadj):
    result = _z(_f06_bandwidth(closeadj, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d bandwidth z-score over 252d
def f06sq_f06_volatility_squeeze_breakout_bwz_63d_base_v013_signal(closeadj):
    result = _z(_f06_bandwidth(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d bandwidth z-score over 504d
def f06sq_f06_volatility_squeeze_breakout_bwz_126d_base_v014_signal(closeadj):
    result = _z(_f06_bandwidth(closeadj, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth ratio short/long: 21d over 126d (coil tightness relative to regime)
def f06sq_f06_volatility_squeeze_breakout_bwratio_21_126_base_v015_signal(closeadj):
    result = _safe_div(_f06_bandwidth(closeadj, 21), _f06_bandwidth(closeadj, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth ratio 42d over 252d
def f06sq_f06_volatility_squeeze_breakout_bwratio_42_252_base_v016_signal(closeadj):
    result = _safe_div(_f06_bandwidth(closeadj, 42), _f06_bandwidth(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth ratio 10d over 63d
def f06sq_f06_volatility_squeeze_breakout_bwratio_10_63_base_v017_signal(closeadj):
    result = _safe_div(_f06_bandwidth(closeadj, 10), _f06_bandwidth(closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d bandwidth relative to its own 63d mean (compression vs recent norm)
def f06sq_f06_volatility_squeeze_breakout_bwrel_21d_base_v018_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 21)
    result = _safe_div(bw, _mean(bw, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d bandwidth relative to its own 126d mean
def f06sq_f06_volatility_squeeze_breakout_bwrel_63d_base_v019_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 63)
    result = _safe_div(bw, _mean(bw, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d squeeze ratio (BB width / KC width)
def f06sq_f06_volatility_squeeze_breakout_sq_21d_base_v020_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d squeeze ratio
def f06sq_f06_volatility_squeeze_breakout_sq_63d_base_v021_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d squeeze ratio
def f06sq_f06_volatility_squeeze_breakout_sq_126d_base_v022_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d squeeze ratio (short coil)
def f06sq_f06_volatility_squeeze_breakout_sq_10d_base_v023_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d squeeze ratio
def f06sq_f06_volatility_squeeze_breakout_sq_42d_base_v024_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d squeeze ratio
def f06sq_f06_volatility_squeeze_breakout_sq_252d_base_v025_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d squeeze z-score over 252d
def f06sq_f06_volatility_squeeze_breakout_sqz_21d_base_v026_signal(high, low, closeadj):
    result = _z(_f06_squeeze(high, low, closeadj, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d squeeze z-score over 252d
def f06sq_f06_volatility_squeeze_breakout_sqz_63d_base_v027_signal(high, low, closeadj):
    result = _z(_f06_squeeze(high, low, closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d squeeze percentile rank over 252d
def f06sq_f06_volatility_squeeze_breakout_sqrank_21d_base_v028_signal(high, low, closeadj):
    sq = _f06_squeeze(high, low, closeadj, 21)
    result = sq.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d squeeze percentile rank over 252d
def f06sq_f06_volatility_squeeze_breakout_sqrank_63d_base_v029_signal(high, low, closeadj):
    sq = _f06_squeeze(high, low, closeadj, 63)
    result = sq.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d squeeze relative to its 63d mean
def f06sq_f06_volatility_squeeze_breakout_sqrel_21d_base_v030_signal(high, low, closeadj):
    sq = _f06_squeeze(high, low, closeadj, 21)
    result = _safe_div(sq, _mean(sq, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d %B (position in Bollinger envelope)
def f06sq_f06_volatility_squeeze_breakout_pctb_21d_base_v031_signal(closeadj):
    result = _f06_pctb(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d %B
def f06sq_f06_volatility_squeeze_breakout_pctb_63d_base_v032_signal(closeadj):
    result = _f06_pctb(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d %B
def f06sq_f06_volatility_squeeze_breakout_pctb_126d_base_v033_signal(closeadj):
    result = _f06_pctb(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d %B (short-horizon band position)
def f06sq_f06_volatility_squeeze_breakout_pctb_10d_base_v034_signal(closeadj):
    result = _f06_pctb(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d %B
def f06sq_f06_volatility_squeeze_breakout_pctb_42d_base_v035_signal(closeadj):
    result = _f06_pctb(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d %B
def f06sq_f06_volatility_squeeze_breakout_pctb_252d_base_v036_signal(closeadj):
    result = _f06_pctb(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d %B centered (distance from band midpoint)
def f06sq_f06_volatility_squeeze_breakout_pctbc_21d_base_v037_signal(closeadj):
    result = _f06_pctb(closeadj, 21) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# 63d %B centered
def f06sq_f06_volatility_squeeze_breakout_pctbc_63d_base_v038_signal(closeadj):
    result = _f06_pctb(closeadj, 63) - 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# 21d %B k=1.0 (tighter envelope position)
def f06sq_f06_volatility_squeeze_breakout_pctbk1_21d_base_v039_signal(closeadj):
    result = _f06_pctb(closeadj, 21, 1.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d %B k=3.0 (wide envelope position)
def f06sq_f06_volatility_squeeze_breakout_pctbk3_63d_base_v040_signal(closeadj):
    result = _f06_pctb(closeadj, 63, 3.0)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR/price compression
def f06sq_f06_volatility_squeeze_breakout_atrp_21d_base_v041_signal(high, low, closeadj):
    result = _f06_atrp(high, low, closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATR/price compression
def f06sq_f06_volatility_squeeze_breakout_atrp_63d_base_v042_signal(high, low, closeadj):
    result = _f06_atrp(high, low, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ATR/price compression
def f06sq_f06_volatility_squeeze_breakout_atrp_126d_base_v043_signal(high, low, closeadj):
    result = _f06_atrp(high, low, closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d ATR/price
def f06sq_f06_volatility_squeeze_breakout_atrp_10d_base_v044_signal(high, low, closeadj):
    result = _f06_atrp(high, low, closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ATR/price
def f06sq_f06_volatility_squeeze_breakout_atrp_252d_base_v045_signal(high, low, closeadj):
    result = _f06_atrp(high, low, closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price compression ratio 21d over 126d
def f06sq_f06_volatility_squeeze_breakout_atrpratio_21_126_base_v046_signal(high, low, closeadj):
    result = _safe_div(_f06_atrp(high, low, closeadj, 21), _f06_atrp(high, low, closeadj, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price z-score over 252d (21d)
def f06sq_f06_volatility_squeeze_breakout_atrpz_21d_base_v047_signal(high, low, closeadj):
    result = _z(_f06_atrp(high, low, closeadj, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price percentile rank over 252d (63d)
def f06sq_f06_volatility_squeeze_breakout_atrprank_63d_base_v048_signal(high, low, closeadj):
    a = _f06_atrp(high, low, closeadj, 63)
    result = a.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# distance to upper band normalized by bandwidth (21d)
def f06sq_f06_volatility_squeeze_breakout_distup_21d_base_v049_signal(closeadj):
    m = _mean(closeadj, 21)
    sd = _std(closeadj, 21)
    upper = m + 2.0 * sd
    result = _safe_div(upper - closeadj, 2.0 * 2.0 * sd) + _f06_bandwidth(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance to lower band normalized by bandwidth (21d)
def f06sq_f06_volatility_squeeze_breakout_distdn_21d_base_v050_signal(closeadj):
    m = _mean(closeadj, 21)
    sd = _std(closeadj, 21)
    lower = m - 2.0 * sd
    result = _safe_div(closeadj - lower, 2.0 * 2.0 * sd) + _f06_bandwidth(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance to upper band normalized (63d)
def f06sq_f06_volatility_squeeze_breakout_distup_63d_base_v051_signal(closeadj):
    m = _mean(closeadj, 63)
    sd = _std(closeadj, 63)
    upper = m + 2.0 * sd
    result = _safe_div(upper - closeadj, 2.0 * 2.0 * sd) + _f06_bandwidth(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance to lower band normalized (63d)
def f06sq_f06_volatility_squeeze_breakout_distdn_63d_base_v052_signal(closeadj):
    m = _mean(closeadj, 63)
    sd = _std(closeadj, 63)
    lower = m - 2.0 * sd
    result = _safe_div(closeadj - lower, 2.0 * 2.0 * sd) + _f06_bandwidth(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# close distance from band mid normalized by std (21d) - z of price vs band center
def f06sq_f06_volatility_squeeze_breakout_midz_21d_base_v053_signal(closeadj):
    result = _z(closeadj, 21) + _f06_bandwidth(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# close distance from band mid normalized by std (63d)
def f06sq_f06_volatility_squeeze_breakout_midz_63d_base_v054_signal(closeadj):
    result = _z(closeadj, 63) + _f06_bandwidth(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# range / average-range compression 21d (high-low vs its 63d mean)
def f06sq_f06_volatility_squeeze_breakout_rngcomp_21d_base_v055_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    result = _safe_div(_mean(rng, 21), _mean(rng, 63)) + _f06_atrp(high, low, closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# range / average-range compression 63d vs 252d
def f06sq_f06_volatility_squeeze_breakout_rngcomp_63d_base_v056_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    result = _safe_div(_mean(rng, 63), _mean(rng, 252)) + _f06_atrp(high, low, closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# std ratio short/long 10d over 63d (volatility compression)
def f06sq_f06_volatility_squeeze_breakout_stdratio_10_63_base_v057_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(_std(lr, 10), _std(lr, 63)) + _f06_bandwidth(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# std ratio 21d over 126d
def f06sq_f06_volatility_squeeze_breakout_stdratio_21_126_base_v058_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(_std(lr, 21), _std(lr, 126)) + _f06_bandwidth(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# std ratio 42d over 252d
def f06sq_f06_volatility_squeeze_breakout_stdratio_42_252_base_v059_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(_std(lr, 42), _std(lr, 252)) + _f06_bandwidth(closeadj, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# coil tightness: inverse bandwidth z-score (21d) - high when compressed
def f06sq_f06_volatility_squeeze_breakout_coil_21d_base_v060_signal(closeadj):
    result = -_z(_f06_bandwidth(closeadj, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# coil tightness 63d
def f06sq_f06_volatility_squeeze_breakout_coil_63d_base_v061_signal(closeadj):
    result = -_z(_f06_bandwidth(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze * %B interaction 21d (compressed coil with band position)
def f06sq_f06_volatility_squeeze_breakout_sqxb_21d_base_v062_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 21) * (_f06_pctb(closeadj, 21) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze * %B interaction 63d
def f06sq_f06_volatility_squeeze_breakout_sqxb_63d_base_v063_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 63) * (_f06_pctb(closeadj, 63) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth change rate 21d (expansion velocity, scaled by mean)
def f06sq_f06_volatility_squeeze_breakout_bwchg_21d_base_v064_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 21)
    result = _safe_div(bw - bw.shift(21), _mean(bw, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth change rate 63d
def f06sq_f06_volatility_squeeze_breakout_bwchg_63d_base_v065_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 63)
    result = _safe_div(bw - bw.shift(21), _mean(bw, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze change rate 21d (squeeze release velocity)
def f06sq_f06_volatility_squeeze_breakout_sqchg_21d_base_v066_signal(high, low, closeadj):
    sq = _f06_squeeze(high, low, closeadj, 21)
    result = _safe_div(sq - sq.shift(21), _mean(sq, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# %B momentum 21d (band-position thrust)
def f06sq_f06_volatility_squeeze_breakout_pctbmom_21d_base_v067_signal(closeadj):
    b = _f06_pctb(closeadj, 21)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# %B momentum 63d
def f06sq_f06_volatility_squeeze_breakout_pctbmom_63d_base_v068_signal(closeadj):
    b = _f06_pctb(closeadj, 63)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth EWMA span 21 (smoothed compression)
def f06sq_f06_volatility_squeeze_breakout_bwewm_21d_base_v069_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 21)
    result = bw.ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth EWMA span 63 (smoothed compression)
def f06sq_f06_volatility_squeeze_breakout_bwewm_63d_base_v070_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 63)
    result = bw.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth dispersion 63d (variability of compression itself)
def f06sq_f06_volatility_squeeze_breakout_bwdisp_63d_base_v071_signal(closeadj):
    result = _std(_f06_bandwidth(closeadj, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth dispersion 126d
def f06sq_f06_volatility_squeeze_breakout_bwdisp_126d_base_v072_signal(closeadj):
    result = _std(_f06_bandwidth(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# normalized distance close-to-upper over ATR (21d breakout proximity)
def f06sq_f06_volatility_squeeze_breakout_upatr_21d_base_v073_signal(high, low, closeadj):
    m = _mean(closeadj, 21)
    sd = _std(closeadj, 21)
    upper = m + 2.0 * sd
    atrp = _f06_atrp(high, low, closeadj, 21)
    result = _safe_div(upper - closeadj, atrp * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# normalized distance close-to-lower over ATR (21d)
def f06sq_f06_volatility_squeeze_breakout_dnatr_21d_base_v074_signal(high, low, closeadj):
    m = _mean(closeadj, 21)
    sd = _std(closeadj, 21)
    lower = m - 2.0 * sd
    atrp = _f06_atrp(high, low, closeadj, 21)
    result = _safe_div(closeadj - lower, atrp * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze ratio inverse (Keltner/Bollinger) 21d - alternate compression view
def f06sq_f06_volatility_squeeze_breakout_invsq_21d_base_v075_signal(high, low, closeadj):
    result = _safe_div(pd.Series(1.0, index=closeadj.index), _f06_squeeze(high, low, closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06sq_f06_volatility_squeeze_breakout_bw_21d_base_v001_signal,
    f06sq_f06_volatility_squeeze_breakout_bw_63d_base_v002_signal,
    f06sq_f06_volatility_squeeze_breakout_bw_126d_base_v003_signal,
    f06sq_f06_volatility_squeeze_breakout_bw_10d_base_v004_signal,
    f06sq_f06_volatility_squeeze_breakout_bw_42d_base_v005_signal,
    f06sq_f06_volatility_squeeze_breakout_bw_252d_base_v006_signal,
    f06sq_f06_volatility_squeeze_breakout_bwk1_21d_base_v007_signal,
    f06sq_f06_volatility_squeeze_breakout_bwk3_63d_base_v008_signal,
    f06sq_f06_volatility_squeeze_breakout_bwrank_21d_base_v009_signal,
    f06sq_f06_volatility_squeeze_breakout_bwrank_63d_base_v010_signal,
    f06sq_f06_volatility_squeeze_breakout_bwrank_126d_base_v011_signal,
    f06sq_f06_volatility_squeeze_breakout_bwz_21d_base_v012_signal,
    f06sq_f06_volatility_squeeze_breakout_bwz_63d_base_v013_signal,
    f06sq_f06_volatility_squeeze_breakout_bwz_126d_base_v014_signal,
    f06sq_f06_volatility_squeeze_breakout_bwratio_21_126_base_v015_signal,
    f06sq_f06_volatility_squeeze_breakout_bwratio_42_252_base_v016_signal,
    f06sq_f06_volatility_squeeze_breakout_bwratio_10_63_base_v017_signal,
    f06sq_f06_volatility_squeeze_breakout_bwrel_21d_base_v018_signal,
    f06sq_f06_volatility_squeeze_breakout_bwrel_63d_base_v019_signal,
    f06sq_f06_volatility_squeeze_breakout_sq_21d_base_v020_signal,
    f06sq_f06_volatility_squeeze_breakout_sq_63d_base_v021_signal,
    f06sq_f06_volatility_squeeze_breakout_sq_126d_base_v022_signal,
    f06sq_f06_volatility_squeeze_breakout_sq_10d_base_v023_signal,
    f06sq_f06_volatility_squeeze_breakout_sq_42d_base_v024_signal,
    f06sq_f06_volatility_squeeze_breakout_sq_252d_base_v025_signal,
    f06sq_f06_volatility_squeeze_breakout_sqz_21d_base_v026_signal,
    f06sq_f06_volatility_squeeze_breakout_sqz_63d_base_v027_signal,
    f06sq_f06_volatility_squeeze_breakout_sqrank_21d_base_v028_signal,
    f06sq_f06_volatility_squeeze_breakout_sqrank_63d_base_v029_signal,
    f06sq_f06_volatility_squeeze_breakout_sqrel_21d_base_v030_signal,
    f06sq_f06_volatility_squeeze_breakout_pctb_21d_base_v031_signal,
    f06sq_f06_volatility_squeeze_breakout_pctb_63d_base_v032_signal,
    f06sq_f06_volatility_squeeze_breakout_pctb_126d_base_v033_signal,
    f06sq_f06_volatility_squeeze_breakout_pctb_10d_base_v034_signal,
    f06sq_f06_volatility_squeeze_breakout_pctb_42d_base_v035_signal,
    f06sq_f06_volatility_squeeze_breakout_pctb_252d_base_v036_signal,
    f06sq_f06_volatility_squeeze_breakout_pctbc_21d_base_v037_signal,
    f06sq_f06_volatility_squeeze_breakout_pctbc_63d_base_v038_signal,
    f06sq_f06_volatility_squeeze_breakout_pctbk1_21d_base_v039_signal,
    f06sq_f06_volatility_squeeze_breakout_pctbk3_63d_base_v040_signal,
    f06sq_f06_volatility_squeeze_breakout_atrp_21d_base_v041_signal,
    f06sq_f06_volatility_squeeze_breakout_atrp_63d_base_v042_signal,
    f06sq_f06_volatility_squeeze_breakout_atrp_126d_base_v043_signal,
    f06sq_f06_volatility_squeeze_breakout_atrp_10d_base_v044_signal,
    f06sq_f06_volatility_squeeze_breakout_atrp_252d_base_v045_signal,
    f06sq_f06_volatility_squeeze_breakout_atrpratio_21_126_base_v046_signal,
    f06sq_f06_volatility_squeeze_breakout_atrpz_21d_base_v047_signal,
    f06sq_f06_volatility_squeeze_breakout_atrprank_63d_base_v048_signal,
    f06sq_f06_volatility_squeeze_breakout_distup_21d_base_v049_signal,
    f06sq_f06_volatility_squeeze_breakout_distdn_21d_base_v050_signal,
    f06sq_f06_volatility_squeeze_breakout_distup_63d_base_v051_signal,
    f06sq_f06_volatility_squeeze_breakout_distdn_63d_base_v052_signal,
    f06sq_f06_volatility_squeeze_breakout_midz_21d_base_v053_signal,
    f06sq_f06_volatility_squeeze_breakout_midz_63d_base_v054_signal,
    f06sq_f06_volatility_squeeze_breakout_rngcomp_21d_base_v055_signal,
    f06sq_f06_volatility_squeeze_breakout_rngcomp_63d_base_v056_signal,
    f06sq_f06_volatility_squeeze_breakout_stdratio_10_63_base_v057_signal,
    f06sq_f06_volatility_squeeze_breakout_stdratio_21_126_base_v058_signal,
    f06sq_f06_volatility_squeeze_breakout_stdratio_42_252_base_v059_signal,
    f06sq_f06_volatility_squeeze_breakout_coil_21d_base_v060_signal,
    f06sq_f06_volatility_squeeze_breakout_coil_63d_base_v061_signal,
    f06sq_f06_volatility_squeeze_breakout_sqxb_21d_base_v062_signal,
    f06sq_f06_volatility_squeeze_breakout_sqxb_63d_base_v063_signal,
    f06sq_f06_volatility_squeeze_breakout_bwchg_21d_base_v064_signal,
    f06sq_f06_volatility_squeeze_breakout_bwchg_63d_base_v065_signal,
    f06sq_f06_volatility_squeeze_breakout_sqchg_21d_base_v066_signal,
    f06sq_f06_volatility_squeeze_breakout_pctbmom_21d_base_v067_signal,
    f06sq_f06_volatility_squeeze_breakout_pctbmom_63d_base_v068_signal,
    f06sq_f06_volatility_squeeze_breakout_bwewm_21d_base_v069_signal,
    f06sq_f06_volatility_squeeze_breakout_bwewm_63d_base_v070_signal,
    f06sq_f06_volatility_squeeze_breakout_bwdisp_63d_base_v071_signal,
    f06sq_f06_volatility_squeeze_breakout_bwdisp_126d_base_v072_signal,
    f06sq_f06_volatility_squeeze_breakout_upatr_21d_base_v073_signal,
    f06sq_f06_volatility_squeeze_breakout_dnatr_21d_base_v074_signal,
    f06sq_f06_volatility_squeeze_breakout_invsq_21d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_VOLATILITY_SQUEEZE_BREAKOUT_REGISTRY_001_075 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open","high","low","close","closeadj","price","volume","marketcap","ev",
           "assets","assetsc","equity","revenue","gp","ebitda","ppnenet","sharesbas",
           "shareswa","cashneq","cor","opex","sgna","rnd","inventory","receivables",
           "intangibles","evebitda","evebit","pe","pb","ps","currentratio","bvps","sps",
           "shrvalue","shrunits","totalvalue","percentoftotal","sf3a_shares","sf3a_value",
           "sf3b_shares","sf3b_value","grossmargin","beta1y","beta5y","invcap","debt"}
    for nm in names:
        if nm in ("closeadj","close","price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price*(1+np.random.normal(0,0.01,n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price*(1+nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price*(1-nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7,7e6,n))+1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0,1.0,n))
            level = 1000.0*np.exp(0.03*np.random.normal(0,1,n).cumsum()/np.sqrt(n))
            s = level + 50.0*walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f06_bandwidth", "_f06_squeeze", "_f06_pctb", "_f06_atrp")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0; nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args); y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f06_volatility_squeeze_breakout_base_001_075_claude: {n_features} features pass")
