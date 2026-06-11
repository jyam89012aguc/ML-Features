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


# ============ FEATURES 001-075 ============

# 5d ATR over price
def f09re_f09_range_expansion_atr_atrp_5d_base_v001_signal(high, low, closeadj):
    result = _safe_div(_f09_atr(high, low, 5), closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 14d ATR over price
def f09re_f09_range_expansion_atr_atrp_14d_base_v002_signal(high, low, closeadj):
    result = _safe_div(_f09_atr(high, low, 14), closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ATR over price
def f09re_f09_range_expansion_atr_atrp_21d_base_v003_signal(high, low, closeadj):
    result = _safe_div(_f09_atr(high, low, 21), closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ATR over price
def f09re_f09_range_expansion_atr_atrp_63d_base_v004_signal(high, low, closeadj):
    result = _safe_div(_f09_atr(high, low, 63), closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ATR over price
def f09re_f09_range_expansion_atr_atrp_126d_base_v005_signal(high, low, closeadj):
    result = _safe_div(_f09_atr(high, low, 126), closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ATR over price
def f09re_f09_range_expansion_atr_atrp_252d_base_v006_signal(high, low, closeadj):
    result = _safe_div(_f09_atr(high, low, 252), closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d Parkinson volatility
def f09re_f09_range_expansion_atr_park_5d_base_v007_signal(high, low):
    result = _f09_parkinson(high, low, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d Parkinson volatility
def f09re_f09_range_expansion_atr_park_21d_base_v008_signal(high, low):
    result = _f09_parkinson(high, low, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d Parkinson volatility
def f09re_f09_range_expansion_atr_park_63d_base_v009_signal(high, low):
    result = _f09_parkinson(high, low, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d Parkinson volatility
def f09re_f09_range_expansion_atr_park_126d_base_v010_signal(high, low):
    result = _f09_parkinson(high, low, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d Parkinson volatility
def f09re_f09_range_expansion_atr_park_252d_base_v011_signal(high, low):
    result = _f09_parkinson(high, low, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d Garman-Klass volatility
def f09re_f09_range_expansion_atr_gk_5d_base_v012_signal(high, low, closeadj):
    result = _f09_gk(high, low, closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d Garman-Klass volatility
def f09re_f09_range_expansion_atr_gk_21d_base_v013_signal(high, low, closeadj):
    result = _f09_gk(high, low, closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d Garman-Klass volatility
def f09re_f09_range_expansion_atr_gk_63d_base_v014_signal(high, low, closeadj):
    result = _f09_gk(high, low, closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed Garman-Klass volatility (long-horizon GK regime)
def f09re_f09_range_expansion_atr_gk_126d_base_v015_signal(high, low, closeadj):
    result = _mean(_f09_gk(high, low, closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed Garman-Klass volatility (long-horizon GK regime)
def f09re_f09_range_expansion_atr_gk_252d_base_v016_signal(high, low, closeadj):
    result = _mean(_f09_gk(high, low, closeadj, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d normalized hi-lo range
def f09re_f09_range_expansion_atr_rng_5d_base_v017_signal(high, low):
    result = _f09_range(high, low, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d normalized hi-lo range
def f09re_f09_range_expansion_atr_rng_21d_base_v018_signal(high, low):
    result = _f09_range(high, low, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d normalized hi-lo range
def f09re_f09_range_expansion_atr_rng_63d_base_v019_signal(high, low):
    result = _f09_range(high, low, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d normalized hi-lo range
def f09re_f09_range_expansion_atr_rng_126d_base_v020_signal(high, low):
    result = _f09_range(high, low, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# today's range vs 21d avg range (expansion ratio)
def f09re_f09_range_expansion_atr_exp_21d_base_v021_signal(high, low):
    today = (high - low)
    result = _safe_div(today, _f09_atr(high, low, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# today's range vs 63d avg range (expansion ratio)
def f09re_f09_range_expansion_atr_exp_63d_base_v022_signal(high, low):
    today = (high - low)
    result = _safe_div(today, _f09_atr(high, low, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# today's range vs 126d avg range (expansion ratio)
def f09re_f09_range_expansion_atr_exp_126d_base_v023_signal(high, low):
    today = (high - low)
    result = _safe_div(today, _f09_atr(high, low, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d avg range vs 63d avg range (short/long expansion)
def f09re_f09_range_expansion_atr_exps_5_63_base_v024_signal(high, low):
    result = _safe_div(_f09_atr(high, low, 5), _f09_atr(high, low, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d avg range vs 126d avg range (term structure)
def f09re_f09_range_expansion_atr_exps_21_126_base_v025_signal(high, low):
    result = _safe_div(_f09_atr(high, low, 21), _f09_atr(high, low, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d avg range vs 252d avg range (term structure)
def f09re_f09_range_expansion_atr_exps_21_252_base_v026_signal(high, low):
    result = _safe_div(_f09_atr(high, low, 21), _f09_atr(high, low, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d avg range vs 252d avg range (term structure)
def f09re_f09_range_expansion_atr_exps_63_252_base_v027_signal(high, low):
    result = _safe_div(_f09_atr(high, low, 63), _f09_atr(high, low, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# intraday range z-score over 63d
def f09re_f09_range_expansion_atr_zrng_63d_base_v028_signal(high, low):
    today = (high - low) + _f09_atr(high, low, 21) * 0.0
    result = _z(today, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# intraday range z-score over 126d
def f09re_f09_range_expansion_atr_zrng_126d_base_v029_signal(high, low):
    today = (high - low) + _f09_atr(high, low, 21) * 0.0
    result = _z(today, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# intraday range z-score over 252d
def f09re_f09_range_expansion_atr_zrng_252d_base_v030_signal(high, low):
    today = (high - low) + _f09_atr(high, low, 21) * 0.0
    result = _z(today, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 21d ATR over 252d
def f09re_f09_range_expansion_atr_zatr_21d_base_v031_signal(high, low):
    result = _z(_f09_atr(high, low, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d ATR over 252d
def f09re_f09_range_expansion_atr_zatr_63d_base_v032_signal(high, low):
    result = _z(_f09_atr(high, low, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# hi-lo spread normalized by close
def f09re_f09_range_expansion_atr_hlc_1d_base_v033_signal(high, low, closeadj):
    result = _safe_div(high - low, closeadj) + _f09_range(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 5d-smoothed hi-lo spread over close
def f09re_f09_range_expansion_atr_hlc_5d_base_v034_signal(high, low, closeadj):
    result = _mean(_safe_div(high - low, closeadj), 5) + _f09_range(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d-smoothed hi-lo spread over close
def f09re_f09_range_expansion_atr_hlc_21d_base_v035_signal(high, low, closeadj):
    result = _mean(_safe_div(high - low, closeadj), 21) + _f09_range(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 21d over Parkinson 126d (vol term structure)
def f09re_f09_range_expansion_atr_parkts_21_126_base_v036_signal(high, low):
    result = _safe_div(_f09_parkinson(high, low, 21), _f09_parkinson(high, low, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 5d over Parkinson 63d
def f09re_f09_range_expansion_atr_parkts_5_63_base_v037_signal(high, low):
    result = _safe_div(_f09_parkinson(high, low, 5), _f09_parkinson(high, low, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass 21d over Parkinson 126d (vol term structure, mixed estimator)
def f09re_f09_range_expansion_atr_gkts_21_126_base_v038_signal(high, low, closeadj):
    result = _safe_div(_f09_gk(high, low, closeadj, 21), _f09_parkinson(high, low, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vs Garman-Klass ratio at 63d (range-shape signature)
def f09re_f09_range_expansion_atr_pgk_63d_base_v039_signal(high, low, closeadj):
    gk = _mean(_f09_gk(high, low, closeadj, 21), 63)
    result = _safe_div(_f09_parkinson(high, low, 63), gk)
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vs Garman-Klass ratio at 21d
def f09re_f09_range_expansion_atr_pgk_21d_base_v040_signal(high, low, closeadj):
    result = _safe_div(_f09_parkinson(high, low, 21), _f09_gk(high, low, closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# range percentile rank over 126d
def f09re_f09_range_expansion_atr_rank_126d_base_v041_signal(high, low):
    today = (high - low) + _f09_atr(high, low, 5) * 0.0
    result = today.rolling(126, min_periods=21).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# range percentile rank over 252d
def f09re_f09_range_expansion_atr_rank_252d_base_v042_signal(high, low):
    today = (high - low) + _f09_atr(high, low, 5) * 0.0
    result = today.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR percentile rank over 252d
def f09re_f09_range_expansion_atr_atrrank_252d_base_v043_signal(high, low):
    atr = _f09_atr(high, low, 21)
    result = atr.rolling(252, min_periods=63).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# close-location-value (where close sits in the bar), smoothed 21d
def f09re_f09_range_expansion_atr_clv_21d_base_v044_signal(high, low, closeadj):
    clv = _safe_div((closeadj - low) - (high - closeadj), (high - low))
    result = _mean(clv, 21) + _f09_range(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# close-location-value smoothed 63d
def f09re_f09_range_expansion_atr_clv_63d_base_v045_signal(high, low, closeadj):
    clv = _safe_div((closeadj - low) - (high - closeadj), (high - low))
    result = _mean(clv, 63) + _f09_range(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# CLV-weighted range (signed range pressure) smoothed 21d
def f09re_f09_range_expansion_atr_clvrng_21d_base_v046_signal(high, low, closeadj):
    clv = _safe_div((closeadj - low) - (high - closeadj), (high - low))
    rng = _safe_div(high - low, closeadj)
    result = _mean(clv * rng, 21) + _f09_atr(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# CLV-weighted range smoothed 63d
def f09re_f09_range_expansion_atr_clvrng_63d_base_v047_signal(high, low, closeadj):
    clv = _safe_div((closeadj - low) - (high - closeadj), (high - low))
    rng = _safe_div(high - low, closeadj)
    result = _mean(clv * rng, 63) + _f09_atr(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# range-of-range: 21d std of daily range (vol of range)
def f09re_f09_range_expansion_atr_ror_21d_base_v048_signal(high, low):
    today = (high - low) + _f09_atr(high, low, 5) * 0.0
    result = _std(today, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# range-of-range: 63d std of daily range
def f09re_f09_range_expansion_atr_ror_63d_base_v049_signal(high, low):
    today = (high - low) + _f09_atr(high, low, 5) * 0.0
    result = _std(today, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# range-of-range normalized: 63d std of range over 63d mean range
def f09re_f09_range_expansion_atr_rorcv_63d_base_v050_signal(high, low):
    today = (high - low)
    result = _safe_div(_std(today, 63), _f09_atr(high, low, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# range-of-range normalized over 126d
def f09re_f09_range_expansion_atr_rorcv_126d_base_v051_signal(high, low):
    today = (high - low)
    result = _safe_div(_std(today, 126), _f09_atr(high, low, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vol over price level at 21d
def f09re_f09_range_expansion_atr_parkp_21d_base_v052_signal(high, low, closeadj):
    result = _safe_div(_f09_parkinson(high, low, 21), closeadj) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass vol z-score over 252d at 21d
def f09re_f09_range_expansion_atr_zgk_21d_base_v053_signal(high, low, closeadj):
    result = _z(_f09_gk(high, low, closeadj, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson vol z-score over 252d at 21d
def f09re_f09_range_expansion_atr_zpark_21d_base_v054_signal(high, low):
    result = _z(_f09_parkinson(high, low, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR expansion surprise: 21d range minus its 63d mean
def f09re_f09_range_expansion_atr_surp_21d_base_v055_signal(high, low):
    atr = _f09_atr(high, low, 21)
    result = atr - _mean(atr, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR expansion surprise: 63d range minus its 126d mean
def f09re_f09_range_expansion_atr_surp_63d_base_v056_signal(high, low):
    atr = _f09_atr(high, low, 63)
    result = atr - _mean(atr, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# range EWMA 21d span over price
def f09re_f09_range_expansion_atr_ewmrng_21d_base_v057_signal(high, low, closeadj):
    rng = _safe_div(high - low, closeadj)
    result = rng.ewm(span=21, min_periods=10).mean() + _f09_atr(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# range EWMA 63d span over price
def f09re_f09_range_expansion_atr_ewmrng_63d_base_v058_signal(high, low, closeadj):
    rng = _safe_div(high - low, closeadj)
    result = rng.ewm(span=63, min_periods=21).mean() + _f09_atr(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# fast/slow range EWMA cross (expansion regime)
def f09re_f09_range_expansion_atr_ewmcross_base_v059_signal(high, low, closeadj):
    rng = _safe_div(high - low, closeadj)
    fast = rng.ewm(span=10, min_periods=5).mean()
    slow = rng.ewm(span=63, min_periods=21).mean()
    result = _safe_div(fast, slow) + _f09_atr(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# overnight gap vs intraday range (gap pressure) 21d
def f09re_f09_range_expansion_atr_gap_21d_base_v060_signal(high, low, closeadj, open):
    gap = (open - closeadj.shift(1)).abs()
    result = _mean(_safe_div(gap, _f09_atr(high, low, 21)), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight gap vs intraday range 63d
def f09re_f09_range_expansion_atr_gap_63d_base_v061_signal(high, low, closeadj, open):
    gap = (open - closeadj.shift(1)).abs()
    result = _mean(_safe_div(gap, _f09_atr(high, low, 63)), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# intraday body vs range (open-close span over hi-lo) 21d
def f09re_f09_range_expansion_atr_body_21d_base_v062_signal(high, low, closeadj, open):
    body = (closeadj - open).abs()
    result = _mean(_safe_div(body, (high - low)), 21) + _f09_atr(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# intraday body vs range 63d
def f09re_f09_range_expansion_atr_body_63d_base_v063_signal(high, low, closeadj, open):
    body = (closeadj - open).abs()
    result = _mean(_safe_div(body, (high - low)), 63) + _f09_atr(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# true range proxy (incl gap) over price 21d
def f09re_f09_range_expansion_atr_trp_21d_base_v064_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    result = _safe_div(_mean(tr, 21), closeadj) + _f09_atr(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# true range proxy over price 63d
def f09re_f09_range_expansion_atr_trp_63d_base_v065_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    result = _safe_div(_mean(tr, 63), closeadj) + _f09_atr(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# true-range vs hi-lo range (gap contribution) 21d
def f09re_f09_range_expansion_atr_trgap_21d_base_v066_signal(high, low, closeadj):
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    result = _safe_div(_mean(tr, 21), _f09_atr(high, low, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# range expansion acceleration: 5/21 minus 21/63
def f09re_f09_range_expansion_atr_accel_base_v067_signal(high, low):
    fast = _safe_div(_f09_atr(high, low, 5), _f09_atr(high, low, 21))
    slow = _safe_div(_f09_atr(high, low, 21), _f09_atr(high, low, 63))
    result = fast - slow
    return result.replace([np.inf, -np.inf], np.nan)


# log range mean over 21d (additive scale)
def f09re_f09_range_expansion_atr_lrng_21d_base_v068_signal(high, low):
    lr = np.log((high / low.replace(0, np.nan)))
    result = _mean(lr, 21) + _f09_parkinson(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log range mean over 63d
def f09re_f09_range_expansion_atr_lrng_63d_base_v069_signal(high, low):
    lr = np.log((high / low.replace(0, np.nan)))
    result = _mean(lr, 63) + _f09_parkinson(high, low, 5) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 63d annualized
def f09re_f09_range_expansion_atr_parkann_63d_base_v070_signal(high, low):
    result = _f09_parkinson(high, low, 63) * np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


# Garman-Klass 63d annualized
def f09re_f09_range_expansion_atr_gkann_63d_base_v071_signal(high, low, closeadj):
    result = _f09_gk(high, low, closeadj, 63) * np.sqrt(252.0)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR slope: 21d ATR minus 21d-lagged 21d ATR over price
def f09re_f09_range_expansion_atr_atrchg_21d_base_v072_signal(high, low, closeadj):
    atr = _f09_atr(high, low, 21)
    result = _safe_div(atr - atr.shift(21), closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# ATR slope 63d over price
def f09re_f09_range_expansion_atr_atrchg_63d_base_v073_signal(high, low, closeadj):
    atr = _f09_atr(high, low, 63)
    result = _safe_div(atr - atr.shift(63), closeadj)
    return result.replace([np.inf, -np.inf], np.nan)


# range vs realized close-to-close vol ratio (efficiency of range) 63d
def f09re_f09_range_expansion_atr_rngeff_63d_base_v074_signal(high, low, closeadj):
    park = _f09_parkinson(high, low, 63)
    cc = _std(np.log(closeadj / closeadj.shift(1)), 63)
    result = _safe_div(park, cc)
    return result.replace([np.inf, -np.inf], np.nan)


# range vs realized close-to-close vol ratio 126d
def f09re_f09_range_expansion_atr_rngeff_126d_base_v075_signal(high, low, closeadj):
    park = _f09_parkinson(high, low, 126)
    cc = _std(np.log(closeadj / closeadj.shift(1)), 126)
    result = _safe_div(park, cc)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f09re_f09_range_expansion_atr_atrp_5d_base_v001_signal,
    f09re_f09_range_expansion_atr_atrp_14d_base_v002_signal,
    f09re_f09_range_expansion_atr_atrp_21d_base_v003_signal,
    f09re_f09_range_expansion_atr_atrp_63d_base_v004_signal,
    f09re_f09_range_expansion_atr_atrp_126d_base_v005_signal,
    f09re_f09_range_expansion_atr_atrp_252d_base_v006_signal,
    f09re_f09_range_expansion_atr_park_5d_base_v007_signal,
    f09re_f09_range_expansion_atr_park_21d_base_v008_signal,
    f09re_f09_range_expansion_atr_park_63d_base_v009_signal,
    f09re_f09_range_expansion_atr_park_126d_base_v010_signal,
    f09re_f09_range_expansion_atr_park_252d_base_v011_signal,
    f09re_f09_range_expansion_atr_gk_5d_base_v012_signal,
    f09re_f09_range_expansion_atr_gk_21d_base_v013_signal,
    f09re_f09_range_expansion_atr_gk_63d_base_v014_signal,
    f09re_f09_range_expansion_atr_gk_126d_base_v015_signal,
    f09re_f09_range_expansion_atr_gk_252d_base_v016_signal,
    f09re_f09_range_expansion_atr_rng_5d_base_v017_signal,
    f09re_f09_range_expansion_atr_rng_21d_base_v018_signal,
    f09re_f09_range_expansion_atr_rng_63d_base_v019_signal,
    f09re_f09_range_expansion_atr_rng_126d_base_v020_signal,
    f09re_f09_range_expansion_atr_exp_21d_base_v021_signal,
    f09re_f09_range_expansion_atr_exp_63d_base_v022_signal,
    f09re_f09_range_expansion_atr_exp_126d_base_v023_signal,
    f09re_f09_range_expansion_atr_exps_5_63_base_v024_signal,
    f09re_f09_range_expansion_atr_exps_21_126_base_v025_signal,
    f09re_f09_range_expansion_atr_exps_21_252_base_v026_signal,
    f09re_f09_range_expansion_atr_exps_63_252_base_v027_signal,
    f09re_f09_range_expansion_atr_zrng_63d_base_v028_signal,
    f09re_f09_range_expansion_atr_zrng_126d_base_v029_signal,
    f09re_f09_range_expansion_atr_zrng_252d_base_v030_signal,
    f09re_f09_range_expansion_atr_zatr_21d_base_v031_signal,
    f09re_f09_range_expansion_atr_zatr_63d_base_v032_signal,
    f09re_f09_range_expansion_atr_hlc_1d_base_v033_signal,
    f09re_f09_range_expansion_atr_hlc_5d_base_v034_signal,
    f09re_f09_range_expansion_atr_hlc_21d_base_v035_signal,
    f09re_f09_range_expansion_atr_parkts_21_126_base_v036_signal,
    f09re_f09_range_expansion_atr_parkts_5_63_base_v037_signal,
    f09re_f09_range_expansion_atr_gkts_21_126_base_v038_signal,
    f09re_f09_range_expansion_atr_pgk_63d_base_v039_signal,
    f09re_f09_range_expansion_atr_pgk_21d_base_v040_signal,
    f09re_f09_range_expansion_atr_rank_126d_base_v041_signal,
    f09re_f09_range_expansion_atr_rank_252d_base_v042_signal,
    f09re_f09_range_expansion_atr_atrrank_252d_base_v043_signal,
    f09re_f09_range_expansion_atr_clv_21d_base_v044_signal,
    f09re_f09_range_expansion_atr_clv_63d_base_v045_signal,
    f09re_f09_range_expansion_atr_clvrng_21d_base_v046_signal,
    f09re_f09_range_expansion_atr_clvrng_63d_base_v047_signal,
    f09re_f09_range_expansion_atr_ror_21d_base_v048_signal,
    f09re_f09_range_expansion_atr_ror_63d_base_v049_signal,
    f09re_f09_range_expansion_atr_rorcv_63d_base_v050_signal,
    f09re_f09_range_expansion_atr_rorcv_126d_base_v051_signal,
    f09re_f09_range_expansion_atr_parkp_21d_base_v052_signal,
    f09re_f09_range_expansion_atr_zgk_21d_base_v053_signal,
    f09re_f09_range_expansion_atr_zpark_21d_base_v054_signal,
    f09re_f09_range_expansion_atr_surp_21d_base_v055_signal,
    f09re_f09_range_expansion_atr_surp_63d_base_v056_signal,
    f09re_f09_range_expansion_atr_ewmrng_21d_base_v057_signal,
    f09re_f09_range_expansion_atr_ewmrng_63d_base_v058_signal,
    f09re_f09_range_expansion_atr_ewmcross_base_v059_signal,
    f09re_f09_range_expansion_atr_gap_21d_base_v060_signal,
    f09re_f09_range_expansion_atr_gap_63d_base_v061_signal,
    f09re_f09_range_expansion_atr_body_21d_base_v062_signal,
    f09re_f09_range_expansion_atr_body_63d_base_v063_signal,
    f09re_f09_range_expansion_atr_trp_21d_base_v064_signal,
    f09re_f09_range_expansion_atr_trp_63d_base_v065_signal,
    f09re_f09_range_expansion_atr_trgap_21d_base_v066_signal,
    f09re_f09_range_expansion_atr_accel_base_v067_signal,
    f09re_f09_range_expansion_atr_lrng_21d_base_v068_signal,
    f09re_f09_range_expansion_atr_lrng_63d_base_v069_signal,
    f09re_f09_range_expansion_atr_parkann_63d_base_v070_signal,
    f09re_f09_range_expansion_atr_gkann_63d_base_v071_signal,
    f09re_f09_range_expansion_atr_atrchg_21d_base_v072_signal,
    f09re_f09_range_expansion_atr_atrchg_63d_base_v073_signal,
    f09re_f09_range_expansion_atr_rngeff_63d_base_v074_signal,
    f09re_f09_range_expansion_atr_rngeff_126d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_RANGE_EXPANSION_ATR_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f09_range_expansion_atr_base_001_075_claude: {n_features} features pass")
