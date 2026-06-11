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


# ============ FEATURES 076-150 ============

# 84d Bollinger bandwidth
def f06sq_f06_volatility_squeeze_breakout_bw_84d_base_v076_signal(closeadj):
    result = _f06_bandwidth(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d Bollinger bandwidth
def f06sq_f06_volatility_squeeze_breakout_bw_189d_base_v077_signal(closeadj):
    result = _f06_bandwidth(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d Bollinger bandwidth (very short coil)
def f06sq_f06_volatility_squeeze_breakout_bw_5d_base_v078_signal(closeadj):
    result = _f06_bandwidth(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d Bollinger bandwidth
def f06sq_f06_volatility_squeeze_breakout_bw_504d_base_v079_signal(closeadj):
    result = _f06_bandwidth(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d Bollinger bandwidth
def f06sq_f06_volatility_squeeze_breakout_bw_315d_base_v080_signal(closeadj):
    result = _f06_bandwidth(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d bandwidth k=2.5
def f06sq_f06_volatility_squeeze_breakout_bwk25_21d_base_v081_signal(closeadj):
    result = _f06_bandwidth(closeadj, 21, 2.5)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d bandwidth k=1.5
def f06sq_f06_volatility_squeeze_breakout_bwk15_126d_base_v082_signal(closeadj):
    result = _f06_bandwidth(closeadj, 126, 1.5)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d bandwidth percentile rank over 252d
def f06sq_f06_volatility_squeeze_breakout_bwrank_42d_base_v083_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 42)
    result = bw.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d bandwidth percentile rank over 504d
def f06sq_f06_volatility_squeeze_breakout_bwrank_252d_base_v084_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 252)
    result = bw.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d bandwidth z-score over 252d
def f06sq_f06_volatility_squeeze_breakout_bwz_42d_base_v085_signal(closeadj):
    result = _z(_f06_bandwidth(closeadj, 42), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d bandwidth z-score over 504d
def f06sq_f06_volatility_squeeze_breakout_bwz_84d_base_v086_signal(closeadj):
    result = _z(_f06_bandwidth(closeadj, 84), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth ratio 21d over 252d
def f06sq_f06_volatility_squeeze_breakout_bwratio_21_252_base_v087_signal(closeadj):
    result = _safe_div(_f06_bandwidth(closeadj, 21), _f06_bandwidth(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth ratio 63d over 252d
def f06sq_f06_volatility_squeeze_breakout_bwratio_63_252_base_v088_signal(closeadj):
    result = _safe_div(_f06_bandwidth(closeadj, 63), _f06_bandwidth(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d bandwidth relative to its own 252d mean
def f06sq_f06_volatility_squeeze_breakout_bwrel_126d_base_v089_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 126)
    result = _safe_div(bw, _mean(bw, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 84d squeeze ratio
def f06sq_f06_volatility_squeeze_breakout_sq_84d_base_v090_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d squeeze ratio
def f06sq_f06_volatility_squeeze_breakout_sq_189d_base_v091_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d squeeze ratio
def f06sq_f06_volatility_squeeze_breakout_sq_5d_base_v092_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d squeeze z-score over 504d
def f06sq_f06_volatility_squeeze_breakout_sqz_126d_base_v093_signal(high, low, closeadj):
    result = _z(_f06_squeeze(high, low, closeadj, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d squeeze z-score over 252d
def f06sq_f06_volatility_squeeze_breakout_sqz_42d_base_v094_signal(high, low, closeadj):
    result = _z(_f06_squeeze(high, low, closeadj, 42), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d squeeze percentile rank over 504d
def f06sq_f06_volatility_squeeze_breakout_sqrank_126d_base_v095_signal(high, low, closeadj):
    sq = _f06_squeeze(high, low, closeadj, 126)
    result = sq.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d squeeze percentile rank over 252d
def f06sq_f06_volatility_squeeze_breakout_sqrank_42d_base_v096_signal(high, low, closeadj):
    sq = _f06_squeeze(high, low, closeadj, 42)
    result = sq.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d squeeze relative to its 126d mean
def f06sq_f06_volatility_squeeze_breakout_sqrel_63d_base_v097_signal(high, low, closeadj):
    sq = _f06_squeeze(high, low, closeadj, 63)
    result = _safe_div(sq, _mean(sq, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze ratio short/long 21d over 126d
def f06sq_f06_volatility_squeeze_breakout_sqratio_21_126_base_v098_signal(high, low, closeadj):
    result = _safe_div(_f06_squeeze(high, low, closeadj, 21), _f06_squeeze(high, low, closeadj, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 84d %B
def f06sq_f06_volatility_squeeze_breakout_pctb_84d_base_v099_signal(closeadj):
    result = _f06_pctb(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d %B
def f06sq_f06_volatility_squeeze_breakout_pctb_189d_base_v100_signal(closeadj):
    result = _f06_pctb(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d %B
def f06sq_f06_volatility_squeeze_breakout_pctb_5d_base_v101_signal(closeadj):
    result = _f06_pctb(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d %B smoothed (21d mean)
def f06sq_f06_volatility_squeeze_breakout_pctbsm_21d_base_v102_signal(closeadj):
    result = _mean(_f06_pctb(closeadj, 21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d %B smoothed (21d mean)
def f06sq_f06_volatility_squeeze_breakout_pctbsm_63d_base_v103_signal(closeadj):
    result = _mean(_f06_pctb(closeadj, 63), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d %B z-score over 252d
def f06sq_f06_volatility_squeeze_breakout_pctbz_21d_base_v104_signal(closeadj):
    result = _z(_f06_pctb(closeadj, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d %B z-score over 252d
def f06sq_f06_volatility_squeeze_breakout_pctbz_63d_base_v105_signal(closeadj):
    result = _z(_f06_pctb(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d %B dispersion 63d (band-walk variability)
def f06sq_f06_volatility_squeeze_breakout_pctbdisp_63d_base_v106_signal(closeadj):
    result = _std(_f06_pctb(closeadj, 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d ATR/price compression
def f06sq_f06_volatility_squeeze_breakout_atrp_84d_base_v107_signal(high, low, closeadj):
    result = _f06_atrp(high, low, closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d ATR/price compression
def f06sq_f06_volatility_squeeze_breakout_atrp_189d_base_v108_signal(high, low, closeadj):
    result = _f06_atrp(high, low, closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d ATR/price compression
def f06sq_f06_volatility_squeeze_breakout_atrp_42d_base_v109_signal(high, low, closeadj):
    result = _f06_atrp(high, low, closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price ratio 10d over 63d
def f06sq_f06_volatility_squeeze_breakout_atrpratio_10_63_base_v110_signal(high, low, closeadj):
    result = _safe_div(_f06_atrp(high, low, closeadj, 10), _f06_atrp(high, low, closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price ratio 42d over 252d
def f06sq_f06_volatility_squeeze_breakout_atrpratio_42_252_base_v111_signal(high, low, closeadj):
    result = _safe_div(_f06_atrp(high, low, closeadj, 42), _f06_atrp(high, low, closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price z-score over 252d (63d)
def f06sq_f06_volatility_squeeze_breakout_atrpz_63d_base_v112_signal(high, low, closeadj):
    result = _z(_f06_atrp(high, low, closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price percentile rank over 252d (21d)
def f06sq_f06_volatility_squeeze_breakout_atrprank_21d_base_v113_signal(high, low, closeadj):
    a = _f06_atrp(high, low, closeadj, 21)
    result = a.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price relative to its 63d mean (21d)
def f06sq_f06_volatility_squeeze_breakout_atrprel_21d_base_v114_signal(high, low, closeadj):
    a = _f06_atrp(high, low, closeadj, 21)
    result = _safe_div(a, _mean(a, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# distance to upper band normalized (126d)
def f06sq_f06_volatility_squeeze_breakout_distup_126d_base_v115_signal(closeadj):
    m = _mean(closeadj, 126)
    sd = _std(closeadj, 126)
    upper = m + 2.0 * sd
    result = _safe_div(upper - closeadj, 2.0 * 2.0 * sd) + _f06_bandwidth(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance to lower band normalized (126d)
def f06sq_f06_volatility_squeeze_breakout_distdn_126d_base_v116_signal(closeadj):
    m = _mean(closeadj, 126)
    sd = _std(closeadj, 126)
    lower = m - 2.0 * sd
    result = _safe_div(closeadj - lower, 2.0 * 2.0 * sd) + _f06_bandwidth(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# close distance from band mid normalized by std (126d)
def f06sq_f06_volatility_squeeze_breakout_midz_126d_base_v117_signal(closeadj):
    result = _z(closeadj, 126) + _f06_bandwidth(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# range / average-range compression 42d vs 126d
def f06sq_f06_volatility_squeeze_breakout_rngcomp_42d_base_v118_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    result = _safe_div(_mean(rng, 42), _mean(rng, 126)) + _f06_atrp(high, low, closeadj, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# range / average-range compression 10d vs 42d
def f06sq_f06_volatility_squeeze_breakout_rngcomp_10d_base_v119_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    result = _safe_div(_mean(rng, 10), _mean(rng, 42)) + _f06_atrp(high, low, closeadj, 10) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# std ratio 5d over 42d (very-short compression)
def f06sq_f06_volatility_squeeze_breakout_stdratio_5_42_base_v120_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(_std(lr, 5), _std(lr, 42)) + _f06_bandwidth(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# std ratio 63d over 252d
def f06sq_f06_volatility_squeeze_breakout_stdratio_63_252_base_v121_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(_std(lr, 63), _std(lr, 252)) + _f06_bandwidth(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# coil tightness 126d (inverse bandwidth z)
def f06sq_f06_volatility_squeeze_breakout_coil_126d_base_v122_signal(closeadj):
    result = -_z(_f06_bandwidth(closeadj, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# coil tightness via rank (1 - bandwidth rank) 42d
def f06sq_f06_volatility_squeeze_breakout_coilrank_42d_base_v123_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 42)
    result = 1.0 - bw.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze * %B interaction 126d
def f06sq_f06_volatility_squeeze_breakout_sqxb_126d_base_v124_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 126) * (_f06_pctb(closeadj, 126) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth * %B interaction 21d (expansion with breakout direction)
def f06sq_f06_volatility_squeeze_breakout_bwxb_21d_base_v125_signal(closeadj):
    result = _f06_bandwidth(closeadj, 21) * (_f06_pctb(closeadj, 21) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth * %B interaction 63d
def f06sq_f06_volatility_squeeze_breakout_bwxb_63d_base_v126_signal(closeadj):
    result = _f06_bandwidth(closeadj, 63) * (_f06_pctb(closeadj, 63) - 0.5)
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth change rate 126d
def f06sq_f06_volatility_squeeze_breakout_bwchg_126d_base_v127_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 126)
    result = _safe_div(bw - bw.shift(21), _mean(bw, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth expansion (current vs rolling min over 126d) - release magnitude
def f06sq_f06_volatility_squeeze_breakout_bwexp_126d_base_v128_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 21)
    floor = bw.rolling(126, min_periods=42).min().replace(0, np.nan)
    result = _safe_div(bw, floor)
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth expansion vs rolling min over 252d (63d bandwidth)
def f06sq_f06_volatility_squeeze_breakout_bwexp_252d_base_v129_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 63)
    floor = bw.rolling(252, min_periods=84).min().replace(0, np.nan)
    result = _safe_div(bw, floor)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR compression vs rolling min over 126d (release proxy)
def f06sq_f06_volatility_squeeze_breakout_atrexp_126d_base_v130_signal(high, low, closeadj):
    a = _f06_atrp(high, low, closeadj, 21)
    floor = a.rolling(126, min_periods=42).min().replace(0, np.nan)
    result = _safe_div(a, floor)
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze change rate 63d
def f06sq_f06_volatility_squeeze_breakout_sqchg_63d_base_v131_signal(high, low, closeadj):
    sq = _f06_squeeze(high, low, closeadj, 63)
    result = _safe_div(sq - sq.shift(21), _mean(sq, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# %B momentum 126d
def f06sq_f06_volatility_squeeze_breakout_pctbmom_126d_base_v132_signal(closeadj):
    b = _f06_pctb(closeadj, 126)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth EWMA span 126 (smoothed compression)
def f06sq_f06_volatility_squeeze_breakout_bwewm_126d_base_v133_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 126)
    result = bw.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze EWMA span 63 (smoothed squeeze)
def f06sq_f06_volatility_squeeze_breakout_sqewm_63d_base_v134_signal(high, low, closeadj):
    sq = _f06_squeeze(high, low, closeadj, 63)
    result = sq.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth dispersion 252d
def f06sq_f06_volatility_squeeze_breakout_bwdisp_252d_base_v135_signal(closeadj):
    result = _std(_f06_bandwidth(closeadj, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze dispersion 126d (variability of squeeze regime)
def f06sq_f06_volatility_squeeze_breakout_sqdisp_126d_base_v136_signal(high, low, closeadj):
    result = _std(_f06_squeeze(high, low, closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# normalized close-to-upper over ATR (63d breakout proximity)
def f06sq_f06_volatility_squeeze_breakout_upatr_63d_base_v137_signal(high, low, closeadj):
    m = _mean(closeadj, 63)
    sd = _std(closeadj, 63)
    upper = m + 2.0 * sd
    atrp = _f06_atrp(high, low, closeadj, 63)
    result = _safe_div(upper - closeadj, atrp * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# normalized close-to-lower over ATR (63d)
def f06sq_f06_volatility_squeeze_breakout_dnatr_63d_base_v138_signal(high, low, closeadj):
    m = _mean(closeadj, 63)
    sd = _std(closeadj, 63)
    lower = m - 2.0 * sd
    atrp = _f06_atrp(high, low, closeadj, 63)
    result = _safe_div(closeadj - lower, atrp * closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# inverse squeeze 63d (Keltner/Bollinger)
def f06sq_f06_volatility_squeeze_breakout_invsq_63d_base_v139_signal(high, low, closeadj):
    result = _safe_div(pd.Series(1.0, index=closeadj.index), _f06_squeeze(high, low, closeadj, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth times %B momentum (compression-armed breakout) 21d
def f06sq_f06_volatility_squeeze_breakout_armed_21d_base_v140_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 21)
    b = _f06_pctb(closeadj, 21)
    result = _safe_div(b - b.shift(21), bw)
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth-armed breakout 63d
def f06sq_f06_volatility_squeeze_breakout_armed_63d_base_v141_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 63)
    b = _f06_pctb(closeadj, 63)
    result = _safe_div(b - b.shift(21), bw)
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth normalized by 252d realized vol (vol-of-band) 21d
def f06sq_f06_volatility_squeeze_breakout_bwvoln_21d_base_v142_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 252)
    result = _safe_div(_f06_bandwidth(closeadj, 21), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# bandwidth normalized by 252d realized vol 63d
def f06sq_f06_volatility_squeeze_breakout_bwvoln_63d_base_v143_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 252)
    result = _safe_div(_f06_bandwidth(closeadj, 63), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze deviation from 1.0 (BB vs KC parity, signed compression) 21d
def f06sq_f06_volatility_squeeze_breakout_sqdev_21d_base_v144_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 21) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# squeeze deviation from 1.0 63d
def f06sq_f06_volatility_squeeze_breakout_sqdev_63d_base_v145_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 63) - 1.0
    return result.replace([np.inf, -np.inf], np.nan)


# log bandwidth (compression on log scale) 21d
def f06sq_f06_volatility_squeeze_breakout_logbw_21d_base_v146_signal(closeadj):
    result = np.log(_f06_bandwidth(closeadj, 21).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# log bandwidth 63d
def f06sq_f06_volatility_squeeze_breakout_logbw_63d_base_v147_signal(closeadj):
    result = np.log(_f06_bandwidth(closeadj, 63).replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


# %B distance from extremes (min of upper/lower proximity) 21d - coil edge tension
def f06sq_f06_volatility_squeeze_breakout_edge_21d_base_v148_signal(closeadj):
    b = _f06_pctb(closeadj, 21)
    result = (b - 0.5).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# %B distance from extremes 63d
def f06sq_f06_volatility_squeeze_breakout_edge_63d_base_v149_signal(closeadj):
    b = _f06_pctb(closeadj, 63)
    result = (b - 0.5).abs()
    return result.replace([np.inf, -np.inf], np.nan)


# blended squeeze composite: bandwidth-rank + atr-rank + squeeze level (multi-horizon coil)
def f06sq_f06_volatility_squeeze_breakout_blend_multi_base_v150_signal(high, low, closeadj):
    bwr = _f06_bandwidth(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    atr = _f06_atrp(high, low, closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    sq = _f06_squeeze(high, low, closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    result = (bwr + atr + sq) / 3.0 + _f06_pctb(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f06sq_f06_volatility_squeeze_breakout_bw_84d_base_v076_signal,
    f06sq_f06_volatility_squeeze_breakout_bw_189d_base_v077_signal,
    f06sq_f06_volatility_squeeze_breakout_bw_5d_base_v078_signal,
    f06sq_f06_volatility_squeeze_breakout_bw_504d_base_v079_signal,
    f06sq_f06_volatility_squeeze_breakout_bw_315d_base_v080_signal,
    f06sq_f06_volatility_squeeze_breakout_bwk25_21d_base_v081_signal,
    f06sq_f06_volatility_squeeze_breakout_bwk15_126d_base_v082_signal,
    f06sq_f06_volatility_squeeze_breakout_bwrank_42d_base_v083_signal,
    f06sq_f06_volatility_squeeze_breakout_bwrank_252d_base_v084_signal,
    f06sq_f06_volatility_squeeze_breakout_bwz_42d_base_v085_signal,
    f06sq_f06_volatility_squeeze_breakout_bwz_84d_base_v086_signal,
    f06sq_f06_volatility_squeeze_breakout_bwratio_21_252_base_v087_signal,
    f06sq_f06_volatility_squeeze_breakout_bwratio_63_252_base_v088_signal,
    f06sq_f06_volatility_squeeze_breakout_bwrel_126d_base_v089_signal,
    f06sq_f06_volatility_squeeze_breakout_sq_84d_base_v090_signal,
    f06sq_f06_volatility_squeeze_breakout_sq_189d_base_v091_signal,
    f06sq_f06_volatility_squeeze_breakout_sq_5d_base_v092_signal,
    f06sq_f06_volatility_squeeze_breakout_sqz_126d_base_v093_signal,
    f06sq_f06_volatility_squeeze_breakout_sqz_42d_base_v094_signal,
    f06sq_f06_volatility_squeeze_breakout_sqrank_126d_base_v095_signal,
    f06sq_f06_volatility_squeeze_breakout_sqrank_42d_base_v096_signal,
    f06sq_f06_volatility_squeeze_breakout_sqrel_63d_base_v097_signal,
    f06sq_f06_volatility_squeeze_breakout_sqratio_21_126_base_v098_signal,
    f06sq_f06_volatility_squeeze_breakout_pctb_84d_base_v099_signal,
    f06sq_f06_volatility_squeeze_breakout_pctb_189d_base_v100_signal,
    f06sq_f06_volatility_squeeze_breakout_pctb_5d_base_v101_signal,
    f06sq_f06_volatility_squeeze_breakout_pctbsm_21d_base_v102_signal,
    f06sq_f06_volatility_squeeze_breakout_pctbsm_63d_base_v103_signal,
    f06sq_f06_volatility_squeeze_breakout_pctbz_21d_base_v104_signal,
    f06sq_f06_volatility_squeeze_breakout_pctbz_63d_base_v105_signal,
    f06sq_f06_volatility_squeeze_breakout_pctbdisp_63d_base_v106_signal,
    f06sq_f06_volatility_squeeze_breakout_atrp_84d_base_v107_signal,
    f06sq_f06_volatility_squeeze_breakout_atrp_189d_base_v108_signal,
    f06sq_f06_volatility_squeeze_breakout_atrp_42d_base_v109_signal,
    f06sq_f06_volatility_squeeze_breakout_atrpratio_10_63_base_v110_signal,
    f06sq_f06_volatility_squeeze_breakout_atrpratio_42_252_base_v111_signal,
    f06sq_f06_volatility_squeeze_breakout_atrpz_63d_base_v112_signal,
    f06sq_f06_volatility_squeeze_breakout_atrprank_21d_base_v113_signal,
    f06sq_f06_volatility_squeeze_breakout_atrprel_21d_base_v114_signal,
    f06sq_f06_volatility_squeeze_breakout_distup_126d_base_v115_signal,
    f06sq_f06_volatility_squeeze_breakout_distdn_126d_base_v116_signal,
    f06sq_f06_volatility_squeeze_breakout_midz_126d_base_v117_signal,
    f06sq_f06_volatility_squeeze_breakout_rngcomp_42d_base_v118_signal,
    f06sq_f06_volatility_squeeze_breakout_rngcomp_10d_base_v119_signal,
    f06sq_f06_volatility_squeeze_breakout_stdratio_5_42_base_v120_signal,
    f06sq_f06_volatility_squeeze_breakout_stdratio_63_252_base_v121_signal,
    f06sq_f06_volatility_squeeze_breakout_coil_126d_base_v122_signal,
    f06sq_f06_volatility_squeeze_breakout_coilrank_42d_base_v123_signal,
    f06sq_f06_volatility_squeeze_breakout_sqxb_126d_base_v124_signal,
    f06sq_f06_volatility_squeeze_breakout_bwxb_21d_base_v125_signal,
    f06sq_f06_volatility_squeeze_breakout_bwxb_63d_base_v126_signal,
    f06sq_f06_volatility_squeeze_breakout_bwchg_126d_base_v127_signal,
    f06sq_f06_volatility_squeeze_breakout_bwexp_126d_base_v128_signal,
    f06sq_f06_volatility_squeeze_breakout_bwexp_252d_base_v129_signal,
    f06sq_f06_volatility_squeeze_breakout_atrexp_126d_base_v130_signal,
    f06sq_f06_volatility_squeeze_breakout_sqchg_63d_base_v131_signal,
    f06sq_f06_volatility_squeeze_breakout_pctbmom_126d_base_v132_signal,
    f06sq_f06_volatility_squeeze_breakout_bwewm_126d_base_v133_signal,
    f06sq_f06_volatility_squeeze_breakout_sqewm_63d_base_v134_signal,
    f06sq_f06_volatility_squeeze_breakout_bwdisp_252d_base_v135_signal,
    f06sq_f06_volatility_squeeze_breakout_sqdisp_126d_base_v136_signal,
    f06sq_f06_volatility_squeeze_breakout_upatr_63d_base_v137_signal,
    f06sq_f06_volatility_squeeze_breakout_dnatr_63d_base_v138_signal,
    f06sq_f06_volatility_squeeze_breakout_invsq_63d_base_v139_signal,
    f06sq_f06_volatility_squeeze_breakout_armed_21d_base_v140_signal,
    f06sq_f06_volatility_squeeze_breakout_armed_63d_base_v141_signal,
    f06sq_f06_volatility_squeeze_breakout_bwvoln_21d_base_v142_signal,
    f06sq_f06_volatility_squeeze_breakout_bwvoln_63d_base_v143_signal,
    f06sq_f06_volatility_squeeze_breakout_sqdev_21d_base_v144_signal,
    f06sq_f06_volatility_squeeze_breakout_sqdev_63d_base_v145_signal,
    f06sq_f06_volatility_squeeze_breakout_logbw_21d_base_v146_signal,
    f06sq_f06_volatility_squeeze_breakout_logbw_63d_base_v147_signal,
    f06sq_f06_volatility_squeeze_breakout_edge_21d_base_v148_signal,
    f06sq_f06_volatility_squeeze_breakout_edge_63d_base_v149_signal,
    f06sq_f06_volatility_squeeze_breakout_blend_multi_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_VOLATILITY_SQUEEZE_BREAKOUT_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f06_volatility_squeeze_breakout_base_076_150_claude: {n_features} features pass")
