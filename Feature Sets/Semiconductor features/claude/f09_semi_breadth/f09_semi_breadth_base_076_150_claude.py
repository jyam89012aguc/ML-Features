import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f09_brd_diff(brd, n):
    return brd - brd.shift(n)


def _f09_brd_dev(brd, w):
    return brd - brd.rolling(w, min_periods=max(1, w // 2)).mean()


def _f09_brd_thrust(brd, threshold=0.5):
    return (brd > threshold).astype(float)


def _f09_brd_above_ma(brd, w):
    return (brd > brd.rolling(w, min_periods=max(1, w // 2)).mean()).astype(float)


# 21d own avg return on breadth-strong days
def f09br_f09_semi_breadth_ownretbrdup_21d_base_v076_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth > 0.5
    result = _mean(own.where(mask), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own avg return on breadth-strong days
def f09br_f09_semi_breadth_ownretbrdup_63d_base_v077_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth > 0.5
    result = _mean(own.where(mask), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own avg return on breadth-strong days
def f09br_f09_semi_breadth_ownretbrdup_126d_base_v078_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth > 0.5
    result = _mean(own.where(mask), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own avg return on breadth-strong days
def f09br_f09_semi_breadth_ownretbrdup_252d_base_v079_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth > 0.5
    result = _mean(own.where(mask), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own avg return on breadth-strong days
def f09br_f09_semi_breadth_ownretbrdup_504d_base_v080_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth > 0.5
    result = _mean(own.where(mask), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d own avg return on breadth-weak days
def f09br_f09_semi_breadth_ownretbrddn_21d_base_v081_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth < 0.5
    result = _mean(own.where(mask), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own avg return on breadth-weak days
def f09br_f09_semi_breadth_ownretbrddn_63d_base_v082_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth < 0.5
    result = _mean(own.where(mask), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own avg return on breadth-weak days
def f09br_f09_semi_breadth_ownretbrddn_126d_base_v083_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth < 0.5
    result = _mean(own.where(mask), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own avg return on breadth-weak days
def f09br_f09_semi_breadth_ownretbrddn_252d_base_v084_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth < 0.5
    result = _mean(own.where(mask), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own avg return on breadth-weak days
def f09br_f09_semi_breadth_ownretbrddn_504d_base_v085_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth < 0.5
    result = _mean(own.where(mask), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d divergence between basket return and breadth direction
def f09br_f09_semi_breadth_brdbasdiv_21d_base_v086_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    bret = semi_basket_closeadj.pct_change().rolling(21, min_periods=max(1, 21 // 2)).sum()
    bz = _z(semi_basket_breadth, 21)
    result = pd.Series(np.sign(bret) - np.sign(bz), index=bret.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d divergence between basket return and breadth direction
def f09br_f09_semi_breadth_brdbasdiv_63d_base_v087_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    bret = semi_basket_closeadj.pct_change().rolling(63, min_periods=max(1, 63 // 2)).sum()
    bz = _z(semi_basket_breadth, 63)
    result = pd.Series(np.sign(bret) - np.sign(bz), index=bret.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d divergence between basket return and breadth direction
def f09br_f09_semi_breadth_brdbasdiv_126d_base_v088_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    bret = semi_basket_closeadj.pct_change().rolling(126, min_periods=max(1, 126 // 2)).sum()
    bz = _z(semi_basket_breadth, 126)
    result = pd.Series(np.sign(bret) - np.sign(bz), index=bret.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d divergence between basket return and breadth direction
def f09br_f09_semi_breadth_brdbasdiv_252d_base_v089_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    bret = semi_basket_closeadj.pct_change().rolling(252, min_periods=max(1, 252 // 2)).sum()
    bz = _z(semi_basket_breadth, 252)
    result = pd.Series(np.sign(bret) - np.sign(bz), index=bret.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d divergence between basket return and breadth direction
def f09br_f09_semi_breadth_brdbasdiv_504d_base_v090_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    bret = semi_basket_closeadj.pct_change().rolling(504, min_periods=max(1, 504 // 2)).sum()
    bz = _z(semi_basket_breadth, 504)
    result = pd.Series(np.sign(bret) - np.sign(bz), index=bret.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of breadth
def f09br_f09_semi_breadth_brdskew_21d_base_v091_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth.rolling(21, min_periods=11).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of breadth
def f09br_f09_semi_breadth_brdskew_63d_base_v092_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth.rolling(63, min_periods=32).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of breadth
def f09br_f09_semi_breadth_brdskew_126d_base_v093_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth.rolling(126, min_periods=63).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of breadth
def f09br_f09_semi_breadth_brdskew_252d_base_v094_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth.rolling(252, min_periods=126).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of breadth
def f09br_f09_semi_breadth_brdskew_504d_base_v095_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth.rolling(504, min_periods=252).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of breadth
def f09br_f09_semi_breadth_brdkurt_21d_base_v096_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth.rolling(21, min_periods=11).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of breadth
def f09br_f09_semi_breadth_brdkurt_63d_base_v097_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth.rolling(63, min_periods=32).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of breadth
def f09br_f09_semi_breadth_brdkurt_126d_base_v098_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth.rolling(126, min_periods=63).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of breadth
def f09br_f09_semi_breadth_brdkurt_252d_base_v099_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth.rolling(252, min_periods=126).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of breadth
def f09br_f09_semi_breadth_brdkurt_504d_base_v100_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth.rolling(504, min_periods=252).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of breadth-advancing days
def f09br_f09_semi_breadth_brdadv_21d_base_v101_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth.diff() > 0).astype(float).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of breadth-advancing days
def f09br_f09_semi_breadth_brdadv_63d_base_v102_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth.diff() > 0).astype(float).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of breadth-advancing days
def f09br_f09_semi_breadth_brdadv_126d_base_v103_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth.diff() > 0).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of breadth-advancing days
def f09br_f09_semi_breadth_brdadv_252d_base_v104_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth.diff() > 0).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of breadth-advancing days
def f09br_f09_semi_breadth_brdadv_504d_base_v105_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth.diff() > 0).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d count of breadth-declining days
def f09br_f09_semi_breadth_brddec_21d_base_v106_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth.diff() < 0).astype(float).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of breadth-declining days
def f09br_f09_semi_breadth_brddec_63d_base_v107_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth.diff() < 0).astype(float).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d count of breadth-declining days
def f09br_f09_semi_breadth_brddec_126d_base_v108_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth.diff() < 0).astype(float).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of breadth-declining days
def f09br_f09_semi_breadth_brddec_252d_base_v109_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth.diff() < 0).astype(float).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of breadth-declining days
def f09br_f09_semi_breadth_brddec_504d_base_v110_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth.diff() < 0).astype(float).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d advance-decline ratio of breadth
def f09br_f09_semi_breadth_brdadratio_21d_base_v111_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    adv = (semi_basket_breadth.diff() > 0).astype(float).rolling(21, min_periods=11).sum()
    dec = (semi_basket_breadth.diff() < 0).astype(float).rolling(21, min_periods=11).sum()
    result = adv / (adv + dec).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d advance-decline ratio of breadth
def f09br_f09_semi_breadth_brdadratio_63d_base_v112_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    adv = (semi_basket_breadth.diff() > 0).astype(float).rolling(63, min_periods=32).sum()
    dec = (semi_basket_breadth.diff() < 0).astype(float).rolling(63, min_periods=32).sum()
    result = adv / (adv + dec).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d advance-decline ratio of breadth
def f09br_f09_semi_breadth_brdadratio_126d_base_v113_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    adv = (semi_basket_breadth.diff() > 0).astype(float).rolling(126, min_periods=63).sum()
    dec = (semi_basket_breadth.diff() < 0).astype(float).rolling(126, min_periods=63).sum()
    result = adv / (adv + dec).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d advance-decline ratio of breadth
def f09br_f09_semi_breadth_brdadratio_252d_base_v114_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    adv = (semi_basket_breadth.diff() > 0).astype(float).rolling(252, min_periods=126).sum()
    dec = (semi_basket_breadth.diff() < 0).astype(float).rolling(252, min_periods=126).sum()
    result = adv / (adv + dec).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d advance-decline ratio of breadth
def f09br_f09_semi_breadth_brdadratio_504d_base_v115_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    adv = (semi_basket_breadth.diff() > 0).astype(float).rolling(504, min_periods=252).sum()
    dec = (semi_basket_breadth.diff() < 0).astype(float).rolling(504, min_periods=252).sum()
    result = adv / (adv + dec).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rate of change of breadth
def f09br_f09_semi_breadth_brdroc_21d_base_v116_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth - semi_basket_breadth.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rate of change of breadth
def f09br_f09_semi_breadth_brdroc_63d_base_v117_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth - semi_basket_breadth.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rate of change of breadth
def f09br_f09_semi_breadth_brdroc_126d_base_v118_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth - semi_basket_breadth.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rate of change of breadth
def f09br_f09_semi_breadth_brdroc_252d_base_v119_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth - semi_basket_breadth.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rate of change of breadth
def f09br_f09_semi_breadth_brdroc_504d_base_v120_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = semi_basket_breadth - semi_basket_breadth.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cumulative breadth-vs-neutral excess
def f09br_f09_semi_breadth_brdcumexcess_21d_base_v121_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth - 0.5).rolling(21, min_periods=11).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative breadth-vs-neutral excess
def f09br_f09_semi_breadth_brdcumexcess_63d_base_v122_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth - 0.5).rolling(63, min_periods=32).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cumulative breadth-vs-neutral excess
def f09br_f09_semi_breadth_brdcumexcess_126d_base_v123_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth - 0.5).rolling(126, min_periods=63).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative breadth-vs-neutral excess
def f09br_f09_semi_breadth_brdcumexcess_252d_base_v124_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth - 0.5).rolling(252, min_periods=126).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative breadth-vs-neutral excess
def f09br_f09_semi_breadth_brdcumexcess_504d_base_v125_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = (semi_basket_breadth - 0.5).rolling(504, min_periods=252).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d correlation of breadth with basket return
def f09br_f09_semi_breadth_brdcorrbret_21d_base_v126_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    bret = semi_basket_closeadj.pct_change()
    result = semi_basket_breadth.rolling(21, min_periods=10).corr(bret)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d correlation of breadth with basket return
def f09br_f09_semi_breadth_brdcorrbret_63d_base_v127_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    bret = semi_basket_closeadj.pct_change()
    result = semi_basket_breadth.rolling(63, min_periods=31).corr(bret)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d correlation of breadth with basket return
def f09br_f09_semi_breadth_brdcorrbret_126d_base_v128_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    bret = semi_basket_closeadj.pct_change()
    result = semi_basket_breadth.rolling(126, min_periods=63).corr(bret)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d correlation of breadth with basket return
def f09br_f09_semi_breadth_brdcorrbret_252d_base_v129_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    bret = semi_basket_closeadj.pct_change()
    result = semi_basket_breadth.rolling(252, min_periods=126).corr(bret)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d correlation of breadth with basket return
def f09br_f09_semi_breadth_brdcorrbret_504d_base_v130_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    bret = semi_basket_closeadj.pct_change()
    result = semi_basket_breadth.rolling(504, min_periods=252).corr(bret)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d own return z-score on high-breadth days
def f09br_f09_semi_breadth_ownzbrdhi_21d_base_v131_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth > _mean(semi_basket_breadth, 21)
    result = _z(own.where(mask), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own return z-score on high-breadth days
def f09br_f09_semi_breadth_ownzbrdhi_63d_base_v132_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth > _mean(semi_basket_breadth, 63)
    result = _z(own.where(mask), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own return z-score on high-breadth days
def f09br_f09_semi_breadth_ownzbrdhi_126d_base_v133_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth > _mean(semi_basket_breadth, 126)
    result = _z(own.where(mask), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own return z-score on high-breadth days
def f09br_f09_semi_breadth_ownzbrdhi_252d_base_v134_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth > _mean(semi_basket_breadth, 252)
    result = _z(own.where(mask), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own return z-score on high-breadth days
def f09br_f09_semi_breadth_ownzbrdhi_504d_base_v135_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth > _mean(semi_basket_breadth, 504)
    result = _z(own.where(mask), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d own return z-score on low-breadth days
def f09br_f09_semi_breadth_ownzbrdlo_21d_base_v136_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth < _mean(semi_basket_breadth, 21)
    result = _z(own.where(mask), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own return z-score on low-breadth days
def f09br_f09_semi_breadth_ownzbrdlo_63d_base_v137_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth < _mean(semi_basket_breadth, 63)
    result = _z(own.where(mask), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own return z-score on low-breadth days
def f09br_f09_semi_breadth_ownzbrdlo_126d_base_v138_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth < _mean(semi_basket_breadth, 126)
    result = _z(own.where(mask), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own return z-score on low-breadth days
def f09br_f09_semi_breadth_ownzbrdlo_252d_base_v139_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth < _mean(semi_basket_breadth, 252)
    result = _z(own.where(mask), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own return z-score on low-breadth days
def f09br_f09_semi_breadth_ownzbrdlo_504d_base_v140_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    own = closeadj.pct_change()
    mask = semi_basket_breadth < _mean(semi_basket_breadth, 504)
    result = _z(own.where(mask), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# breadth composite: 21d z + 63d z + 126d z
def f09br_f09_semi_breadth_brdcompshort_63d_base_v141_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _z(semi_basket_breadth, 21) + _z(semi_basket_breadth, 63) + _z(semi_basket_breadth, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# breadth composite: 63d z + 126d z + 252d z
def f09br_f09_semi_breadth_brdcomplong_252d_base_v142_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    result = _z(semi_basket_breadth, 63) + _z(semi_basket_breadth, 126) + _z(semi_basket_breadth, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# breadth regime divergence (short EMA cross vs long EMA cross sign)
def f09br_f09_semi_breadth_brdregdiv_63d_base_v143_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    short = np.sign(semi_basket_breadth.ewm(span=21, adjust=False).mean() - semi_basket_breadth.ewm(span=63, adjust=False).mean())
    long = np.sign(semi_basket_breadth.ewm(span=126, adjust=False).mean() - semi_basket_breadth.ewm(span=252, adjust=False).mean())
    result = pd.Series(short - long, index=semi_basket_breadth.index)
    return result.replace([np.inf, -np.inf], np.nan)


# breadth quality: 63d thrust frac x own 63d return
def f09br_f09_semi_breadth_brdquality63_63d_base_v144_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    thrust = (semi_basket_breadth > 0.5).astype(float).rolling(63, min_periods=32).mean()
    oret = closeadj.pct_change().rolling(63, min_periods=32).sum()
    result = thrust * oret
    return result.replace([np.inf, -np.inf], np.nan)


# breadth quality: 252d thrust frac x own 252d return
def f09br_f09_semi_breadth_brdquality252_252d_base_v145_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    thrust = (semi_basket_breadth > 0.5).astype(float).rolling(252, min_periods=126).mean()
    oret = closeadj.pct_change().rolling(252, min_periods=126).sum()
    result = thrust * oret
    return result.replace([np.inf, -np.inf], np.nan)


# 21d relative strength of breadth-z vs basket-return-z
def f09br_f09_semi_breadth_brdrsbret_21d_base_v146_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    bz = _z(semi_basket_breadth, 21)
    brz = _z(semi_basket_closeadj.pct_change(), 21)
    result = bz - brz
    return result.replace([np.inf, -np.inf], np.nan)


# 63d relative strength of breadth-z vs basket-return-z
def f09br_f09_semi_breadth_brdrsbret_63d_base_v147_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    bz = _z(semi_basket_breadth, 63)
    brz = _z(semi_basket_closeadj.pct_change(), 63)
    result = bz - brz
    return result.replace([np.inf, -np.inf], np.nan)


# 126d relative strength of breadth-z vs basket-return-z
def f09br_f09_semi_breadth_brdrsbret_126d_base_v148_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    bz = _z(semi_basket_breadth, 126)
    brz = _z(semi_basket_closeadj.pct_change(), 126)
    result = bz - brz
    return result.replace([np.inf, -np.inf], np.nan)


# 252d relative strength of breadth-z vs basket-return-z
def f09br_f09_semi_breadth_brdrsbret_252d_base_v149_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    bz = _z(semi_basket_breadth, 252)
    brz = _z(semi_basket_closeadj.pct_change(), 252)
    result = bz - brz
    return result.replace([np.inf, -np.inf], np.nan)


# 504d relative strength of breadth-z vs basket-return-z
def f09br_f09_semi_breadth_brdrsbret_504d_base_v150_signal(closeadj, semi_basket_breadth, semi_basket_closeadj):
    bz = _z(semi_basket_breadth, 504)
    brz = _z(semi_basket_closeadj.pct_change(), 504)
    result = bz - brz
    return result.replace([np.inf, -np.inf], np.nan)
