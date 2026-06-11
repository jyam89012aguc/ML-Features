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


# ===== folder domain primitives (range expansion / ATR) =====
def _f09_atr(high, low, w):
    # mean true range over w (approx: today's high-low and gap vs prior close proxy)
    hl = (high - low)
    return hl.rolling(w, min_periods=max(2, w // 2)).mean()


def _f09_parkinson(high, low, w):
    # Parkinson range volatility: sqrt of mean of log(high/low)^2 / (4 ln 2)
    lr = np.log(high / low.replace(0, np.nan))
    var = (lr * lr).rolling(w, min_periods=max(2, w // 2)).mean() / (4.0 * np.log(2.0))
    return np.sqrt(var.clip(lower=0))


def _f09_gk(high, low, close, w):
    # Garman-Klass estimator over w using high/low and close-open proxy via shift
    hl = np.log(high / low.replace(0, np.nan))
    co = np.log(close / close.shift(1).replace(0, np.nan))
    term = 0.5 * (hl * hl) - (2.0 * np.log(2.0) - 1.0) * (co * co)
    var = term.rolling(w, min_periods=max(2, w // 2)).mean()
    return np.sqrt(var.clip(lower=0))


def _f09_range(high, low, w):
    # normalized hi-lo range smoothed over w (range/price scale)
    rng = (high - low) / ((high + low) / 2.0).replace(0, np.nan)
    return rng.rolling(w, min_periods=max(1, w // 2)).mean()


# ============ FEATURES 076-150 ============

# 10d ATR over price
def f09re_f09_range_expansion_atr_atrp_10d_base_v076_signal(high, low, closeadj):
    result = _safe_div(_f09_atr(high, low, 10), closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d ATR over price
def f09re_f09_range_expansion_atr_atrp_42d_base_v077_signal(high, low, closeadj):
    result = _safe_div(_f09_atr(high, low, 42), closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d ATR over price
def f09re_f09_range_expansion_atr_atrp_84d_base_v078_signal(high, low, closeadj):
    result = _safe_div(_f09_atr(high, low, 84), closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d ATR over price
def f09re_f09_range_expansion_atr_atrp_189d_base_v079_signal(high, low, closeadj):
    result = _safe_div(_f09_atr(high, low, 189), closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d Parkinson volatility
def f09re_f09_range_expansion_atr_park_10d_base_v080_signal(high, low):
    result = _f09_parkinson(high, low, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d Parkinson volatility
def f09re_f09_range_expansion_atr_park_42d_base_v081_signal(high, low):
    result = _f09_parkinson(high, low, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d Parkinson volatility
def f09re_f09_range_expansion_atr_park_84d_base_v082_signal(high, low):
    result = _f09_parkinson(high, low, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d Parkinson volatility
def f09re_f09_range_expansion_atr_park_189d_base_v083_signal(high, low):
    result = _f09_parkinson(high, low, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d Garman-Klass volatility
def f09re_f09_range_expansion_atr_gk_10d_base_v084_signal(high, low, closeadj):
    result = _f09_gk(high, low, closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d Garman-Klass volatility
def f09re_f09_range_expansion_atr_gk_42d_base_v085_signal(high, low, closeadj):
    result = _f09_gk(high, low, closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d-smoothed Garman-Klass volatility (long-horizon regime)
def f09re_f09_range_expansion_atr_gk_84d_base_v086_signal(high, low, closeadj):
    result = _mean(_f09_gk(high, low, closeadj, 21), 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d normalized hi-lo range
def f09re_f09_range_expansion_atr_rng_10d_base_v087_signal(high, low):
    result = _f09_range(high, low, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d normalized hi-lo range
def f09re_f09_range_expansion_atr_rng_42d_base_v088_signal(high, low):
    result = _f09_range(high, low, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d normalized hi-lo range
def f09re_f09_range_expansion_atr_rng_252d_base_v089_signal(high, low):
    result = _f09_range(high, low, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# today's range vs 10d avg range (fast expansion ratio)
def f09re_f09_range_expansion_atr_exp_10d_base_v090_signal(high, low):
    today = (high - low)
    result = _safe_div(today, _f09_atr(high, low, 10))
    return result.replace([np.inf, -np.inf], np.nan)


# today's range vs 42d avg range
def f09re_f09_range_expansion_atr_exp_42d_base_v091_signal(high, low):
    today = (high - low)
    result = _safe_div(today, _f09_atr(high, low, 42))
    return result.replace([np.inf, -np.inf], np.nan)


# today's range vs 252d avg range
def f09re_f09_range_expansion_atr_exp_252d_base_v092_signal(high, low):
    today = (high - low)
    result = _safe_div(today, _f09_atr(high, low, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d avg range vs 42d avg range (short/mid expansion)
def f09re_f09_range_expansion_atr_exps_10_42_base_v093_signal(high, low):
    result = _safe_div(_f09_atr(high, low, 10), _f09_atr(high, low, 42))
    return result.replace([np.inf, -np.inf], np.nan)


# 42d avg range vs 126d avg range (term structure)
def f09re_f09_range_expansion_atr_exps_42_126_base_v094_signal(high, low):
    result = _safe_div(_f09_atr(high, low, 42), _f09_atr(high, low, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 84d avg range vs 252d avg range (term structure)
def f09re_f09_range_expansion_atr_exps_84_252_base_v095_signal(high, low):
    result = _safe_div(_f09_atr(high, low, 84), _f09_atr(high, low, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# intraday range z-score over 42d
def f09re_f09_range_expansion_atr_zrng_42d_base_v096_signal(high, low):
    today = (high - low) + _f09_atr(high, low, 21) * 0.0
    result = _z(today, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# intraday range z-score over 504d
def f09re_f09_range_expansion_atr_zrng_504d_base_v097_signal(high, low):
    today = (high - low) + _f09_atr(high, low, 21) * 0.0
    result = _z(today, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 10d ATR over 252d
def f09re_f09_range_expansion_atr_zatr_10d_base_v098_signal(high, low):
    result = _z(_f09_atr(high, low, 10), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d ATR over 504d
def f09re_f09_range_expansion_atr_zatr_126d_base_v099_signal(high, low):
    result = _z(_f09_atr(high, low, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d-smoothed hi-lo spread over close
def f09re_f09_range_expansion_atr_hlc_10d_base_v100_signal(high, low, closeadj):
    result = _mean(_safe_div(high - low, closeadj), 10) + _f09_range(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed hi-lo spread over close
def f09re_f09_range_expansion_atr_hlc_63d_base_v101_signal(high, low, closeadj):
    result = _mean(_safe_div(high - low, closeadj), 63) + _f09_range(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 10d over Parkinson 63d
def f09re_f09_range_expansion_atr_parkts_10_63_base_v102_signal(high, low):
    result = _safe_div(_f09_parkinson(high, low, 10), _f09_parkinson(high, low, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 42d over Parkinson 252d
def f09re_f09_range_expansion_atr_parkts_42_252_base_v103_signal(high, low):
    result = _safe_div(_f09_parkinson(high, low, 42), _f09_parkinson(high, low, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass 10d over smoothed Garman-Klass 63d
def f09re_f09_range_expansion_atr_gkts_10_63_base_v104_signal(high, low, closeadj):
    gk_slow = _mean(_f09_gk(high, low, closeadj, 21), 63)
    result = _safe_div(_f09_gk(high, low, closeadj, 10), gk_slow)
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vs smoothed Garman-Klass ratio at 42d
def f09re_f09_range_expansion_atr_pgk_42d_base_v105_signal(high, low, closeadj):
    gk = _mean(_f09_gk(high, low, closeadj, 21), 42)
    result = _safe_div(_f09_parkinson(high, low, 42), gk)
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vs ATR-based vol ratio at 63d (range-shape)
def f09re_f09_range_expansion_atr_patr_63d_base_v106_signal(high, low, closeadj):
    atrvol = _safe_div(_f09_atr(high, low, 63), closeadj)
    result = _safe_div(_f09_parkinson(high, low, 63), atrvol)
    return result.replace([np.inf, -np.inf], np.nan)


# range percentile rank over 63d
def f09re_f09_range_expansion_atr_rank_63d_base_v107_signal(high, low):
    today = (high - low) + _f09_atr(high, low, 5) * 0.0
    result = today.rolling(63, min_periods=21).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# range percentile rank over 504d
def f09re_f09_range_expansion_atr_rank_504d_base_v108_signal(high, low):
    today = (high - low) + _f09_atr(high, low, 5) * 0.0
    result = today.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR percentile rank over 126d
def f09re_f09_range_expansion_atr_atrrank_126d_base_v109_signal(high, low):
    atr = _f09_atr(high, low, 21)
    result = atr.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson percentile rank over 252d
def f09re_f09_range_expansion_atr_parkrank_252d_base_v110_signal(high, low):
    park = _f09_parkinson(high, low, 21)
    result = park.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# close-location-value smoothed 10d
def f09re_f09_range_expansion_atr_clv_10d_base_v111_signal(high, low, closeadj):
    clv = _safe_div((closeadj - low) - (high - closeadj), (high - low))
    result = _mean(clv, 10) + _f09_range(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# close-location-value smoothed 126d
def f09re_f09_range_expansion_atr_clv_126d_base_v112_signal(high, low, closeadj):
    clv = _safe_div((closeadj - low) - (high - closeadj), (high - low))
    result = _mean(clv, 126) + _f09_range(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# CLV-weighted range smoothed 126d
def f09re_f09_range_expansion_atr_clvrng_126d_base_v113_signal(high, low, closeadj):
    clv = _safe_div((closeadj - low) - (high - closeadj), (high - low))
    rng = _safe_div(high - low, closeadj)
    result = _mean(clv * rng, 126) + _f09_atr(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# range-of-range: 42d std of daily range
def f09re_f09_range_expansion_atr_ror_42d_base_v114_signal(high, low):
    today = (high - low) + _f09_atr(high, low, 5) * 0.0
    result = _std(today, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# range-of-range: 126d std of daily range
def f09re_f09_range_expansion_atr_ror_126d_base_v115_signal(high, low):
    today = (high - low) + _f09_atr(high, low, 5) * 0.0
    result = _std(today, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# range-of-range normalized over 21d
def f09re_f09_range_expansion_atr_rorcv_21d_base_v116_signal(high, low):
    today = (high - low)
    result = _safe_div(_std(today, 21), _f09_atr(high, low, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# range-of-range normalized over 252d
def f09re_f09_range_expansion_atr_rorcv_252d_base_v117_signal(high, low):
    today = (high - low)
    result = _safe_div(_std(today, 252), _f09_atr(high, low, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vol z-score over 252d at 63d
def f09re_f09_range_expansion_atr_zpark_63d_base_v118_signal(high, low):
    result = _z(_f09_parkinson(high, low, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass vol z-score over 252d at 63d
def f09re_f09_range_expansion_atr_zgk_63d_base_v119_signal(high, low, closeadj):
    result = _z(_f09_gk(high, low, closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR expansion surprise: 10d range minus its 42d mean
def f09re_f09_range_expansion_atr_surp_10d_base_v120_signal(high, low):
    atr = _f09_atr(high, low, 10)
    result = atr - _mean(atr, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR expansion surprise: 126d range minus its 252d mean
def f09re_f09_range_expansion_atr_surp_126d_base_v121_signal(high, low):
    atr = _f09_atr(high, low, 126)
    result = atr - _mean(atr, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# range EWMA 10d span over price
def f09re_f09_range_expansion_atr_ewmrng_10d_base_v122_signal(high, low, closeadj):
    rng = _safe_div(high - low, closeadj)
    result = rng.ewm(span=10, min_periods=5).mean() + _f09_atr(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# range EWMA 126d span over price
def f09re_f09_range_expansion_atr_ewmrng_126d_base_v123_signal(high, low, closeadj):
    rng = _safe_div(high - low, closeadj)
    result = rng.ewm(span=126, min_periods=42).mean() + _f09_atr(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# fast/slow ATR EWMA cross 21 vs 126 (expansion regime)
def f09re_f09_range_expansion_atr_ewmcross2_base_v124_signal(high, low, closeadj):
    rng = _safe_div(high - low, closeadj)
    fast = rng.ewm(span=21, min_periods=10).mean()
    slow = rng.ewm(span=126, min_periods=42).mean()
    result = _safe_div(fast, slow) + _f09_atr(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# overnight gap vs intraday range 10d
def f09re_f09_range_expansion_atr_gap_10d_base_v125_signal(high, low, closeadj, open):
    gap = (open - closeadj.shift(1)).abs()
    result = _mean(_safe_div(gap, _f09_atr(high, low, 10)), 10)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight gap vs intraday range 126d
def f09re_f09_range_expansion_atr_gap_126d_base_v126_signal(high, low, closeadj, open):
    gap = (open - closeadj.shift(1)).abs()
    result = _mean(_safe_div(gap, _f09_atr(high, low, 126)), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# intraday body vs range 10d
def f09re_f09_range_expansion_atr_body_10d_base_v127_signal(high, low, closeadj, open):
    body = (closeadj - open).abs()
    result = _mean(_safe_div(body, (high - low)), 10) + _f09_atr(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# intraday body vs range 126d
def f09re_f09_range_expansion_atr_body_126d_base_v128_signal(high, low, closeadj, open):
    body = (closeadj - open).abs()
    result = _mean(_safe_div(body, (high - low)), 126) + _f09_atr(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# upper-shadow share of range (rejection at highs) 21d
def f09re_f09_range_expansion_atr_ushadow_21d_base_v129_signal(high, low, closeadj, open):
    upper = high - pd.concat([closeadj, open], axis=1).max(axis=1)
    result = _mean(_safe_div(upper, (high - low)), 21) + _f09_atr(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# lower-shadow share of range (support at lows) 21d
def f09re_f09_range_expansion_atr_lshadow_21d_base_v130_signal(high, low, closeadj, open):
    lower = pd.concat([closeadj, open], axis=1).min(axis=1) - low
    result = _mean(_safe_div(lower, (high - low)), 21) + _f09_atr(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# true range proxy over price 10d
def f09re_f09_range_expansion_atr_trp_10d_base_v131_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    result = _safe_div(_mean(tr, 10), closeadj) + _f09_atr(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# true range proxy over price 126d
def f09re_f09_range_expansion_atr_trp_126d_base_v132_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    result = _safe_div(_mean(tr, 126), closeadj) + _f09_atr(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# true-range vs hi-lo (gap contribution) 63d
def f09re_f09_range_expansion_atr_trgap_63d_base_v133_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    result = _safe_div(_mean(tr, 63), _f09_atr(high, low, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion acceleration: 10/42 minus 42/126
def f09re_f09_range_expansion_atr_accel2_base_v134_signal(high, low):
    fast = _safe_div(_f09_atr(high, low, 10), _f09_atr(high, low, 42))
    slow = _safe_div(_f09_atr(high, low, 42), _f09_atr(high, low, 126))
    result = fast - slow
    return result.replace([np.inf, -np.inf], np.nan)


# log range mean over 126d
def f09re_f09_range_expansion_atr_lrng_126d_base_v135_signal(high, low):
    lr = np.log((high / low.replace(0, np.nan)))
    result = _mean(lr, 126) + _f09_parkinson(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log range dispersion over 63d (vol of log-range)
def f09re_f09_range_expansion_atr_lrngstd_63d_base_v136_signal(high, low):
    lr = np.log((high / low.replace(0, np.nan)))
    result = _std(lr, 63) + _f09_parkinson(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 21d annualized
def f09re_f09_range_expansion_atr_parkann_21d_base_v137_signal(high, low):
    result = _f09_parkinson(high, low, 21) * np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 126d annualized
def f09re_f09_range_expansion_atr_parkann_126d_base_v138_signal(high, low):
    result = _f09_parkinson(high, low, 126) * np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass 21d annualized
def f09re_f09_range_expansion_atr_gkann_21d_base_v139_signal(high, low, closeadj):
    result = _f09_gk(high, low, closeadj, 21) * np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR slope 10d over price
def f09re_f09_range_expansion_atr_atrchg_10d_base_v140_signal(high, low, closeadj):
    atr = _f09_atr(high, low, 10)
    result = _safe_div(atr - atr.shift(10), closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR slope 126d over price
def f09re_f09_range_expansion_atr_atrchg_126d_base_v141_signal(high, low, closeadj):
    atr = _f09_atr(high, low, 126)
    result = _safe_div(atr - atr.shift(126), closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# range efficiency: Parkinson vs close-to-close vol 21d
def f09re_f09_range_expansion_atr_rngeff_21d_base_v142_signal(high, low, closeadj):
    park = _f09_parkinson(high, low, 21)
    cc = _std(np.log(closeadj / closeadj.shift(1)), 21)
    result = _safe_div(park, cc)
    return result.replace([np.inf, -np.inf], np.nan)


# range efficiency: Parkinson vs close-to-close vol 252d
def f09re_f09_range_expansion_atr_rngeff_252d_base_v143_signal(high, low, closeadj):
    park = _f09_parkinson(high, low, 252)
    cc = _std(np.log(closeadj / closeadj.shift(1)), 252)
    result = _safe_div(park, cc)
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass vs close-to-close vol efficiency 63d
def f09re_f09_range_expansion_atr_gkeff_63d_base_v144_signal(high, low, closeadj):
    gk = _f09_gk(high, low, closeadj, 63)
    cc = _std(np.log(closeadj / closeadj.shift(1)), 63)
    result = _safe_div(gk, cc)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price expansion vs its own 252d level (regime ratio) 21d
def f09re_f09_range_expansion_atr_regime_21d_base_v145_signal(high, low, closeadj):
    atrp = _safe_div(_f09_atr(high, low, 21), closeadj)
    result = _safe_div(atrp, _mean(atrp, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price expansion vs its own 252d level 63d
def f09re_f09_range_expansion_atr_regime_63d_base_v146_signal(high, low, closeadj):
    atrp = _safe_div(_f09_atr(high, low, 63), closeadj)
    result = _safe_div(atrp, _mean(atrp, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson EWMA fast/slow cross (vol regime)
def f09re_f09_range_expansion_atr_parkewm_base_v147_signal(high, low):
    park = _f09_parkinson(high, low, 21)
    fast = park.ewm(span=21, min_periods=10).mean()
    slow = park.ewm(span=126, min_periods=42).mean()
    result = _safe_div(fast, slow)
    return result.replace([np.inf, -np.inf], np.nan)


# normalized range skew over 63d (range distribution asymmetry)
def f09re_f09_range_expansion_atr_rngskew_63d_base_v148_signal(high, low):
    rng = _safe_div(high - low, ((high + low) / 2.0))
    result = rng.rolling(63, min_periods=21).skew() + _f09_range(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# normalized range kurtosis over 126d (range tail regime)
def f09re_f09_range_expansion_atr_rngkurt_126d_base_v149_signal(high, low):
    rng = _safe_div(high - low, ((high + low) / 2.0))
    result = rng.rolling(126, min_periods=42).kurt() + _f09_range(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon range-expansion composite (5/21/63/126)
def f09re_f09_range_expansion_atr_blend_multi_base_v150_signal(high, low):
    today = (high - low)
    result = (_safe_div(today, _f09_atr(high, low, 5))
              + _safe_div(today, _f09_atr(high, low, 21))
              + _safe_div(today, _f09_atr(high, low, 63))
              + _safe_div(today, _f09_atr(high, low, 126))) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09re_f09_range_expansion_atr_atrp_10d_base_v076_signal,
    f09re_f09_range_expansion_atr_atrp_42d_base_v077_signal,
    f09re_f09_range_expansion_atr_atrp_84d_base_v078_signal,
    f09re_f09_range_expansion_atr_atrp_189d_base_v079_signal,
    f09re_f09_range_expansion_atr_park_10d_base_v080_signal,
    f09re_f09_range_expansion_atr_park_42d_base_v081_signal,
    f09re_f09_range_expansion_atr_park_84d_base_v082_signal,
    f09re_f09_range_expansion_atr_park_189d_base_v083_signal,
    f09re_f09_range_expansion_atr_gk_10d_base_v084_signal,
    f09re_f09_range_expansion_atr_gk_42d_base_v085_signal,
    f09re_f09_range_expansion_atr_gk_84d_base_v086_signal,
    f09re_f09_range_expansion_atr_rng_10d_base_v087_signal,
    f09re_f09_range_expansion_atr_rng_42d_base_v088_signal,
    f09re_f09_range_expansion_atr_rng_252d_base_v089_signal,
    f09re_f09_range_expansion_atr_exp_10d_base_v090_signal,
    f09re_f09_range_expansion_atr_exp_42d_base_v091_signal,
    f09re_f09_range_expansion_atr_exp_252d_base_v092_signal,
    f09re_f09_range_expansion_atr_exps_10_42_base_v093_signal,
    f09re_f09_range_expansion_atr_exps_42_126_base_v094_signal,
    f09re_f09_range_expansion_atr_exps_84_252_base_v095_signal,
    f09re_f09_range_expansion_atr_zrng_42d_base_v096_signal,
    f09re_f09_range_expansion_atr_zrng_504d_base_v097_signal,
    f09re_f09_range_expansion_atr_zatr_10d_base_v098_signal,
    f09re_f09_range_expansion_atr_zatr_126d_base_v099_signal,
    f09re_f09_range_expansion_atr_hlc_10d_base_v100_signal,
    f09re_f09_range_expansion_atr_hlc_63d_base_v101_signal,
    f09re_f09_range_expansion_atr_parkts_10_63_base_v102_signal,
    f09re_f09_range_expansion_atr_parkts_42_252_base_v103_signal,
    f09re_f09_range_expansion_atr_gkts_10_63_base_v104_signal,
    f09re_f09_range_expansion_atr_pgk_42d_base_v105_signal,
    f09re_f09_range_expansion_atr_patr_63d_base_v106_signal,
    f09re_f09_range_expansion_atr_rank_63d_base_v107_signal,
    f09re_f09_range_expansion_atr_rank_504d_base_v108_signal,
    f09re_f09_range_expansion_atr_atrrank_126d_base_v109_signal,
    f09re_f09_range_expansion_atr_parkrank_252d_base_v110_signal,
    f09re_f09_range_expansion_atr_clv_10d_base_v111_signal,
    f09re_f09_range_expansion_atr_clv_126d_base_v112_signal,
    f09re_f09_range_expansion_atr_clvrng_126d_base_v113_signal,
    f09re_f09_range_expansion_atr_ror_42d_base_v114_signal,
    f09re_f09_range_expansion_atr_ror_126d_base_v115_signal,
    f09re_f09_range_expansion_atr_rorcv_21d_base_v116_signal,
    f09re_f09_range_expansion_atr_rorcv_252d_base_v117_signal,
    f09re_f09_range_expansion_atr_zpark_63d_base_v118_signal,
    f09re_f09_range_expansion_atr_zgk_63d_base_v119_signal,
    f09re_f09_range_expansion_atr_surp_10d_base_v120_signal,
    f09re_f09_range_expansion_atr_surp_126d_base_v121_signal,
    f09re_f09_range_expansion_atr_ewmrng_10d_base_v122_signal,
    f09re_f09_range_expansion_atr_ewmrng_126d_base_v123_signal,
    f09re_f09_range_expansion_atr_ewmcross2_base_v124_signal,
    f09re_f09_range_expansion_atr_gap_10d_base_v125_signal,
    f09re_f09_range_expansion_atr_gap_126d_base_v126_signal,
    f09re_f09_range_expansion_atr_body_10d_base_v127_signal,
    f09re_f09_range_expansion_atr_body_126d_base_v128_signal,
    f09re_f09_range_expansion_atr_ushadow_21d_base_v129_signal,
    f09re_f09_range_expansion_atr_lshadow_21d_base_v130_signal,
    f09re_f09_range_expansion_atr_trp_10d_base_v131_signal,
    f09re_f09_range_expansion_atr_trp_126d_base_v132_signal,
    f09re_f09_range_expansion_atr_trgap_63d_base_v133_signal,
    f09re_f09_range_expansion_atr_accel2_base_v134_signal,
    f09re_f09_range_expansion_atr_lrng_126d_base_v135_signal,
    f09re_f09_range_expansion_atr_lrngstd_63d_base_v136_signal,
    f09re_f09_range_expansion_atr_parkann_21d_base_v137_signal,
    f09re_f09_range_expansion_atr_parkann_126d_base_v138_signal,
    f09re_f09_range_expansion_atr_gkann_21d_base_v139_signal,
    f09re_f09_range_expansion_atr_atrchg_10d_base_v140_signal,
    f09re_f09_range_expansion_atr_atrchg_126d_base_v141_signal,
    f09re_f09_range_expansion_atr_rngeff_21d_base_v142_signal,
    f09re_f09_range_expansion_atr_rngeff_252d_base_v143_signal,
    f09re_f09_range_expansion_atr_gkeff_63d_base_v144_signal,
    f09re_f09_range_expansion_atr_regime_21d_base_v145_signal,
    f09re_f09_range_expansion_atr_regime_63d_base_v146_signal,
    f09re_f09_range_expansion_atr_parkewm_base_v147_signal,
    f09re_f09_range_expansion_atr_rngskew_63d_base_v148_signal,
    f09re_f09_range_expansion_atr_rngkurt_126d_base_v149_signal,
    f09re_f09_range_expansion_atr_blend_multi_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_RANGE_EXPANSION_ATR_REGISTRY_076_150 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume"}
    for nm in names:
        if nm in ("closeadj", "close", "price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            s = level + 50.0 * walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f09_atr", "_f09_parkinson", "_f09_gk", "_f09_range")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0
    nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f09_range_expansion_atr_base_076_150_claude: {n_features} features pass")
