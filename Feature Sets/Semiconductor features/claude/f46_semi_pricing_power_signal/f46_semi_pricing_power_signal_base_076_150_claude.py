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
def _f46pp_gm_daily(gp, revenue, closeadj):
    g = gp / revenue.replace(0, np.nan)
    return g.reindex(closeadj.index).ffill()


def _f46pp_basket_gm_daily(semi_basket_gm, closeadj):
    return semi_basket_gm.reindex(closeadj.index).ffill()


def _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj):
    own = _f46pp_gm_daily(gp, revenue, closeadj)
    bas = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    return own - bas


# 21d outperformance streak (rolling sum of sign of own minus basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmoutstr_21d_base_v076_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    d = (g - g.shift(21)) - (b - b.shift(21))
    result = pd.Series(np.sign(d), index=d.index).rolling(21, min_periods=max(2, 21 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d outperformance streak (rolling sum of sign of own minus basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmoutstr_63d_base_v077_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    d = (g - g.shift(63)) - (b - b.shift(63))
    result = pd.Series(np.sign(d), index=d.index).rolling(63, min_periods=max(2, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d outperformance streak (rolling sum of sign of own minus basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmoutstr_126d_base_v078_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    d = (g - g.shift(126)) - (b - b.shift(126))
    result = pd.Series(np.sign(d), index=d.index).rolling(126, min_periods=max(2, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d outperformance streak (rolling sum of sign of own minus basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmoutstr_252d_base_v079_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    d = (g - g.shift(252)) - (b - b.shift(252))
    result = pd.Series(np.sign(d), index=d.index).rolling(252, min_periods=max(2, 252 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d outperformance streak (rolling sum of sign of own minus basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmoutstr_504d_base_v080_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    d = (g - g.shift(504)) - (b - b.shift(504))
    result = pd.Series(np.sign(d), index=d.index).rolling(504, min_periods=max(2, 504 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d drawdown of own gm from rolling peak
def f46pp_f46_semi_pricing_power_signal_gmdd_21d_base_v081_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - _max(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d drawdown of own gm from rolling peak
def f46pp_f46_semi_pricing_power_signal_gmdd_63d_base_v082_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - _max(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d drawdown of own gm from rolling peak
def f46pp_f46_semi_pricing_power_signal_gmdd_126d_base_v083_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - _max(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d drawdown of own gm from rolling peak
def f46pp_f46_semi_pricing_power_signal_gmdd_252d_base_v084_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - _max(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d drawdown of own gm from rolling peak
def f46pp_f46_semi_pricing_power_signal_gmdd_504d_base_v085_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - _max(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of own gm above rolling trough
def f46pp_f46_semi_pricing_power_signal_gmru_21d_base_v086_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - _min(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of own gm above rolling trough
def f46pp_f46_semi_pricing_power_signal_gmru_63d_base_v087_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - _min(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of own gm above rolling trough
def f46pp_f46_semi_pricing_power_signal_gmru_126d_base_v088_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - _min(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of own gm above rolling trough
def f46pp_f46_semi_pricing_power_signal_gmru_252d_base_v089_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - _min(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of own gm above rolling trough
def f46pp_f46_semi_pricing_power_signal_gmru_504d_base_v090_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - _min(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d own gm position in rolling range
def f46pp_f46_semi_pricing_power_signal_gmpos_21d_base_v091_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    lo = _min(g, 21)
    hi = _max(g, 21)
    result = (g - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own gm position in rolling range
def f46pp_f46_semi_pricing_power_signal_gmpos_63d_base_v092_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    lo = _min(g, 63)
    hi = _max(g, 63)
    result = (g - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own gm position in rolling range
def f46pp_f46_semi_pricing_power_signal_gmpos_126d_base_v093_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    lo = _min(g, 126)
    hi = _max(g, 126)
    result = (g - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own gm position in rolling range
def f46pp_f46_semi_pricing_power_signal_gmpos_252d_base_v094_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    lo = _min(g, 252)
    hi = _max(g, 252)
    result = (g - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own gm position in rolling range
def f46pp_f46_semi_pricing_power_signal_gmpos_504d_base_v095_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    lo = _min(g, 504)
    hi = _max(g, 504)
    result = (g - lo) / (hi - lo).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d std of own gm change
def f46pp_f46_semi_pricing_power_signal_gmvol_21d_base_v096_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = _std(g - g.shift(21), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of own gm change
def f46pp_f46_semi_pricing_power_signal_gmvol_63d_base_v097_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = _std(g - g.shift(63), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d std of own gm change
def f46pp_f46_semi_pricing_power_signal_gmvol_126d_base_v098_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = _std(g - g.shift(126), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of own gm change
def f46pp_f46_semi_pricing_power_signal_gmvol_252d_base_v099_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = _std(g - g.shift(252), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d std of own gm change
def f46pp_f46_semi_pricing_power_signal_gmvol_504d_base_v100_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = _std(g - g.shift(504), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ratio own gm change std to basket gm change std
def f46pp_f46_semi_pricing_power_signal_gmvolr_21d_base_v101_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    result = _std(g - g.shift(21), 21) / _std(b - b.shift(21), 21).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ratio own gm change std to basket gm change std
def f46pp_f46_semi_pricing_power_signal_gmvolr_63d_base_v102_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    result = _std(g - g.shift(63), 63) / _std(b - b.shift(63), 63).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ratio own gm change std to basket gm change std
def f46pp_f46_semi_pricing_power_signal_gmvolr_126d_base_v103_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    result = _std(g - g.shift(126), 126) / _std(b - b.shift(126), 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio own gm change std to basket gm change std
def f46pp_f46_semi_pricing_power_signal_gmvolr_252d_base_v104_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    result = _std(g - g.shift(252), 252) / _std(b - b.shift(252), 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ratio own gm change std to basket gm change std
def f46pp_f46_semi_pricing_power_signal_gmvolr_504d_base_v105_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    result = _std(g - g.shift(504), 504) / _std(b - b.shift(504), 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema crossover of own gm (short=max(2,W/4) vs long=W)
def f46pp_f46_semi_pricing_power_signal_gmema_21d_base_v106_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    short = max(2, 21 // 4)
    result = g.ewm(span=short, adjust=False).mean() - g.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema crossover of own gm (short=max(2,W/4) vs long=W)
def f46pp_f46_semi_pricing_power_signal_gmema_63d_base_v107_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    short = max(2, 63 // 4)
    result = g.ewm(span=short, adjust=False).mean() - g.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema crossover of own gm (short=max(2,W/4) vs long=W)
def f46pp_f46_semi_pricing_power_signal_gmema_126d_base_v108_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    short = max(2, 126 // 4)
    result = g.ewm(span=short, adjust=False).mean() - g.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema crossover of own gm (short=max(2,W/4) vs long=W)
def f46pp_f46_semi_pricing_power_signal_gmema_252d_base_v109_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    short = max(2, 252 // 4)
    result = g.ewm(span=short, adjust=False).mean() - g.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema crossover of own gm (short=max(2,W/4) vs long=W)
def f46pp_f46_semi_pricing_power_signal_gmema_504d_base_v110_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    short = max(2, 504 // 4)
    result = g.ewm(span=short, adjust=False).mean() - g.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema crossover of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmspema_21d_base_v111_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    short = max(2, 21 // 4)
    result = s.ewm(span=short, adjust=False).mean() - s.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema crossover of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmspema_63d_base_v112_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    short = max(2, 63 // 4)
    result = s.ewm(span=short, adjust=False).mean() - s.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema crossover of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmspema_126d_base_v113_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    short = max(2, 126 // 4)
    result = s.ewm(span=short, adjust=False).mean() - s.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema crossover of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmspema_252d_base_v114_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    short = max(2, 252 // 4)
    result = s.ewm(span=short, adjust=False).mean() - s.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema crossover of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmspema_504d_base_v115_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    short = max(2, 504 // 4)
    result = s.ewm(span=short, adjust=False).mean() - s.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration of own gm (second diff over 21d)
def f46pp_f46_semi_pricing_power_signal_gmacc_21d_base_v116_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(21)
    result = dg - dg.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of own gm (second diff over 63d)
def f46pp_f46_semi_pricing_power_signal_gmacc_63d_base_v117_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(63)
    result = dg - dg.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d acceleration of own gm (second diff over 126d)
def f46pp_f46_semi_pricing_power_signal_gmacc_126d_base_v118_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(126)
    result = dg - dg.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of own gm (second diff over 252d)
def f46pp_f46_semi_pricing_power_signal_gmacc_252d_base_v119_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(252)
    result = dg - dg.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d acceleration of own gm (second diff over 504d)
def f46pp_f46_semi_pricing_power_signal_gmacc_504d_base_v120_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(504)
    result = dg - dg.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration of basket gm (second diff over 21d)
def f46pp_f46_semi_pricing_power_signal_bgmacc_21d_base_v121_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    db = b - b.shift(21)
    result = db - db.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of basket gm (second diff over 63d)
def f46pp_f46_semi_pricing_power_signal_bgmacc_63d_base_v122_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    db = b - b.shift(63)
    result = db - db.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d acceleration of basket gm (second diff over 126d)
def f46pp_f46_semi_pricing_power_signal_bgmacc_126d_base_v123_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    db = b - b.shift(126)
    result = db - db.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of basket gm (second diff over 252d)
def f46pp_f46_semi_pricing_power_signal_bgmacc_252d_base_v124_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    db = b - b.shift(252)
    result = db - db.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d acceleration of basket gm (second diff over 504d)
def f46pp_f46_semi_pricing_power_signal_bgmacc_504d_base_v125_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    db = b - b.shift(504)
    result = db - db.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration of gm spread own vs basket (second diff over 21d)
def f46pp_f46_semi_pricing_power_signal_gmspracc_21d_base_v126_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    ds = s - s.shift(21)
    result = ds - ds.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of gm spread own vs basket (second diff over 63d)
def f46pp_f46_semi_pricing_power_signal_gmspracc_63d_base_v127_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    ds = s - s.shift(63)
    result = ds - ds.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d acceleration of gm spread own vs basket (second diff over 126d)
def f46pp_f46_semi_pricing_power_signal_gmspracc_126d_base_v128_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    ds = s - s.shift(126)
    result = ds - ds.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of gm spread own vs basket (second diff over 252d)
def f46pp_f46_semi_pricing_power_signal_gmspracc_252d_base_v129_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    ds = s - s.shift(252)
    result = ds - ds.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d acceleration of gm spread own vs basket (second diff over 504d)
def f46pp_f46_semi_pricing_power_signal_gmspracc_504d_base_v130_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    ds = s - s.shift(504)
    result = ds - ds.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite strength: z(spread) + z(own gm) + z(Wd own gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp1_21d_base_v131_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    cg = g - g.shift(21)
    result = _z(s, 21) + _z(g, 21) + _z(cg, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite strength: z(spread) + z(own gm) + z(Wd own gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp1_63d_base_v132_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    cg = g - g.shift(63)
    result = _z(s, 63) + _z(g, 63) + _z(cg, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d composite strength: z(spread) + z(own gm) + z(Wd own gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp1_126d_base_v133_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    cg = g - g.shift(126)
    result = _z(s, 126) + _z(g, 126) + _z(cg, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite strength: z(spread) + z(own gm) + z(Wd own gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp1_252d_base_v134_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    cg = g - g.shift(252)
    result = _z(s, 252) + _z(g, 252) + _z(cg, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite strength: z(spread) + z(own gm) + z(Wd own gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp1_504d_base_v135_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    cg = g - g.shift(504)
    result = _z(s, 504) + _z(g, 504) + _z(cg, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite pricing power: z(spread) minus z(corr own/basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp2_21d_base_v136_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(21)
    db = b - b.shift(21)
    c = dg.rolling(21, min_periods=max(2, 21 // 2)).corr(db)
    result = _z(s, 21) - _z(c, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite pricing power: z(spread) minus z(corr own/basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp2_63d_base_v137_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(63)
    db = b - b.shift(63)
    c = dg.rolling(63, min_periods=max(2, 63 // 2)).corr(db)
    result = _z(s, 63) - _z(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d composite pricing power: z(spread) minus z(corr own/basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp2_126d_base_v138_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(126)
    db = b - b.shift(126)
    c = dg.rolling(126, min_periods=max(2, 126 // 2)).corr(db)
    result = _z(s, 126) - _z(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite pricing power: z(spread) minus z(corr own/basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp2_252d_base_v139_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(252)
    db = b - b.shift(252)
    c = dg.rolling(252, min_periods=max(2, 252 // 2)).corr(db)
    result = _z(s, 252) - _z(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite pricing power: z(spread) minus z(corr own/basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp2_504d_base_v140_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(504)
    db = b - b.shift(504)
    c = dg.rolling(504, min_periods=max(2, 504 // 2)).corr(db)
    result = _z(s, 504) - _z(c, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite expansion: z(own gm) + z(spread) - z(basket gm)
def f46pp_f46_semi_pricing_power_signal_gmcomp3_21d_base_v141_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    result = _z(g, 21) + _z(s, 21) - _z(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite expansion: z(own gm) + z(spread) - z(basket gm)
def f46pp_f46_semi_pricing_power_signal_gmcomp3_63d_base_v142_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    result = _z(g, 63) + _z(s, 63) - _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d composite expansion: z(own gm) + z(spread) - z(basket gm)
def f46pp_f46_semi_pricing_power_signal_gmcomp3_126d_base_v143_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    result = _z(g, 126) + _z(s, 126) - _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite expansion: z(own gm) + z(spread) - z(basket gm)
def f46pp_f46_semi_pricing_power_signal_gmcomp3_252d_base_v144_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    result = _z(g, 252) + _z(s, 252) - _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite expansion: z(own gm) + z(spread) - z(basket gm)
def f46pp_f46_semi_pricing_power_signal_gmcomp3_504d_base_v145_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    result = _z(g, 504) + _z(s, 504) - _z(b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d quality index: mean gm spread times hit ratio own gm change beats basket over 21d
def f46pp_f46_semi_pricing_power_signal_gmqi_21d_base_v146_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(21)
    db = b - b.shift(21)
    hit = (dg > db).astype(float).rolling(21, min_periods=max(2, 21 // 2)).mean()
    result = _mean(s, 21) * hit
    return result.replace([np.inf, -np.inf], np.nan)


# 63d quality index: mean gm spread times hit ratio own gm change beats basket over 63d
def f46pp_f46_semi_pricing_power_signal_gmqi_63d_base_v147_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(63)
    db = b - b.shift(63)
    hit = (dg > db).astype(float).rolling(63, min_periods=max(2, 63 // 2)).mean()
    result = _mean(s, 63) * hit
    return result.replace([np.inf, -np.inf], np.nan)


# 126d quality index: mean gm spread times hit ratio own gm change beats basket over 126d
def f46pp_f46_semi_pricing_power_signal_gmqi_126d_base_v148_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(126)
    db = b - b.shift(126)
    hit = (dg > db).astype(float).rolling(126, min_periods=max(2, 126 // 2)).mean()
    result = _mean(s, 126) * hit
    return result.replace([np.inf, -np.inf], np.nan)


# 252d quality index: mean gm spread times hit ratio own gm change beats basket over 252d
def f46pp_f46_semi_pricing_power_signal_gmqi_252d_base_v149_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(252)
    db = b - b.shift(252)
    hit = (dg > db).astype(float).rolling(252, min_periods=max(2, 252 // 2)).mean()
    result = _mean(s, 252) * hit
    return result.replace([np.inf, -np.inf], np.nan)


# 504d quality index: mean gm spread times hit ratio own gm change beats basket over 504d
def f46pp_f46_semi_pricing_power_signal_gmqi_504d_base_v150_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(504)
    db = b - b.shift(504)
    hit = (dg > db).astype(float).rolling(504, min_periods=max(2, 504 // 2)).mean()
    result = _mean(s, 504) * hit
    return result.replace([np.inf, -np.inf], np.nan)

