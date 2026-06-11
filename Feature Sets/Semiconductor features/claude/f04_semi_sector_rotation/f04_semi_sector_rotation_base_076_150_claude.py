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
def _f04_log_ret(s, n=1):
    return np.log(s / s.shift(n))


def _f04_rot_spread(semi, spx, n):
    return np.log(semi / semi.shift(n)) - np.log(spx / spx.shift(n))


def _f04_rs_log_ratio(a, b):
    return np.log(a.replace(0, np.nan).abs() / b.replace(0, np.nan).abs())

# 21d tracking error own vs spx
def f04sr_f04_semi_sector_rotation_ownspxte_21d_base_v076_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = _std(o - x, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d tracking error own vs spx
def f04sr_f04_semi_sector_rotation_ownspxte_63d_base_v077_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = _std(o - x, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d tracking error own vs spx
def f04sr_f04_semi_sector_rotation_ownspxte_126d_base_v078_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = _std(o - x, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d tracking error own vs spx
def f04sr_f04_semi_sector_rotation_ownspxte_252d_base_v079_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = _std(o - x, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d tracking error own vs spx
def f04sr_f04_semi_sector_rotation_ownspxte_504d_base_v080_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = _std(o - x, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d tracking error own vs semi-basket
def f04sr_f04_semi_sector_rotation_ownsemite_21d_base_v081_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    b = semi_basket_closeadj.pct_change()
    result = _std(o - b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d tracking error own vs semi-basket
def f04sr_f04_semi_sector_rotation_ownsemite_63d_base_v082_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    b = semi_basket_closeadj.pct_change()
    result = _std(o - b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d tracking error own vs semi-basket
def f04sr_f04_semi_sector_rotation_ownsemite_126d_base_v083_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    b = semi_basket_closeadj.pct_change()
    result = _std(o - b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d tracking error own vs semi-basket
def f04sr_f04_semi_sector_rotation_ownsemite_252d_base_v084_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    b = semi_basket_closeadj.pct_change()
    result = _std(o - b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d tracking error own vs semi-basket
def f04sr_f04_semi_sector_rotation_ownsemite_504d_base_v085_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    b = semi_basket_closeadj.pct_change()
    result = _std(o - b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d information ratio semi vs spx
def f04sr_f04_semi_sector_rotation_semispxir_21d_base_v086_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = s - x
    result = _mean(d, 21) / _std(d, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d information ratio semi vs spx
def f04sr_f04_semi_sector_rotation_semispxir_63d_base_v087_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = s - x
    result = _mean(d, 63) / _std(d, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d information ratio semi vs spx
def f04sr_f04_semi_sector_rotation_semispxir_126d_base_v088_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = s - x
    result = _mean(d, 126) / _std(d, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d information ratio semi vs spx
def f04sr_f04_semi_sector_rotation_semispxir_252d_base_v089_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = s - x
    result = _mean(d, 252) / _std(d, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d information ratio semi vs spx
def f04sr_f04_semi_sector_rotation_semispxir_504d_base_v090_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = s - x
    result = _mean(d, 504) / _std(d, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d information ratio own vs spx
def f04sr_f04_semi_sector_rotation_ownspxir_21d_base_v091_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = o - x
    result = _mean(d, 21) / _std(d, 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d information ratio own vs spx
def f04sr_f04_semi_sector_rotation_ownspxir_63d_base_v092_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = o - x
    result = _mean(d, 63) / _std(d, 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d information ratio own vs spx
def f04sr_f04_semi_sector_rotation_ownspxir_126d_base_v093_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = o - x
    result = _mean(d, 126) / _std(d, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d information ratio own vs spx
def f04sr_f04_semi_sector_rotation_ownspxir_252d_base_v094_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = o - x
    result = _mean(d, 252) / _std(d, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d information ratio own vs spx
def f04sr_f04_semi_sector_rotation_ownspxir_504d_base_v095_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = o - x
    result = _mean(d, 504) / _std(d, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d fraction of days own > semi > spx (in-order rotation)
def f04sr_f04_semi_sector_rotation_tripleorder_21d_base_v096_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    b = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    ok = ((o > b) & (b > x)).astype(float)
    result = ok.rolling(21, min_periods=max(1, 21 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fraction of days own > semi > spx (in-order rotation)
def f04sr_f04_semi_sector_rotation_tripleorder_63d_base_v097_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    b = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    ok = ((o > b) & (b > x)).astype(float)
    result = ok.rolling(63, min_periods=max(1, 63 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d fraction of days own > semi > spx (in-order rotation)
def f04sr_f04_semi_sector_rotation_tripleorder_126d_base_v098_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    b = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    ok = ((o > b) & (b > x)).astype(float)
    result = ok.rolling(126, min_periods=max(1, 126 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fraction of days own > semi > spx (in-order rotation)
def f04sr_f04_semi_sector_rotation_tripleorder_252d_base_v099_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    b = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    ok = ((o > b) & (b > x)).astype(float)
    result = ok.rolling(252, min_periods=max(1, 252 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d fraction of days own > semi > spx (in-order rotation)
def f04sr_f04_semi_sector_rotation_tripleorder_504d_base_v100_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    b = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    ok = ((o > b) & (b > x)).astype(float)
    result = ok.rolling(504, min_periods=max(1, 504 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d own beta to sp500
def f04sr_f04_semi_sector_rotation_ownspxbeta_21d_base_v101_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    cov = o.rolling(21, min_periods=max(2, 21 // 2)).cov(x)
    var = x.rolling(21, min_periods=max(2, 21 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own beta to sp500
def f04sr_f04_semi_sector_rotation_ownspxbeta_63d_base_v102_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    cov = o.rolling(63, min_periods=max(2, 63 // 2)).cov(x)
    var = x.rolling(63, min_periods=max(2, 63 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own beta to sp500
def f04sr_f04_semi_sector_rotation_ownspxbeta_126d_base_v103_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    cov = o.rolling(126, min_periods=max(2, 126 // 2)).cov(x)
    var = x.rolling(126, min_periods=max(2, 126 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own beta to sp500
def f04sr_f04_semi_sector_rotation_ownspxbeta_252d_base_v104_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    cov = o.rolling(252, min_periods=max(2, 252 // 2)).cov(x)
    var = x.rolling(252, min_periods=max(2, 252 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own beta to sp500
def f04sr_f04_semi_sector_rotation_ownspxbeta_504d_base_v105_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    cov = o.rolling(504, min_periods=max(2, 504 // 2)).cov(x)
    var = x.rolling(504, min_periods=max(2, 504 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d semi-basket beta to sp500
def f04sr_f04_semi_sector_rotation_semispxbeta_21d_base_v106_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    cov = s.rolling(21, min_periods=max(2, 21 // 2)).cov(x)
    var = x.rolling(21, min_periods=max(2, 21 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d semi-basket beta to sp500
def f04sr_f04_semi_sector_rotation_semispxbeta_63d_base_v107_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    cov = s.rolling(63, min_periods=max(2, 63 // 2)).cov(x)
    var = x.rolling(63, min_periods=max(2, 63 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d semi-basket beta to sp500
def f04sr_f04_semi_sector_rotation_semispxbeta_126d_base_v108_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    cov = s.rolling(126, min_periods=max(2, 126 // 2)).cov(x)
    var = x.rolling(126, min_periods=max(2, 126 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d semi-basket beta to sp500
def f04sr_f04_semi_sector_rotation_semispxbeta_252d_base_v109_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    cov = s.rolling(252, min_periods=max(2, 252 // 2)).cov(x)
    var = x.rolling(252, min_periods=max(2, 252 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d semi-basket beta to sp500
def f04sr_f04_semi_sector_rotation_semispxbeta_504d_base_v110_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    cov = s.rolling(504, min_periods=max(2, 504 // 2)).cov(x)
    var = x.rolling(504, min_periods=max(2, 504 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d beta spread (own beta - semi beta) to spx
def f04sr_f04_semi_sector_rotation_betaspread_21d_base_v111_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    vx = x.rolling(21, min_periods=max(2, 21 // 2)).var()
    bo = o.rolling(21, min_periods=max(2, 21 // 2)).cov(x) / vx.replace(0, np.nan)
    bs = s.rolling(21, min_periods=max(2, 21 // 2)).cov(x) / vx.replace(0, np.nan)
    result = bo - bs
    return result.replace([np.inf, -np.inf], np.nan)


# 63d beta spread (own beta - semi beta) to spx
def f04sr_f04_semi_sector_rotation_betaspread_63d_base_v112_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    vx = x.rolling(63, min_periods=max(2, 63 // 2)).var()
    bo = o.rolling(63, min_periods=max(2, 63 // 2)).cov(x) / vx.replace(0, np.nan)
    bs = s.rolling(63, min_periods=max(2, 63 // 2)).cov(x) / vx.replace(0, np.nan)
    result = bo - bs
    return result.replace([np.inf, -np.inf], np.nan)


# 126d beta spread (own beta - semi beta) to spx
def f04sr_f04_semi_sector_rotation_betaspread_126d_base_v113_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    vx = x.rolling(126, min_periods=max(2, 126 // 2)).var()
    bo = o.rolling(126, min_periods=max(2, 126 // 2)).cov(x) / vx.replace(0, np.nan)
    bs = s.rolling(126, min_periods=max(2, 126 // 2)).cov(x) / vx.replace(0, np.nan)
    result = bo - bs
    return result.replace([np.inf, -np.inf], np.nan)


# 252d beta spread (own beta - semi beta) to spx
def f04sr_f04_semi_sector_rotation_betaspread_252d_base_v114_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    vx = x.rolling(252, min_periods=max(2, 252 // 2)).var()
    bo = o.rolling(252, min_periods=max(2, 252 // 2)).cov(x) / vx.replace(0, np.nan)
    bs = s.rolling(252, min_periods=max(2, 252 // 2)).cov(x) / vx.replace(0, np.nan)
    result = bo - bs
    return result.replace([np.inf, -np.inf], np.nan)


# 504d beta spread (own beta - semi beta) to spx
def f04sr_f04_semi_sector_rotation_betaspread_504d_base_v115_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    vx = x.rolling(504, min_periods=max(2, 504 // 2)).var()
    bo = o.rolling(504, min_periods=max(2, 504 // 2)).cov(x) / vx.replace(0, np.nan)
    bs = s.rolling(504, min_periods=max(2, 504 // 2)).cov(x) / vx.replace(0, np.nan)
    result = bo - bs
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of cumulative semi-spx spread from peak
def f04sr_f04_semi_sector_rotation_semispxcumdd_21d_base_v116_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    cum = (s - x).rolling(21, min_periods=max(1, 21 // 2)).sum()
    result = cum - _max(cum, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of cumulative semi-spx spread from peak
def f04sr_f04_semi_sector_rotation_semispxcumdd_63d_base_v117_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    cum = (s - x).rolling(63, min_periods=max(1, 63 // 2)).sum()
    result = cum - _max(cum, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of cumulative semi-spx spread from peak
def f04sr_f04_semi_sector_rotation_semispxcumdd_126d_base_v118_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    cum = (s - x).rolling(126, min_periods=max(1, 126 // 2)).sum()
    result = cum - _max(cum, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of cumulative semi-spx spread from peak
def f04sr_f04_semi_sector_rotation_semispxcumdd_252d_base_v119_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    cum = (s - x).rolling(252, min_periods=max(1, 252 // 2)).sum()
    result = cum - _max(cum, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of cumulative semi-spx spread from peak
def f04sr_f04_semi_sector_rotation_semispxcumdd_504d_base_v120_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    cum = (s - x).rolling(504, min_periods=max(1, 504 // 2)).sum()
    result = cum - _max(cum, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of own-spx return spread
def f04sr_f04_semi_sector_rotation_ownspxskew_21d_base_v121_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (o - x).rolling(21, min_periods=max(2, 21 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of own-spx return spread
def f04sr_f04_semi_sector_rotation_ownspxskew_63d_base_v122_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (o - x).rolling(63, min_periods=max(2, 63 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of own-spx return spread
def f04sr_f04_semi_sector_rotation_ownspxskew_126d_base_v123_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (o - x).rolling(126, min_periods=max(2, 126 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of own-spx return spread
def f04sr_f04_semi_sector_rotation_ownspxskew_252d_base_v124_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (o - x).rolling(252, min_periods=max(2, 252 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of own-spx return spread
def f04sr_f04_semi_sector_rotation_ownspxskew_504d_base_v125_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (o - x).rolling(504, min_periods=max(2, 504 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of own-semi return spread
def f04sr_f04_semi_sector_rotation_ownsemiskew_21d_base_v126_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    b = semi_basket_closeadj.pct_change()
    result = (o - b).rolling(21, min_periods=max(2, 21 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of own-semi return spread
def f04sr_f04_semi_sector_rotation_ownsemiskew_63d_base_v127_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    b = semi_basket_closeadj.pct_change()
    result = (o - b).rolling(63, min_periods=max(2, 63 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of own-semi return spread
def f04sr_f04_semi_sector_rotation_ownsemiskew_126d_base_v128_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    b = semi_basket_closeadj.pct_change()
    result = (o - b).rolling(126, min_periods=max(2, 126 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of own-semi return spread
def f04sr_f04_semi_sector_rotation_ownsemiskew_252d_base_v129_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    b = semi_basket_closeadj.pct_change()
    result = (o - b).rolling(252, min_periods=max(2, 252 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of own-semi return spread
def f04sr_f04_semi_sector_rotation_ownsemiskew_504d_base_v130_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    b = semi_basket_closeadj.pct_change()
    result = (o - b).rolling(504, min_periods=max(2, 504 // 2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of own-spx spread
def f04sr_f04_semi_sector_rotation_ownspxkurt_21d_base_v131_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (o - x).rolling(21, min_periods=max(2, 21 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of own-spx spread
def f04sr_f04_semi_sector_rotation_ownspxkurt_63d_base_v132_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (o - x).rolling(63, min_periods=max(2, 63 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of own-spx spread
def f04sr_f04_semi_sector_rotation_ownspxkurt_126d_base_v133_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (o - x).rolling(126, min_periods=max(2, 126 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of own-spx spread
def f04sr_f04_semi_sector_rotation_ownspxkurt_252d_base_v134_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (o - x).rolling(252, min_periods=max(2, 252 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of own-spx spread
def f04sr_f04_semi_sector_rotation_ownspxkurt_504d_base_v135_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    o = closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    result = (o - x).rolling(504, min_periods=max(2, 504 // 2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rotation (semi-spx) on spx-up days
def f04sr_f04_semi_sector_rotation_semispxcondup_21d_base_v136_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = (s - x).where(x > 0)
    result = _mean(d, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rotation (semi-spx) on spx-up days
def f04sr_f04_semi_sector_rotation_semispxcondup_63d_base_v137_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = (s - x).where(x > 0)
    result = _mean(d, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rotation (semi-spx) on spx-up days
def f04sr_f04_semi_sector_rotation_semispxcondup_126d_base_v138_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = (s - x).where(x > 0)
    result = _mean(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rotation (semi-spx) on spx-up days
def f04sr_f04_semi_sector_rotation_semispxcondup_252d_base_v139_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = (s - x).where(x > 0)
    result = _mean(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rotation (semi-spx) on spx-up days
def f04sr_f04_semi_sector_rotation_semispxcondup_504d_base_v140_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = (s - x).where(x > 0)
    result = _mean(d, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rotation (semi-spx) on spx-down days
def f04sr_f04_semi_sector_rotation_semispxconddn_21d_base_v141_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = (s - x).where(x < 0)
    result = _mean(d, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rotation (semi-spx) on spx-down days
def f04sr_f04_semi_sector_rotation_semispxconddn_63d_base_v142_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = (s - x).where(x < 0)
    result = _mean(d, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rotation (semi-spx) on spx-down days
def f04sr_f04_semi_sector_rotation_semispxconddn_126d_base_v143_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = (s - x).where(x < 0)
    result = _mean(d, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rotation (semi-spx) on spx-down days
def f04sr_f04_semi_sector_rotation_semispxconddn_252d_base_v144_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = (s - x).where(x < 0)
    result = _mean(d, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rotation (semi-spx) on spx-down days
def f04sr_f04_semi_sector_rotation_semispxconddn_504d_base_v145_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = (s - x).where(x < 0)
    result = _mean(d, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# short composite: 21z + 63z + 126z of semi-spx log-ratio
def f04sr_f04_semi_sector_rotation_rotcomposite_short_base_v146_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(semi_basket_closeadj, sp500_closeadj)
    result = _z(r, 21) + _z(r, 63) + _z(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# long composite: 63z + 126z + 252z of semi-spx log-ratio
def f04sr_f04_semi_sector_rotation_rotcomposite_long_base_v147_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(semi_basket_closeadj, sp500_closeadj)
    result = _z(r, 63) + _z(r, 126) + _z(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# rotation regime divergence: sign short EMA cross - sign long EMA cross
def f04sr_f04_semi_sector_rotation_rotregime_divergence_base_v148_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    r = _f04_rs_log_ratio(semi_basket_closeadj, sp500_closeadj)
    short = np.sign(r.ewm(span=21, adjust=False).mean() - r.ewm(span=63, adjust=False).mean())
    long = np.sign(r.ewm(span=126, adjust=False).mean() - r.ewm(span=252, adjust=False).mean())
    result = pd.Series(short - long, index=r.index)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rotation quality: IR x hit ratio (semi vs spx)
def f04sr_f04_semi_sector_rotation_rotquality_63d_base_v149_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = s - x
    ir = _mean(d, 63) / _std(d, 63).replace(0, np.nan)
    hit = (d > 0).astype(float).rolling(63, min_periods=32).mean()
    result = ir * hit
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rotation quality: IR x hit ratio (semi vs spx)
def f04sr_f04_semi_sector_rotation_rotquality_252d_base_v150_signal(closeadj, semi_basket_closeadj, sp500_closeadj):
    s = semi_basket_closeadj.pct_change()
    x = sp500_closeadj.pct_change()
    d = s - x
    ir = _mean(d, 252) / _std(d, 252).replace(0, np.nan)
    hit = (d > 0).astype(float).rolling(252, min_periods=126).mean()
    result = ir * hit
    return result.replace([np.inf, -np.inf], np.nan)


