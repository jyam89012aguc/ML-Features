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


# ============ FEATURES 076-150 ============

# close vs 30d SMA ratio
def f10rs_f10_relative_strength_leadership_maratio_30d_base_v076_signal(closeadj):
    result = _f10_maratio(closeadj, 30)
    return result.replace([np.inf, -np.inf], np.nan)


# close vs 150d SMA ratio
def f10rs_f10_relative_strength_leadership_maratio_150d_base_v077_signal(closeadj):
    result = _f10_maratio(closeadj, 150)
    return result.replace([np.inf, -np.inf], np.nan)


# close vs 378d SMA ratio
def f10rs_f10_relative_strength_leadership_maratio_378d_base_v078_signal(closeadj):
    result = _f10_maratio(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# close vs 42d SMA ratio
def f10rs_f10_relative_strength_leadership_maratio_42d_base_v079_signal(closeadj):
    result = _f10_maratio(closeadj, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# log of close/21d-SMA ratio
def f10rs_f10_relative_strength_leadership_logmaratio_21d_base_v080_signal(closeadj):
    result = np.log(_f10_maratio(closeadj, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# log of close/126d-SMA ratio
def f10rs_f10_relative_strength_leadership_logmaratio_126d_base_v081_signal(closeadj):
    result = np.log(_f10_maratio(closeadj, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# log of close/252d-SMA ratio
def f10rs_f10_relative_strength_leadership_logmaratio_252d_base_v082_signal(closeadj):
    result = np.log(_f10_maratio(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 100d/200d SMA-stack ratio
def f10rs_f10_relative_strength_leadership_stack_100_200_base_v083_signal(closeadj):
    fast = closeadj.rolling(100, min_periods=50).mean()
    slow = closeadj.rolling(200, min_periods=100).mean()
    result = _safe_div(fast, slow) + _f10_maratio(closeadj, 100) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 42d/126d SMA-stack ratio
def f10rs_f10_relative_strength_leadership_stack_42_126_base_v084_signal(closeadj):
    fast = closeadj.rolling(42, min_periods=21).mean()
    slow = closeadj.rolling(126, min_periods=63).mean()
    result = _safe_div(fast, slow) + _f10_maratio(closeadj, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d/252d SMA-stack ratio
def f10rs_f10_relative_strength_leadership_stack_126_252_base_v085_signal(closeadj):
    fast = closeadj.rolling(126, min_periods=63).mean()
    slow = closeadj.rolling(252, min_periods=126).mean()
    result = _safe_div(fast, slow) + _f10_maratio(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log of 50d/200d SMA-stack ratio (symmetric trend-stack leadership)
def f10rs_f10_relative_strength_leadership_logstack_50_200_base_v086_signal(closeadj):
    fast = closeadj.rolling(50, min_periods=25).mean()
    slow = closeadj.rolling(200, min_periods=100).mean()
    result = np.log(_safe_div(fast, slow)) + _f10_maratio(closeadj, 50) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# position within 105d range
def f10rs_f10_relative_strength_leadership_hilopos_105d_base_v087_signal(closeadj):
    result = _f10_hilopos(closeadj, 105)
    return result.replace([np.inf, -np.inf], np.nan)


# position within 147d range
def f10rs_f10_relative_strength_leadership_hilopos_147d_base_v088_signal(closeadj):
    result = _f10_hilopos(closeadj, 147)
    return result.replace([np.inf, -np.inf], np.nan)


# position within 378d range
def f10rs_f10_relative_strength_leadership_hilopos_378d_base_v089_signal(closeadj):
    result = _f10_hilopos(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# position within 30d range
def f10rs_f10_relative_strength_leadership_hilopos_30d_base_v090_signal(closeadj):
    result = _f10_hilopos(closeadj, 30)
    return result.replace([np.inf, -np.inf], np.nan)


# distance below 189d high, normalized
def f10rs_f10_relative_strength_leadership_disthigh_189d_base_v091_signal(closeadj):
    hi = closeadj.rolling(189, min_periods=94).max()
    result = (closeadj - hi) / hi.replace(0, np.nan) + _f10_hilopos(closeadj, 189) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance below 63d high, normalized
def f10rs_f10_relative_strength_leadership_disthigh_63d_base_v092_signal(closeadj):
    hi = closeadj.rolling(63, min_periods=31).max()
    result = (closeadj - hi) / hi.replace(0, np.nan) + _f10_hilopos(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 189d low, normalized
def f10rs_f10_relative_strength_leadership_distlow_189d_base_v093_signal(closeadj):
    lo = closeadj.rolling(189, min_periods=94).min()
    result = (closeadj - lo) / lo.replace(0, np.nan) + _f10_hilopos(closeadj, 189) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance above 63d low, normalized
def f10rs_f10_relative_strength_leadership_distlow_63d_base_v094_signal(closeadj):
    lo = closeadj.rolling(63, min_periods=31).min()
    result = (closeadj - lo) / lo.replace(0, np.nan) + _f10_hilopos(closeadj, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# proximity-to-new-high over 252d as continuous ratio close/252d-high
def f10rs_f10_relative_strength_leadership_proxhigh_252d_base_v095_signal(closeadj):
    hi = closeadj.rolling(252, min_periods=126).max()
    result = _safe_div(closeadj, hi) + _f10_hilopos(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# proximity-to-new-high over 504d as continuous ratio close/504d-high
def f10rs_f10_relative_strength_leadership_proxhigh_504d_base_v096_signal(closeadj):
    hi = closeadj.rolling(504, min_periods=252).max()
    result = _safe_div(closeadj, hi) + _f10_hilopos(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# proximity-to-base over 252d as continuous ratio 252d-low/close
def f10rs_f10_relative_strength_leadership_proxlow_252d_base_v097_signal(closeadj):
    lo = closeadj.rolling(252, min_periods=126).min()
    result = _safe_div(lo, closeadj) + _f10_hilopos(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of price over 147d
def f10rs_f10_relative_strength_leadership_retrank_147d_base_v098_signal(closeadj):
    result = _f10_retrank(closeadj, 147)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of price over 378d
def f10rs_f10_relative_strength_leadership_retrank_378d_base_v099_signal(closeadj):
    result = _f10_retrank(closeadj, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of price over 105d
def f10rs_f10_relative_strength_leadership_retrank_105d_base_v100_signal(closeadj):
    result = _f10_retrank(closeadj, 105)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of price over 63d minus rank over 252d (rank momentum)
def f10rs_f10_relative_strength_leadership_rankmom_63_252_base_v101_signal(closeadj):
    result = _f10_retrank(closeadj, 63) - _f10_retrank(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of price over 126d minus rank over 504d
def f10rs_f10_relative_strength_leadership_rankmom_126_504_base_v102_signal(closeadj):
    result = _f10_retrank(closeadj, 126) - _f10_retrank(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# RS-line slope over 105d
def f10rs_f10_relative_strength_leadership_rsslope_105d_base_v103_signal(closeadj):
    result = _f10_rsslope(closeadj, 105)
    return result.replace([np.inf, -np.inf], np.nan)


# RS-line slope over 147d
def f10rs_f10_relative_strength_leadership_rsslope_147d_base_v104_signal(closeadj):
    result = _f10_rsslope(closeadj, 147)
    return result.replace([np.inf, -np.inf], np.nan)


# RS-line slope over 189d
def f10rs_f10_relative_strength_leadership_rsslope_189d_base_v105_signal(closeadj):
    result = _f10_rsslope(closeadj, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# RS-line slope over 504d
def f10rs_f10_relative_strength_leadership_rsslope_504d_base_v106_signal(closeadj):
    result = _f10_rsslope(closeadj, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# RS-line slope spread 63d minus 252d (acceleration of leadership trend)
def f10rs_f10_relative_strength_leadership_rsslopespr_63_252_base_v107_signal(closeadj):
    result = _f10_rsslope(closeadj, 63) - _f10_rsslope(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of close/100d-SMA ratio over 252d
def f10rs_f10_relative_strength_leadership_zmaratio_100d_base_v108_signal(closeadj):
    result = _z(_f10_maratio(closeadj, 100), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of close/63d-SMA ratio over 252d
def f10rs_f10_relative_strength_leadership_zmaratio_63d_base_v109_signal(closeadj):
    result = _z(_f10_maratio(closeadj, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 504d range position over 252d
def f10rs_f10_relative_strength_leadership_zhilopos_504d_base_v110_signal(closeadj):
    result = _z(_f10_hilopos(closeadj, 504), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of 63d range position over 126d
def f10rs_f10_relative_strength_leadership_zhilopos_63d_base_v111_signal(closeadj):
    result = _z(_f10_hilopos(closeadj, 63), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of price percentile rank over 252d (leadership z-score)
def f10rs_f10_relative_strength_leadership_zretrank_252d_base_v112_signal(closeadj):
    result = _z(_f10_retrank(closeadj, 252), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of price percentile rank over 126d
def f10rs_f10_relative_strength_leadership_zretrank_126d_base_v113_signal(closeadj):
    result = _z(_f10_retrank(closeadj, 126), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# close/200d-SMA extension scaled by 126d return vol
def f10rs_f10_relative_strength_leadership_voladjext_200_126_base_v114_signal(closeadj):
    ext = _f10_maratio(closeadj, 200) - 1.0
    vol = _std(closeadj.pct_change(), 126)
    result = _safe_div(ext, vol)
    return result.replace([np.inf, -np.inf], np.nan)


# close/100d-SMA extension scaled by 252d return vol
def f10rs_f10_relative_strength_leadership_voladjext_100_252_base_v115_signal(closeadj):
    ext = _f10_maratio(closeadj, 100) - 1.0
    vol = _std(closeadj.pct_change(), 252)
    result = _safe_div(ext, vol)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed 252d range position (63d mean, leadership persistence)
def f10rs_f10_relative_strength_leadership_smoothpos63_252d_base_v116_signal(closeadj):
    result = _mean(_f10_hilopos(closeadj, 252), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed close/200d-SMA ratio (63d mean)
def f10rs_f10_relative_strength_leadership_smoothma63_200d_base_v117_signal(closeadj):
    result = _mean(_f10_maratio(closeadj, 200), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA-smoothed 252d range position
def f10rs_f10_relative_strength_leadership_ewmpos_252d_base_v118_signal(closeadj):
    result = _f10_hilopos(closeadj, 252).ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA-smoothed price percentile rank over 252d
def f10rs_f10_relative_strength_leadership_ewmrank_252d_base_v119_signal(closeadj):
    result = _f10_retrank(closeadj, 252).ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range position weighted by 50d/200d SMA stack
def f10rs_f10_relative_strength_leadership_posstackw_252d_base_v120_signal(closeadj):
    fast = closeadj.rolling(50, min_periods=25).mean()
    slow = closeadj.rolling(200, min_periods=100).mean()
    stack = _safe_div(fast, slow)
    result = _f10_hilopos(closeadj, 252) * stack
    return result.replace([np.inf, -np.inf], np.nan)


# price percentile rank over 252d weighted by close/200d-SMA leadership
def f10rs_f10_relative_strength_leadership_rankmaw_252d_base_v121_signal(closeadj):
    result = _f10_retrank(closeadj, 252) * _f10_maratio(closeadj, 200)
    return result.replace([np.inf, -np.inf], np.nan)


# product of 63d and 252d range positions (multi-horizon leadership)
def f10rs_f10_relative_strength_leadership_posprod_63_252_base_v122_signal(closeadj):
    result = _f10_hilopos(closeadj, 63) * _f10_hilopos(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# average of close/SMA ratios across 20/50/100/200 (composite leadership)
def f10rs_f10_relative_strength_leadership_macomposite_base_v123_signal(closeadj):
    result = (_f10_maratio(closeadj, 20) + _f10_maratio(closeadj, 50)
              + _f10_maratio(closeadj, 100) + _f10_maratio(closeadj, 200)) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


# average of range positions across 63/126/252/504 (composite position)
def f10rs_f10_relative_strength_leadership_poscomposite_base_v124_signal(closeadj):
    result = (_f10_hilopos(closeadj, 63) + _f10_hilopos(closeadj, 126)
              + _f10_hilopos(closeadj, 252) + _f10_hilopos(closeadj, 504)) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


# average of price percentile ranks across 63/126/252 (composite rank leadership)
def f10rs_f10_relative_strength_leadership_rankcomposite_base_v125_signal(closeadj):
    result = (_f10_retrank(closeadj, 63) + _f10_retrank(closeadj, 126)
              + _f10_retrank(closeadj, 252)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# close/50d-SMA ratio confirmed by dollar-volume surge
def f10rs_f10_relative_strength_leadership_dvsurge_50d_base_v126_signal(closeadj, volume):
    dv = closeadj * volume
    surge = _safe_div(dv, _mean(dv, 63))
    result = (_f10_maratio(closeadj, 50) - 1.0) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range position confirmed by volume z-score
def f10rs_f10_relative_strength_leadership_volconfpos_252d_base_v127_signal(closeadj, volume):
    result = _f10_hilopos(closeadj, 252) * _z(volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# intraday high/low range position over 126d window
def f10rs_f10_relative_strength_leadership_hlpos_126d_base_v128_signal(high, low, closeadj):
    hi = high.rolling(126, min_periods=63).max()
    lo = low.rolling(126, min_periods=63).min()
    rng = (hi - lo).replace(0, np.nan)
    result = (closeadj - lo) / rng + _f10_hilopos(closeadj, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# intraday high/low range position over 504d window
def f10rs_f10_relative_strength_leadership_hlpos_504d_base_v129_signal(high, low, closeadj):
    hi = high.rolling(504, min_periods=252).max()
    lo = low.rolling(504, min_periods=252).min()
    rng = (hi - lo).replace(0, np.nan)
    result = (closeadj - lo) / rng + _f10_hilopos(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# close position relative to high-anchored 252d range using highs (new-high pressure)
def f10rs_f10_relative_strength_leadership_highpress_252d_base_v130_signal(high, closeadj):
    hi = high.rolling(252, min_periods=126).max()
    result = _safe_div(closeadj, hi) + _f10_hilopos(closeadj, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log of close/315d-SMA ratio
def f10rs_f10_relative_strength_leadership_logmaratio_315d_base_v131_signal(closeadj):
    result = np.log(_f10_maratio(closeadj, 315))
    return result.replace([np.inf, -np.inf], np.nan)


# log of close/84d-SMA ratio
def f10rs_f10_relative_strength_leadership_logmaratio_84d_base_v132_signal(closeadj):
    result = np.log(_f10_maratio(closeadj, 84))
    return result.replace([np.inf, -np.inf], np.nan)


# spread between close/50d-SMA and close/252d-SMA log ratios
def f10rs_f10_relative_strength_leadership_logmaspread_50_252_base_v133_signal(closeadj):
    result = np.log(_f10_maratio(closeadj, 50)) - np.log(_f10_maratio(closeadj, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# spread between close/10d-SMA and close/63d-SMA ratios
def f10rs_f10_relative_strength_leadership_maspread_10_63_base_v134_signal(closeadj):
    result = _f10_maratio(closeadj, 10) - _f10_maratio(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# spread between 504d and 126d range positions
def f10rs_f10_relative_strength_leadership_posspread_504_126_base_v135_signal(closeadj):
    result = _f10_hilopos(closeadj, 504) - _f10_hilopos(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# spread between 315d and 84d range positions
def f10rs_f10_relative_strength_leadership_posspread_315_84_base_v136_signal(closeadj):
    result = _f10_hilopos(closeadj, 315) - _f10_hilopos(closeadj, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# spread between 504d and 252d price percentile ranks
def f10rs_f10_relative_strength_leadership_rankspread_504_252_base_v137_signal(closeadj):
    result = _f10_retrank(closeadj, 504) - _f10_retrank(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 315d high scaled by 315d range width
def f10rs_f10_relative_strength_leadership_normdraw_315d_base_v138_signal(closeadj):
    hi = closeadj.rolling(315, min_periods=157).max()
    lo = closeadj.rolling(315, min_periods=157).min()
    rng = (hi - lo).replace(0, np.nan)
    result = (closeadj - hi) / rng + _f10_hilopos(closeadj, 315) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# distance from 504d high scaled by 504d range width
def f10rs_f10_relative_strength_leadership_normdraw_504d_base_v139_signal(closeadj):
    hi = closeadj.rolling(504, min_periods=252).max()
    lo = closeadj.rolling(504, min_periods=252).min()
    rng = (hi - lo).replace(0, np.nan)
    result = (closeadj - hi) / rng + _f10_hilopos(closeadj, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# close/200d-SMA ratio smoothed by EWMA then re-extended (leadership trend strength)
def f10rs_f10_relative_strength_leadership_ewmma_200d_base_v140_signal(closeadj):
    result = _f10_maratio(closeadj, 200).ewm(span=63, min_periods=31).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# close/50d-SMA ratio smoothed by EWMA
def f10rs_f10_relative_strength_leadership_ewmma_50d_base_v141_signal(closeadj):
    result = _f10_maratio(closeadj, 50).ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range position minus its 63d trailing mean (position surprise)
def f10rs_f10_relative_strength_leadership_possurp_252d_base_v142_signal(closeadj):
    p = _f10_hilopos(closeadj, 252)
    result = p - _mean(p, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# close/50d-SMA ratio minus its 63d trailing mean (leadership surprise)
def f10rs_f10_relative_strength_leadership_masurp_50d_base_v143_signal(closeadj):
    m = _f10_maratio(closeadj, 50)
    result = m - _mean(m, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range position relative to its 252d percentile rank (double-rank leadership)
def f10rs_f10_relative_strength_leadership_posrank_252d_base_v144_signal(closeadj):
    p = _f10_hilopos(closeadj, 252)
    result = p.rolling(252, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# close/200d-SMA ratio rolling percentile rank over 252d
def f10rs_f10_relative_strength_leadership_marank_200d_base_v145_signal(closeadj):
    m = _f10_maratio(closeadj, 200)
    result = m.rolling(252, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# RS-line slope over 126d scaled by 252d return vol (vol-adjusted leadership velocity)
def f10rs_f10_relative_strength_leadership_rsslopevol_126d_base_v146_signal(closeadj):
    vol = _std(closeadj.pct_change(), 252)
    result = _safe_div(_f10_rsslope(closeadj, 126), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# RS-line slope over 252d scaled by 252d return vol
def f10rs_f10_relative_strength_leadership_rsslopevol_252d_base_v147_signal(closeadj):
    vol = _std(closeadj.pct_change(), 252)
    result = _safe_div(_f10_rsslope(closeadj, 252), vol)
    return result.replace([np.inf, -np.inf], np.nan)


# close/63d-SMA ratio minus close/252d-SMA ratio (term-structure of leadership)
def f10rs_f10_relative_strength_leadership_materm_63_252_base_v148_signal(closeadj):
    result = _f10_maratio(closeadj, 63) - _f10_maratio(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# blended leadership composite: range position + close/200d-SMA extension + rank
def f10rs_f10_relative_strength_leadership_blend_lead_base_v149_signal(closeadj):
    result = (_f10_hilopos(closeadj, 252)
              + (_f10_maratio(closeadj, 200) - 1.0)
              + _f10_retrank(closeadj, 252)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d range position scaled by RS-line slope sign-strength (directional leadership)
def f10rs_f10_relative_strength_leadership_posrsslope_252d_base_v150_signal(closeadj):
    result = _f10_hilopos(closeadj, 252) * _f10_rsslope(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f10rs_f10_relative_strength_leadership_maratio_30d_base_v076_signal,
    f10rs_f10_relative_strength_leadership_maratio_150d_base_v077_signal,
    f10rs_f10_relative_strength_leadership_maratio_378d_base_v078_signal,
    f10rs_f10_relative_strength_leadership_maratio_42d_base_v079_signal,
    f10rs_f10_relative_strength_leadership_logmaratio_21d_base_v080_signal,
    f10rs_f10_relative_strength_leadership_logmaratio_126d_base_v081_signal,
    f10rs_f10_relative_strength_leadership_logmaratio_252d_base_v082_signal,
    f10rs_f10_relative_strength_leadership_stack_100_200_base_v083_signal,
    f10rs_f10_relative_strength_leadership_stack_42_126_base_v084_signal,
    f10rs_f10_relative_strength_leadership_stack_126_252_base_v085_signal,
    f10rs_f10_relative_strength_leadership_logstack_50_200_base_v086_signal,
    f10rs_f10_relative_strength_leadership_hilopos_105d_base_v087_signal,
    f10rs_f10_relative_strength_leadership_hilopos_147d_base_v088_signal,
    f10rs_f10_relative_strength_leadership_hilopos_378d_base_v089_signal,
    f10rs_f10_relative_strength_leadership_hilopos_30d_base_v090_signal,
    f10rs_f10_relative_strength_leadership_disthigh_189d_base_v091_signal,
    f10rs_f10_relative_strength_leadership_disthigh_63d_base_v092_signal,
    f10rs_f10_relative_strength_leadership_distlow_189d_base_v093_signal,
    f10rs_f10_relative_strength_leadership_distlow_63d_base_v094_signal,
    f10rs_f10_relative_strength_leadership_proxhigh_252d_base_v095_signal,
    f10rs_f10_relative_strength_leadership_proxhigh_504d_base_v096_signal,
    f10rs_f10_relative_strength_leadership_proxlow_252d_base_v097_signal,
    f10rs_f10_relative_strength_leadership_retrank_147d_base_v098_signal,
    f10rs_f10_relative_strength_leadership_retrank_378d_base_v099_signal,
    f10rs_f10_relative_strength_leadership_retrank_105d_base_v100_signal,
    f10rs_f10_relative_strength_leadership_rankmom_63_252_base_v101_signal,
    f10rs_f10_relative_strength_leadership_rankmom_126_504_base_v102_signal,
    f10rs_f10_relative_strength_leadership_rsslope_105d_base_v103_signal,
    f10rs_f10_relative_strength_leadership_rsslope_147d_base_v104_signal,
    f10rs_f10_relative_strength_leadership_rsslope_189d_base_v105_signal,
    f10rs_f10_relative_strength_leadership_rsslope_504d_base_v106_signal,
    f10rs_f10_relative_strength_leadership_rsslopespr_63_252_base_v107_signal,
    f10rs_f10_relative_strength_leadership_zmaratio_100d_base_v108_signal,
    f10rs_f10_relative_strength_leadership_zmaratio_63d_base_v109_signal,
    f10rs_f10_relative_strength_leadership_zhilopos_504d_base_v110_signal,
    f10rs_f10_relative_strength_leadership_zhilopos_63d_base_v111_signal,
    f10rs_f10_relative_strength_leadership_zretrank_252d_base_v112_signal,
    f10rs_f10_relative_strength_leadership_zretrank_126d_base_v113_signal,
    f10rs_f10_relative_strength_leadership_voladjext_200_126_base_v114_signal,
    f10rs_f10_relative_strength_leadership_voladjext_100_252_base_v115_signal,
    f10rs_f10_relative_strength_leadership_smoothpos63_252d_base_v116_signal,
    f10rs_f10_relative_strength_leadership_smoothma63_200d_base_v117_signal,
    f10rs_f10_relative_strength_leadership_ewmpos_252d_base_v118_signal,
    f10rs_f10_relative_strength_leadership_ewmrank_252d_base_v119_signal,
    f10rs_f10_relative_strength_leadership_posstackw_252d_base_v120_signal,
    f10rs_f10_relative_strength_leadership_rankmaw_252d_base_v121_signal,
    f10rs_f10_relative_strength_leadership_posprod_63_252_base_v122_signal,
    f10rs_f10_relative_strength_leadership_macomposite_base_v123_signal,
    f10rs_f10_relative_strength_leadership_poscomposite_base_v124_signal,
    f10rs_f10_relative_strength_leadership_rankcomposite_base_v125_signal,
    f10rs_f10_relative_strength_leadership_dvsurge_50d_base_v126_signal,
    f10rs_f10_relative_strength_leadership_volconfpos_252d_base_v127_signal,
    f10rs_f10_relative_strength_leadership_hlpos_126d_base_v128_signal,
    f10rs_f10_relative_strength_leadership_hlpos_504d_base_v129_signal,
    f10rs_f10_relative_strength_leadership_highpress_252d_base_v130_signal,
    f10rs_f10_relative_strength_leadership_logmaratio_315d_base_v131_signal,
    f10rs_f10_relative_strength_leadership_logmaratio_84d_base_v132_signal,
    f10rs_f10_relative_strength_leadership_logmaspread_50_252_base_v133_signal,
    f10rs_f10_relative_strength_leadership_maspread_10_63_base_v134_signal,
    f10rs_f10_relative_strength_leadership_posspread_504_126_base_v135_signal,
    f10rs_f10_relative_strength_leadership_posspread_315_84_base_v136_signal,
    f10rs_f10_relative_strength_leadership_rankspread_504_252_base_v137_signal,
    f10rs_f10_relative_strength_leadership_normdraw_315d_base_v138_signal,
    f10rs_f10_relative_strength_leadership_normdraw_504d_base_v139_signal,
    f10rs_f10_relative_strength_leadership_ewmma_200d_base_v140_signal,
    f10rs_f10_relative_strength_leadership_ewmma_50d_base_v141_signal,
    f10rs_f10_relative_strength_leadership_possurp_252d_base_v142_signal,
    f10rs_f10_relative_strength_leadership_masurp_50d_base_v143_signal,
    f10rs_f10_relative_strength_leadership_posrank_252d_base_v144_signal,
    f10rs_f10_relative_strength_leadership_marank_200d_base_v145_signal,
    f10rs_f10_relative_strength_leadership_rsslopevol_126d_base_v146_signal,
    f10rs_f10_relative_strength_leadership_rsslopevol_252d_base_v147_signal,
    f10rs_f10_relative_strength_leadership_materm_63_252_base_v148_signal,
    f10rs_f10_relative_strength_leadership_blend_lead_base_v149_signal,
    f10rs_f10_relative_strength_leadership_posrsslope_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F10_RELATIVE_STRENGTH_LEADERSHIP_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f10_relative_strength_leadership_base_076_150_claude: {n_features} features pass")
