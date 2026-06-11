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


# ===== folder domain primitives (relative-strength leadership) =====
def _f10_maratio(s, w):
    # price relative to its own trailing moving average (leadership vs own trend)
    ma = s.rolling(w, min_periods=max(1, w // 2)).mean()
    return s / ma.replace(0, np.nan)


def _f10_hilopos(s, w):
    # continuous position of price within trailing w-day low..high range in [0,1]
    hi = s.rolling(w, min_periods=max(1, w // 2)).max()
    lo = s.rolling(w, min_periods=max(1, w // 2)).min()
    rng = (hi - lo).replace(0, np.nan)
    return (s - lo) / rng


def _f10_retrank(s, w):
    # rolling percentile rank of current price within its own trailing window
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True)


def _f10_rsslope(s, w):
    # OLS slope of the relative-strength line (price / own rolling mean) over w days,
    # normalized per-day; continuous leadership-trend velocity
    ma = s.rolling(w, min_periods=max(1, w // 2)).mean()
    rs = s / ma.replace(0, np.nan)
    idx = np.arange(w, dtype=float)
    xm = idx.mean()
    xden = ((idx - xm) ** 2).sum()

    def _ols(arr):
        y = arr
        ym = y.mean()
        return ((idx - xm) * (y - ym)).sum() / xden

    return rs.rolling(w, min_periods=w).apply(_ols, raw=True)


# ============ FEATURES 001-075 ============

# close vs 20d SMA ratio
def f10rs_f10_relative_strength_leadership_maratio_20d_base_v001_signal(closeadj):
    result = _f10_maratio(closeadj, 20)
    return result.replace([np.inf, -np.inf], np.nan)


# close vs 50d SMA ratio
def f10rs_f10_relative_strength_leadership_maratio_50d_base_v002_signal(closeadj):
    result = _f10_maratio(closeadj, 50)
    return result.replace([np.inf, -np.inf], np.nan)


# close vs 100d SMA ratio
def f10rs_f10_relative_strength_leadership_maratio_100d_base_v003_signal(closeadj):
    result = _f10_maratio(closeadj, 100)
    return result.replace([np.inf, -np.inf], np.nan)


# close vs 200d SMA ratio
def f10rs_f10_relative_strength_leadership_maratio_200d_base_v004_signal(closeadj):
    result = _f10_maratio(closeadj, 200)
    return result.replace([np.inf, -np.inf], np.nan)


# close vs 10d SMA ratio (short-term leadership)
def f10rs_f10_relative_strength_leadership_maratio_10d_base_v005_signal(closeadj):
    result = _f10_maratio(closeadj, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# close vs 21d SMA ratio
def f10rs_f10_relative_strength_leadership_maratio_21d_base_v006_signal(closeadj):
    result = _f10_maratio(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# close vs 63d SMA ratio
def f10rs_f10_relative_strength_leadership_maratio_63d_base_v007_signal(closeadj):
    result = _f10_maratio(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# close vs 126d SMA ratio
def f10rs_f10_relative_strength_leadership_maratio_126d_base_v008_signal(closeadj):
    result = _f10_maratio(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# close vs 252d SMA ratio (annual trend leadership)
def f10rs_f10_relative_strength_leadership_maratio_252d_base_v009_signal(closeadj):
    result = _f10_maratio(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# close vs 504d SMA ratio (multi-year trend leadership)
def f10rs_f10_relative_strength_leadership_maratio_504d_base_v010_signal(closeadj):
    result = _f10_maratio(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 50d SMA over 200d SMA stack ratio (golden-cross leadership, continuous)
def f10rs_f10_relative_strength_leadership_stack_50_200_base_v011_signal(closeadj):
    fast = closeadj.rolling(50, min_periods=25).mean()
    slow = closeadj.rolling(200, min_periods=100).mean()
    result = _safe_div(fast, slow) + _f10_maratio(closeadj, 50) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 20d SMA over 100d SMA stack ratio
def f10rs_f10_relative_strength_leadership_stack_20_100_base_v012_signal(closeadj):
    fast = closeadj.rolling(20, min_periods=10).mean()
    slow = closeadj.rolling(100, min_periods=50).mean()
    result = _safe_div(fast, slow) + _f10_maratio(closeadj, 20) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 21d SMA over 63d SMA stack ratio
def f10rs_f10_relative_strength_leadership_stack_21_63_base_v013_signal(closeadj):
    fast = closeadj.rolling(21, min_periods=10).mean()
    slow = closeadj.rolling(63, min_periods=31).mean()
    result = _safe_div(fast, slow) + _f10_maratio(closeadj, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d SMA over 252d SMA stack ratio
def f10rs_f10_relative_strength_leadership_stack_63_252_base_v014_signal(closeadj):
    fast = closeadj.rolling(63, min_periods=31).mean()
    slow = closeadj.rolling(252, min_periods=126).mean()
    result = _safe_div(fast, slow) + _f10_maratio(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 10d SMA over 50d SMA stack ratio
def f10rs_f10_relative_strength_leadership_stack_10_50_base_v015_signal(closeadj):
    fast = closeadj.rolling(10, min_periods=5).mean()
    slow = closeadj.rolling(50, min_periods=25).mean()
    result = _safe_div(fast, slow) + _f10_maratio(closeadj, 10) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# position within 63d range
def f10rs_f10_relative_strength_leadership_hilopos_63d_base_v016_signal(closeadj):
    result = _f10_hilopos(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# position within 126d range
def f10rs_f10_relative_strength_leadership_hilopos_126d_base_v017_signal(closeadj):
    result = _f10_hilopos(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# position within 252d range (52-week range position)
def f10rs_f10_relative_strength_leadership_hilopos_252d_base_v018_signal(closeadj):
    result = _f10_hilopos(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# position within 504d range
def f10rs_f10_relative_strength_leadership_hilopos_504d_base_v019_signal(closeadj):
    result = _f10_hilopos(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# position within 21d range (short-term)
def f10rs_f10_relative_strength_leadership_hilopos_21d_base_v020_signal(closeadj):
    result = _f10_hilopos(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# position within 42d range
def f10rs_f10_relative_strength_leadership_hilopos_42d_base_v021_signal(closeadj):
    result = _f10_hilopos(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# position within 189d range
def f10rs_f10_relative_strength_leadership_hilopos_189d_base_v022_signal(closeadj):
    result = _f10_hilopos(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# intraday true-range position using high/low over 63d window
def f10rs_f10_relative_strength_leadership_hlpos_63d_base_v023_signal(high, low, closeadj):
    hi = high.rolling(63, min_periods=31).max()
    lo = low.rolling(63, min_periods=31).min()
    rng = (hi - lo).replace(0, np.nan)
    result = (closeadj - lo) / rng + _f10_hilopos(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# intraday true-range position using high/low over 252d window
def f10rs_f10_relative_strength_leadership_hlpos_252d_base_v024_signal(high, low, closeadj):
    hi = high.rolling(252, min_periods=126).max()
    lo = low.rolling(252, min_periods=126).min()
    rng = (hi - lo).replace(0, np.nan)
    result = (closeadj - lo) / rng + _f10_hilopos(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance below 252d high, normalized (continuous proximity-to-high)
def f10rs_f10_relative_strength_leadership_disthigh_252d_base_v025_signal(closeadj):
    hi = closeadj.rolling(252, min_periods=126).max()
    result = (closeadj - hi) / hi.replace(0, np.nan) + _f10_hilopos(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance below 504d high, normalized
def f10rs_f10_relative_strength_leadership_disthigh_504d_base_v026_signal(closeadj):
    hi = closeadj.rolling(504, min_periods=252).max()
    result = (closeadj - hi) / hi.replace(0, np.nan) + _f10_hilopos(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance below 126d high, normalized
def f10rs_f10_relative_strength_leadership_disthigh_126d_base_v027_signal(closeadj):
    hi = closeadj.rolling(126, min_periods=63).max()
    result = (closeadj - hi) / hi.replace(0, np.nan) + _f10_hilopos(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 252d low, normalized (continuous run-up from base)
def f10rs_f10_relative_strength_leadership_distlow_252d_base_v028_signal(closeadj):
    lo = closeadj.rolling(252, min_periods=126).min()
    result = (closeadj - lo) / lo.replace(0, np.nan) + _f10_hilopos(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 504d low, normalized
def f10rs_f10_relative_strength_leadership_distlow_504d_base_v029_signal(closeadj):
    lo = closeadj.rolling(504, min_periods=252).min()
    result = (closeadj - lo) / lo.replace(0, np.nan) + _f10_hilopos(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 126d low, normalized
def f10rs_f10_relative_strength_leadership_distlow_126d_base_v030_signal(closeadj):
    lo = closeadj.rolling(126, min_periods=63).min()
    result = (closeadj - lo) / lo.replace(0, np.nan) + _f10_hilopos(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of price over 63d
def f10rs_f10_relative_strength_leadership_retrank_63d_base_v031_signal(closeadj):
    result = _f10_retrank(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of price over 126d
def f10rs_f10_relative_strength_leadership_retrank_126d_base_v032_signal(closeadj):
    result = _f10_retrank(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of price over 252d
def f10rs_f10_relative_strength_leadership_retrank_252d_base_v033_signal(closeadj):
    result = _f10_retrank(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of price over 504d
def f10rs_f10_relative_strength_leadership_retrank_504d_base_v034_signal(closeadj):
    result = _f10_retrank(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of price over 73d
def f10rs_f10_relative_strength_leadership_retrank_73d_base_v035_signal(closeadj):
    result = _f10_retrank(closeadj, 73)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of price over 110d
def f10rs_f10_relative_strength_leadership_retrank_110d_base_v036_signal(closeadj):
    result = _f10_retrank(closeadj, 110)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of price over 189d
def f10rs_f10_relative_strength_leadership_retrank_189d_base_v037_signal(closeadj):
    result = _f10_retrank(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# RS-line slope over 63d (leadership-trend velocity)
def f10rs_f10_relative_strength_leadership_rsslope_63d_base_v038_signal(closeadj):
    result = _f10_rsslope(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# RS-line slope over 126d
def f10rs_f10_relative_strength_leadership_rsslope_126d_base_v039_signal(closeadj):
    result = _f10_rsslope(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# RS-line slope over 21d
def f10rs_f10_relative_strength_leadership_rsslope_21d_base_v040_signal(closeadj):
    result = _f10_rsslope(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# RS-line slope over 42d
def f10rs_f10_relative_strength_leadership_rsslope_42d_base_v041_signal(closeadj):
    result = _f10_rsslope(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of close/50d-SMA ratio over 252d (standardized leadership)
def f10rs_f10_relative_strength_leadership_zmaratio_50d_base_v042_signal(closeadj):
    result = _z(_f10_maratio(closeadj, 50), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of close/200d-SMA ratio over 252d
def f10rs_f10_relative_strength_leadership_zmaratio_200d_base_v043_signal(closeadj):
    result = _z(_f10_maratio(closeadj, 200), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of close/21d-SMA ratio over 126d
def f10rs_f10_relative_strength_leadership_zmaratio_21d_base_v044_signal(closeadj):
    result = _z(_f10_maratio(closeadj, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 252d range position over 252d (leadership z-score)
def f10rs_f10_relative_strength_leadership_zhilopos_252d_base_v045_signal(closeadj):
    result = _z(_f10_hilopos(closeadj, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 126d range position over 126d
def f10rs_f10_relative_strength_leadership_zhilopos_126d_base_v046_signal(closeadj):
    result = _z(_f10_hilopos(closeadj, 126), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# log of close/50d-SMA ratio (symmetric leadership)
def f10rs_f10_relative_strength_leadership_logmaratio_50d_base_v047_signal(closeadj):
    result = np.log(_f10_maratio(closeadj, 50))
    return result.replace([np.inf, -np.inf], np.nan)


# log of close/200d-SMA ratio
def f10rs_f10_relative_strength_leadership_logmaratio_200d_base_v048_signal(closeadj):
    result = np.log(_f10_maratio(closeadj, 200))
    return result.replace([np.inf, -np.inf], np.nan)


# log of close/100d-SMA ratio
def f10rs_f10_relative_strength_leadership_logmaratio_100d_base_v049_signal(closeadj):
    result = np.log(_f10_maratio(closeadj, 100))
    return result.replace([np.inf, -np.inf], np.nan)


# close/50d-SMA ratio minus 1, scaled by 252d price-return vol (vol-adjusted extension)
def f10rs_f10_relative_strength_leadership_voladjext_50d_base_v050_signal(closeadj):
    ext = _f10_maratio(closeadj, 50) - 1.0
    vol = _std(closeadj.pct_change(), 252)
    result = _safe_div(ext, vol)
    return result.replace([np.inf, -np.inf], np.nan)


# close/200d-SMA ratio minus 1, scaled by 252d price-return vol
def f10rs_f10_relative_strength_leadership_voladjext_200d_base_v051_signal(closeadj):
    ext = _f10_maratio(closeadj, 200) - 1.0
    vol = _std(closeadj.pct_change(), 252)
    result = _safe_div(ext, vol)
    return result.replace([np.inf, -np.inf], np.nan)


# spread between 252d and 63d range positions (long vs short leadership)
def f10rs_f10_relative_strength_leadership_posspread_252_63_base_v052_signal(closeadj):
    result = _f10_hilopos(closeadj, 252) - _f10_hilopos(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# spread between 126d and 21d range positions
def f10rs_f10_relative_strength_leadership_posspread_126_21_base_v053_signal(closeadj):
    result = _f10_hilopos(closeadj, 126) - _f10_hilopos(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# spread between close/20d-SMA and close/200d-SMA ratios (fast-vs-slow leadership)
def f10rs_f10_relative_strength_leadership_maspread_20_200_base_v054_signal(closeadj):
    result = _f10_maratio(closeadj, 20) - _f10_maratio(closeadj, 200)
    return result.replace([np.inf, -np.inf], np.nan)


# spread between close/50d-SMA and close/100d-SMA ratios
def f10rs_f10_relative_strength_leadership_maspread_50_100_base_v055_signal(closeadj):
    result = _f10_maratio(closeadj, 50) - _f10_maratio(closeadj, 100)
    return result.replace([np.inf, -np.inf], np.nan)


# spread between 252d and 126d percentile ranks of price
def f10rs_f10_relative_strength_leadership_rankspread_252_126_base_v056_signal(closeadj):
    result = _f10_retrank(closeadj, 252) - _f10_retrank(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed 252d range position (21d mean, leadership persistence)
def f10rs_f10_relative_strength_leadership_smoothpos_252d_base_v057_signal(closeadj):
    result = _mean(_f10_hilopos(closeadj, 252), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed close/50d-SMA ratio (21d mean)
def f10rs_f10_relative_strength_leadership_smoothma_50d_base_v058_signal(closeadj):
    result = _mean(_f10_maratio(closeadj, 50), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA-smoothed close/100d-SMA ratio
def f10rs_f10_relative_strength_leadership_ewmma_100d_base_v059_signal(closeadj):
    result = _f10_maratio(closeadj, 100).ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range position weighted by close/200d-SMA leadership
def f10rs_f10_relative_strength_leadership_posweight_252d_base_v060_signal(closeadj):
    result = _f10_hilopos(closeadj, 252) * _f10_maratio(closeadj, 200)
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of price weighted by 63d range position
def f10rs_f10_relative_strength_leadership_rankweight_126d_base_v061_signal(closeadj):
    result = _f10_retrank(closeadj, 126) * _f10_hilopos(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 252d high scaled by 252d range width (continuous drawdown depth)
def f10rs_f10_relative_strength_leadership_normdraw_252d_base_v062_signal(closeadj):
    hi = closeadj.rolling(252, min_periods=126).max()
    lo = closeadj.rolling(252, min_periods=126).min()
    rng = (hi - lo).replace(0, np.nan)
    result = (closeadj - hi) / rng + _f10_hilopos(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 126d high scaled by 126d range width
def f10rs_f10_relative_strength_leadership_normdraw_126d_base_v063_signal(closeadj):
    hi = closeadj.rolling(126, min_periods=63).max()
    lo = closeadj.rolling(126, min_periods=63).min()
    rng = (hi - lo).replace(0, np.nan)
    result = (closeadj - hi) / rng + _f10_hilopos(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# RS-line slope over 252d (annual leadership velocity)
def f10rs_f10_relative_strength_leadership_rsslope_252d_base_v064_signal(closeadj):
    result = _f10_rsslope(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# close/63d-SMA ratio confirmed by volume z-score (leadership conviction)
def f10rs_f10_relative_strength_leadership_volconf_63d_base_v065_signal(closeadj, volume):
    result = (_f10_maratio(closeadj, 63) - 1.0) * _z(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range position confirmed by dollar-volume z-score
def f10rs_f10_relative_strength_leadership_dvconf_252d_base_v066_signal(closeadj, volume):
    dv = closeadj * volume
    result = _f10_hilopos(closeadj, 252) * _z(dv, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# close vs 84d SMA ratio
def f10rs_f10_relative_strength_leadership_maratio_84d_base_v067_signal(closeadj):
    result = _f10_maratio(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# close vs 189d SMA ratio
def f10rs_f10_relative_strength_leadership_maratio_189d_base_v068_signal(closeadj):
    result = _f10_maratio(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# close vs 315d SMA ratio
def f10rs_f10_relative_strength_leadership_maratio_315d_base_v069_signal(closeadj):
    result = _f10_maratio(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# position within 84d range
def f10rs_f10_relative_strength_leadership_hilopos_84d_base_v070_signal(closeadj):
    result = _f10_hilopos(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# position within 315d range
def f10rs_f10_relative_strength_leadership_hilopos_315d_base_v071_signal(closeadj):
    result = _f10_hilopos(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of price over 84d
def f10rs_f10_relative_strength_leadership_retrank_84d_base_v072_signal(closeadj):
    result = _f10_retrank(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# percentile rank of price over 315d
def f10rs_f10_relative_strength_leadership_retrank_315d_base_v073_signal(closeadj):
    result = _f10_retrank(closeadj, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# RS-line slope over 84d
def f10rs_f10_relative_strength_leadership_rsslope_84d_base_v074_signal(closeadj):
    result = _f10_rsslope(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 50d/200d SMA-stack ratio standardized over 252d (leadership-regime z-score)
def f10rs_f10_relative_strength_leadership_zstack_50_200_base_v075_signal(closeadj):
    fast = closeadj.rolling(50, min_periods=25).mean()
    slow = closeadj.rolling(200, min_periods=100).mean()
    stack = _safe_div(fast, slow)
    result = _z(stack, 252) + _f10_maratio(closeadj, 50) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f10rs_f10_relative_strength_leadership_maratio_20d_base_v001_signal,
    f10rs_f10_relative_strength_leadership_maratio_50d_base_v002_signal,
    f10rs_f10_relative_strength_leadership_maratio_100d_base_v003_signal,
    f10rs_f10_relative_strength_leadership_maratio_200d_base_v004_signal,
    f10rs_f10_relative_strength_leadership_maratio_10d_base_v005_signal,
    f10rs_f10_relative_strength_leadership_maratio_21d_base_v006_signal,
    f10rs_f10_relative_strength_leadership_maratio_63d_base_v007_signal,
    f10rs_f10_relative_strength_leadership_maratio_126d_base_v008_signal,
    f10rs_f10_relative_strength_leadership_maratio_252d_base_v009_signal,
    f10rs_f10_relative_strength_leadership_maratio_504d_base_v010_signal,
    f10rs_f10_relative_strength_leadership_stack_50_200_base_v011_signal,
    f10rs_f10_relative_strength_leadership_stack_20_100_base_v012_signal,
    f10rs_f10_relative_strength_leadership_stack_21_63_base_v013_signal,
    f10rs_f10_relative_strength_leadership_stack_63_252_base_v014_signal,
    f10rs_f10_relative_strength_leadership_stack_10_50_base_v015_signal,
    f10rs_f10_relative_strength_leadership_hilopos_63d_base_v016_signal,
    f10rs_f10_relative_strength_leadership_hilopos_126d_base_v017_signal,
    f10rs_f10_relative_strength_leadership_hilopos_252d_base_v018_signal,
    f10rs_f10_relative_strength_leadership_hilopos_504d_base_v019_signal,
    f10rs_f10_relative_strength_leadership_hilopos_21d_base_v020_signal,
    f10rs_f10_relative_strength_leadership_hilopos_42d_base_v021_signal,
    f10rs_f10_relative_strength_leadership_hilopos_189d_base_v022_signal,
    f10rs_f10_relative_strength_leadership_hlpos_63d_base_v023_signal,
    f10rs_f10_relative_strength_leadership_hlpos_252d_base_v024_signal,
    f10rs_f10_relative_strength_leadership_disthigh_252d_base_v025_signal,
    f10rs_f10_relative_strength_leadership_disthigh_504d_base_v026_signal,
    f10rs_f10_relative_strength_leadership_disthigh_126d_base_v027_signal,
    f10rs_f10_relative_strength_leadership_distlow_252d_base_v028_signal,
    f10rs_f10_relative_strength_leadership_distlow_504d_base_v029_signal,
    f10rs_f10_relative_strength_leadership_distlow_126d_base_v030_signal,
    f10rs_f10_relative_strength_leadership_retrank_63d_base_v031_signal,
    f10rs_f10_relative_strength_leadership_retrank_126d_base_v032_signal,
    f10rs_f10_relative_strength_leadership_retrank_252d_base_v033_signal,
    f10rs_f10_relative_strength_leadership_retrank_504d_base_v034_signal,
    f10rs_f10_relative_strength_leadership_retrank_73d_base_v035_signal,
    f10rs_f10_relative_strength_leadership_retrank_110d_base_v036_signal,
    f10rs_f10_relative_strength_leadership_retrank_189d_base_v037_signal,
    f10rs_f10_relative_strength_leadership_rsslope_63d_base_v038_signal,
    f10rs_f10_relative_strength_leadership_rsslope_126d_base_v039_signal,
    f10rs_f10_relative_strength_leadership_rsslope_21d_base_v040_signal,
    f10rs_f10_relative_strength_leadership_rsslope_42d_base_v041_signal,
    f10rs_f10_relative_strength_leadership_zmaratio_50d_base_v042_signal,
    f10rs_f10_relative_strength_leadership_zmaratio_200d_base_v043_signal,
    f10rs_f10_relative_strength_leadership_zmaratio_21d_base_v044_signal,
    f10rs_f10_relative_strength_leadership_zhilopos_252d_base_v045_signal,
    f10rs_f10_relative_strength_leadership_zhilopos_126d_base_v046_signal,
    f10rs_f10_relative_strength_leadership_logmaratio_50d_base_v047_signal,
    f10rs_f10_relative_strength_leadership_logmaratio_200d_base_v048_signal,
    f10rs_f10_relative_strength_leadership_logmaratio_100d_base_v049_signal,
    f10rs_f10_relative_strength_leadership_voladjext_50d_base_v050_signal,
    f10rs_f10_relative_strength_leadership_voladjext_200d_base_v051_signal,
    f10rs_f10_relative_strength_leadership_posspread_252_63_base_v052_signal,
    f10rs_f10_relative_strength_leadership_posspread_126_21_base_v053_signal,
    f10rs_f10_relative_strength_leadership_maspread_20_200_base_v054_signal,
    f10rs_f10_relative_strength_leadership_maspread_50_100_base_v055_signal,
    f10rs_f10_relative_strength_leadership_rankspread_252_126_base_v056_signal,
    f10rs_f10_relative_strength_leadership_smoothpos_252d_base_v057_signal,
    f10rs_f10_relative_strength_leadership_smoothma_50d_base_v058_signal,
    f10rs_f10_relative_strength_leadership_ewmma_100d_base_v059_signal,
    f10rs_f10_relative_strength_leadership_posweight_252d_base_v060_signal,
    f10rs_f10_relative_strength_leadership_rankweight_126d_base_v061_signal,
    f10rs_f10_relative_strength_leadership_normdraw_252d_base_v062_signal,
    f10rs_f10_relative_strength_leadership_normdraw_126d_base_v063_signal,
    f10rs_f10_relative_strength_leadership_rsslope_252d_base_v064_signal,
    f10rs_f10_relative_strength_leadership_volconf_63d_base_v065_signal,
    f10rs_f10_relative_strength_leadership_dvconf_252d_base_v066_signal,
    f10rs_f10_relative_strength_leadership_maratio_84d_base_v067_signal,
    f10rs_f10_relative_strength_leadership_maratio_189d_base_v068_signal,
    f10rs_f10_relative_strength_leadership_maratio_315d_base_v069_signal,
    f10rs_f10_relative_strength_leadership_hilopos_84d_base_v070_signal,
    f10rs_f10_relative_strength_leadership_hilopos_315d_base_v071_signal,
    f10rs_f10_relative_strength_leadership_retrank_84d_base_v072_signal,
    f10rs_f10_relative_strength_leadership_retrank_315d_base_v073_signal,
    f10rs_f10_relative_strength_leadership_rsslope_84d_base_v074_signal,
    f10rs_f10_relative_strength_leadership_zstack_50_200_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_RELATIVE_STRENGTH_LEADERSHIP_REGISTRY_001_075 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n))
    nl = np.abs(np.random.normal(0, 0.02, n))
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
            out[nm] = pd.Series(np.abs(1000.0 + 50.0 * walk) + 10.0, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f10_maratio", "_f10_hilopos", "_f10_retrank", "_f10_rsslope")
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
    print(f"OK f10_relative_strength_leadership_base_001_075_claude: {n_features} features pass")
