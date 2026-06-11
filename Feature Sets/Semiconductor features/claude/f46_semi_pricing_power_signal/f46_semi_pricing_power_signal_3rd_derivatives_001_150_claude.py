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


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _curvature(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w) / sl.abs().replace(0, np.nan)


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


# 5d curvature of 21d own gm centered by 21d mean
def f46pp_f46_semi_pricing_power_signal_gmlvl_21d_curv_v001_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - _mean(g, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d own gm centered by 63d mean
def f46pp_f46_semi_pricing_power_signal_gmlvl_63d_curv_v002_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - _mean(g, 63)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d own gm centered by 126d mean
def f46pp_f46_semi_pricing_power_signal_gmlvl_126d_curv_v003_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - _mean(g, 126)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d own gm centered by 252d mean
def f46pp_f46_semi_pricing_power_signal_gmlvl_252d_curv_v004_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - _mean(g, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d own gm centered by 504d mean
def f46pp_f46_semi_pricing_power_signal_gmlvl_504d_curv_v005_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - _mean(g, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d gm spread own vs basket centered by 21d mean
def f46pp_f46_semi_pricing_power_signal_gmspr_21d_curv_v006_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    base = s - _mean(s, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d gm spread own vs basket centered by 63d mean
def f46pp_f46_semi_pricing_power_signal_gmspr_63d_curv_v007_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    base = s - _mean(s, 63)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d gm spread own vs basket centered by 126d mean
def f46pp_f46_semi_pricing_power_signal_gmspr_126d_curv_v008_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    base = s - _mean(s, 126)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d gm spread own vs basket centered by 252d mean
def f46pp_f46_semi_pricing_power_signal_gmspr_252d_curv_v009_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    base = s - _mean(s, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d gm spread own vs basket centered by 504d mean
def f46pp_f46_semi_pricing_power_signal_gmspr_504d_curv_v010_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    base = s - _mean(s, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d z-score of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmsprz_21d_curv_v011_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    base = _z(s, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d z-score of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmsprz_63d_curv_v012_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    base = _z(s, 63)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d z-score of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmsprz_126d_curv_v013_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    base = _z(s, 126)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d z-score of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmsprz_252d_curv_v014_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    base = _z(s, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d z-score of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmsprz_504d_curv_v015_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    base = _z(s, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d robust z (median/MAD) of gm spread
def f46pp_f46_semi_pricing_power_signal_gmsprrz_21d_curv_v016_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    med = s.rolling(21, min_periods=max(2, 21 // 2)).median()
    mad = (s - med).abs().rolling(21, min_periods=max(2, 21 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    # fall back to rolling std to keep signal alive when mad is zero (quarterly step data)
    sd = _std(s, 21).replace(0, np.nan)
    base = (s - med) / denom.where(denom.notna(), sd)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d robust z (median/MAD) of gm spread
def f46pp_f46_semi_pricing_power_signal_gmsprrz_63d_curv_v017_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    med = s.rolling(63, min_periods=max(2, 63 // 2)).median()
    mad = (s - med).abs().rolling(63, min_periods=max(2, 63 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    # fall back to rolling std to keep signal alive when mad is zero (quarterly step data)
    sd = _std(s, 63).replace(0, np.nan)
    base = (s - med) / denom.where(denom.notna(), sd)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d robust z (median/MAD) of gm spread
def f46pp_f46_semi_pricing_power_signal_gmsprrz_126d_curv_v018_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    med = s.rolling(126, min_periods=max(2, 126 // 2)).median()
    mad = (s - med).abs().rolling(126, min_periods=max(2, 126 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    # fall back to rolling std to keep signal alive when mad is zero (quarterly step data)
    sd = _std(s, 126).replace(0, np.nan)
    base = (s - med) / denom.where(denom.notna(), sd)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d robust z (median/MAD) of gm spread
def f46pp_f46_semi_pricing_power_signal_gmsprrz_252d_curv_v019_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    med = s.rolling(252, min_periods=max(2, 252 // 2)).median()
    mad = (s - med).abs().rolling(252, min_periods=max(2, 252 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    # fall back to rolling std to keep signal alive when mad is zero (quarterly step data)
    sd = _std(s, 252).replace(0, np.nan)
    base = (s - med) / denom.where(denom.notna(), sd)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d robust z (median/MAD) of gm spread
def f46pp_f46_semi_pricing_power_signal_gmsprrz_504d_curv_v020_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    med = s.rolling(504, min_periods=max(2, 504 // 2)).median()
    mad = (s - med).abs().rolling(504, min_periods=max(2, 504 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    # fall back to rolling std to keep signal alive when mad is zero (quarterly step data)
    sd = _std(s, 504).replace(0, np.nan)
    base = (s - med) / denom.where(denom.notna(), sd)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d z-score of own gm
def f46pp_f46_semi_pricing_power_signal_gmz_21d_curv_v021_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = _z(g, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d z-score of own gm
def f46pp_f46_semi_pricing_power_signal_gmz_63d_curv_v022_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = _z(g, 63)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d z-score of own gm
def f46pp_f46_semi_pricing_power_signal_gmz_126d_curv_v023_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = _z(g, 126)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d z-score of own gm
def f46pp_f46_semi_pricing_power_signal_gmz_252d_curv_v024_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = _z(g, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d z-score of own gm
def f46pp_f46_semi_pricing_power_signal_gmz_504d_curv_v025_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = _z(g, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d robust z (median/MAD) of own gm
def f46pp_f46_semi_pricing_power_signal_gmrz_21d_curv_v026_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    med = g.rolling(21, min_periods=max(2, 21 // 2)).median()
    mad = (g - med).abs().rolling(21, min_periods=max(2, 21 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    sd = _std(g, 21).replace(0, np.nan)
    base = (g - med) / denom.where(denom.notna(), sd)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d robust z (median/MAD) of own gm
def f46pp_f46_semi_pricing_power_signal_gmrz_63d_curv_v027_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    med = g.rolling(63, min_periods=max(2, 63 // 2)).median()
    mad = (g - med).abs().rolling(63, min_periods=max(2, 63 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    sd = _std(g, 63).replace(0, np.nan)
    base = (g - med) / denom.where(denom.notna(), sd)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d robust z (median/MAD) of own gm
def f46pp_f46_semi_pricing_power_signal_gmrz_126d_curv_v028_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    med = g.rolling(126, min_periods=max(2, 126 // 2)).median()
    mad = (g - med).abs().rolling(126, min_periods=max(2, 126 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    sd = _std(g, 126).replace(0, np.nan)
    base = (g - med) / denom.where(denom.notna(), sd)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d robust z (median/MAD) of own gm
def f46pp_f46_semi_pricing_power_signal_gmrz_252d_curv_v029_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    med = g.rolling(252, min_periods=max(2, 252 // 2)).median()
    mad = (g - med).abs().rolling(252, min_periods=max(2, 252 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    sd = _std(g, 252).replace(0, np.nan)
    base = (g - med) / denom.where(denom.notna(), sd)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d robust z (median/MAD) of own gm
def f46pp_f46_semi_pricing_power_signal_gmrz_504d_curv_v030_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    med = g.rolling(504, min_periods=max(2, 504 // 2)).median()
    mad = (g - med).abs().rolling(504, min_periods=max(2, 504 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    sd = _std(g, 504).replace(0, np.nan)
    base = (g - med) / denom.where(denom.notna(), sd)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d change in own gm
def f46pp_f46_semi_pricing_power_signal_gmchg_21d_curv_v031_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - g.shift(21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d change in own gm
def f46pp_f46_semi_pricing_power_signal_gmchg_63d_curv_v032_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - g.shift(63)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d change in own gm
def f46pp_f46_semi_pricing_power_signal_gmchg_126d_curv_v033_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - g.shift(126)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d change in own gm
def f46pp_f46_semi_pricing_power_signal_gmchg_252d_curv_v034_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - g.shift(252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d change in own gm
def f46pp_f46_semi_pricing_power_signal_gmchg_504d_curv_v035_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - g.shift(504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d change in basket gm
def f46pp_f46_semi_pricing_power_signal_bgmchg_21d_curv_v036_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    base = b - b.shift(21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d change in basket gm
def f46pp_f46_semi_pricing_power_signal_bgmchg_63d_curv_v037_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    base = b - b.shift(63)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d change in basket gm
def f46pp_f46_semi_pricing_power_signal_bgmchg_126d_curv_v038_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    base = b - b.shift(126)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d change in basket gm
def f46pp_f46_semi_pricing_power_signal_bgmchg_252d_curv_v039_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    base = b - b.shift(252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d change in basket gm
def f46pp_f46_semi_pricing_power_signal_bgmchg_504d_curv_v040_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    base = b - b.shift(504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d relative gm change own vs basket
def f46pp_f46_semi_pricing_power_signal_gmrel_21d_curv_v041_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    base = (g - g.shift(21)) - (b - b.shift(21))
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d relative gm change own vs basket
def f46pp_f46_semi_pricing_power_signal_gmrel_63d_curv_v042_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    base = (g - g.shift(63)) - (b - b.shift(63))
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d relative gm change own vs basket
def f46pp_f46_semi_pricing_power_signal_gmrel_126d_curv_v043_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    base = (g - g.shift(126)) - (b - b.shift(126))
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d relative gm change own vs basket
def f46pp_f46_semi_pricing_power_signal_gmrel_252d_curv_v044_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    base = (g - g.shift(252)) - (b - b.shift(252))
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d relative gm change own vs basket
def f46pp_f46_semi_pricing_power_signal_gmrel_504d_curv_v045_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    base = (g - g.shift(504)) - (b - b.shift(504))
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d negative cov of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcov_21d_curv_v046_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(21)
    db = b - b.shift(21)
    base = -dg.rolling(21, min_periods=max(2, 21 // 2)).cov(db)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d negative cov of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcov_63d_curv_v047_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(63)
    db = b - b.shift(63)
    base = -dg.rolling(63, min_periods=max(2, 63 // 2)).cov(db)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d negative cov of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcov_126d_curv_v048_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(126)
    db = b - b.shift(126)
    base = -dg.rolling(126, min_periods=max(2, 126 // 2)).cov(db)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d negative cov of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcov_252d_curv_v049_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(252)
    db = b - b.shift(252)
    base = -dg.rolling(252, min_periods=max(2, 252 // 2)).cov(db)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d negative cov of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcov_504d_curv_v050_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(504)
    db = b - b.shift(504)
    base = -dg.rolling(504, min_periods=max(2, 504 // 2)).cov(db)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d negative corr of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcorr_21d_curv_v051_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(21)
    db = b - b.shift(21)
    base = -dg.rolling(21, min_periods=max(2, 21 // 2)).corr(db)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d negative corr of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcorr_63d_curv_v052_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(63)
    db = b - b.shift(63)
    base = -dg.rolling(63, min_periods=max(2, 63 // 2)).corr(db)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d negative corr of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcorr_126d_curv_v053_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(126)
    db = b - b.shift(126)
    base = -dg.rolling(126, min_periods=max(2, 126 // 2)).corr(db)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d negative corr of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcorr_252d_curv_v054_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(252)
    db = b - b.shift(252)
    base = -dg.rolling(252, min_periods=max(2, 252 // 2)).corr(db)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d negative corr of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcorr_504d_curv_v055_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(504)
    db = b - b.shift(504)
    base = -dg.rolling(504, min_periods=max(2, 504 // 2)).corr(db)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d rolling beta of own gm change on basket gm change
def f46pp_f46_semi_pricing_power_signal_gmbeta_21d_curv_v056_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(21)
    db = b - b.shift(21)
    cov = dg.rolling(21, min_periods=max(2, 21 // 2)).cov(db)
    var = db.rolling(21, min_periods=max(2, 21 // 2)).var()
    base = cov / var.replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d rolling beta of own gm change on basket gm change
def f46pp_f46_semi_pricing_power_signal_gmbeta_63d_curv_v057_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(63)
    db = b - b.shift(63)
    cov = dg.rolling(63, min_periods=max(2, 63 // 2)).cov(db)
    var = db.rolling(63, min_periods=max(2, 63 // 2)).var()
    base = cov / var.replace(0, np.nan)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d rolling beta of own gm change on basket gm change
def f46pp_f46_semi_pricing_power_signal_gmbeta_126d_curv_v058_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(126)
    db = b - b.shift(126)
    cov = dg.rolling(126, min_periods=max(2, 126 // 2)).cov(db)
    var = db.rolling(126, min_periods=max(2, 126 // 2)).var()
    base = cov / var.replace(0, np.nan)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d rolling beta of own gm change on basket gm change
def f46pp_f46_semi_pricing_power_signal_gmbeta_252d_curv_v059_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(252)
    db = b - b.shift(252)
    cov = dg.rolling(252, min_periods=max(2, 252 // 2)).cov(db)
    var = db.rolling(252, min_periods=max(2, 252 // 2)).var()
    base = cov / var.replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d rolling beta of own gm change on basket gm change
def f46pp_f46_semi_pricing_power_signal_gmbeta_504d_curv_v060_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(504)
    db = b - b.shift(504)
    cov = dg.rolling(504, min_periods=max(2, 504 // 2)).cov(db)
    var = db.rolling(504, min_periods=max(2, 504 // 2)).var()
    base = cov / var.replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d own gm change when basket gm falling over 21d
def f46pp_f46_semi_pricing_power_signal_gmexpfall_21d_curv_v061_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(21)
    db = b - b.shift(21)
    base = dg.where(db < 0)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d own gm change when basket gm falling over 63d
def f46pp_f46_semi_pricing_power_signal_gmexpfall_63d_curv_v062_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(63)
    db = b - b.shift(63)
    base = dg.where(db < 0)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d own gm change when basket gm falling over 126d
def f46pp_f46_semi_pricing_power_signal_gmexpfall_126d_curv_v063_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(126)
    db = b - b.shift(126)
    base = dg.where(db < 0)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d own gm change when basket gm falling over 252d
def f46pp_f46_semi_pricing_power_signal_gmexpfall_252d_curv_v064_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(252)
    db = b - b.shift(252)
    base = dg.where(db < 0)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d own gm change when basket gm falling over 504d
def f46pp_f46_semi_pricing_power_signal_gmexpfall_504d_curv_v065_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(504)
    db = b - b.shift(504)
    base = dg.where(db < 0)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d own gm change when basket gm rising over 21d
def f46pp_f46_semi_pricing_power_signal_gmexpris_21d_curv_v066_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(21)
    db = b - b.shift(21)
    base = dg.where(db > 0)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d own gm change when basket gm rising over 63d
def f46pp_f46_semi_pricing_power_signal_gmexpris_63d_curv_v067_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(63)
    db = b - b.shift(63)
    base = dg.where(db > 0)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d own gm change when basket gm rising over 126d
def f46pp_f46_semi_pricing_power_signal_gmexpris_126d_curv_v068_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(126)
    db = b - b.shift(126)
    base = dg.where(db > 0)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d own gm change when basket gm rising over 252d
def f46pp_f46_semi_pricing_power_signal_gmexpris_252d_curv_v069_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(252)
    db = b - b.shift(252)
    base = dg.where(db > 0)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d own gm change when basket gm rising over 504d
def f46pp_f46_semi_pricing_power_signal_gmexpris_504d_curv_v070_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(504)
    db = b - b.shift(504)
    base = dg.where(db > 0)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d expansion streak (rolling sum of sign of own gm change)
def f46pp_f46_semi_pricing_power_signal_gmexpstr_21d_curv_v071_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(21)
    base = pd.Series(np.sign(dg), index=dg.index).rolling(21, min_periods=max(2, 21 // 2)).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d expansion streak (rolling sum of sign of own gm change)
def f46pp_f46_semi_pricing_power_signal_gmexpstr_63d_curv_v072_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(63)
    base = pd.Series(np.sign(dg), index=dg.index).rolling(63, min_periods=max(2, 63 // 2)).sum()
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d expansion streak (rolling sum of sign of own gm change)
def f46pp_f46_semi_pricing_power_signal_gmexpstr_126d_curv_v073_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(126)
    base = pd.Series(np.sign(dg), index=dg.index).rolling(126, min_periods=max(2, 126 // 2)).sum()
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d expansion streak (rolling sum of sign of own gm change)
def f46pp_f46_semi_pricing_power_signal_gmexpstr_252d_curv_v074_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(252)
    base = pd.Series(np.sign(dg), index=dg.index).rolling(252, min_periods=max(2, 252 // 2)).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d expansion streak (rolling sum of sign of own gm change)
def f46pp_f46_semi_pricing_power_signal_gmexpstr_504d_curv_v075_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(504)
    base = pd.Series(np.sign(dg), index=dg.index).rolling(504, min_periods=max(2, 504 // 2)).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d outperformance streak (rolling sum of sign of own minus basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmoutstr_21d_curv_v076_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    d = (g - g.shift(21)) - (b - b.shift(21))
    base = pd.Series(np.sign(d), index=d.index).rolling(21, min_periods=max(2, 21 // 2)).sum()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d outperformance streak (rolling sum of sign of own minus basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmoutstr_63d_curv_v077_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    d = (g - g.shift(63)) - (b - b.shift(63))
    base = pd.Series(np.sign(d), index=d.index).rolling(63, min_periods=max(2, 63 // 2)).sum()
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d outperformance streak (rolling sum of sign of own minus basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmoutstr_126d_curv_v078_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    d = (g - g.shift(126)) - (b - b.shift(126))
    base = pd.Series(np.sign(d), index=d.index).rolling(126, min_periods=max(2, 126 // 2)).sum()
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d outperformance streak (rolling sum of sign of own minus basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmoutstr_252d_curv_v079_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    d = (g - g.shift(252)) - (b - b.shift(252))
    base = pd.Series(np.sign(d), index=d.index).rolling(252, min_periods=max(2, 252 // 2)).sum()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d outperformance streak (rolling sum of sign of own minus basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmoutstr_504d_curv_v080_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    d = (g - g.shift(504)) - (b - b.shift(504))
    base = pd.Series(np.sign(d), index=d.index).rolling(504, min_periods=max(2, 504 // 2)).sum()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d drawdown of own gm from rolling peak
def f46pp_f46_semi_pricing_power_signal_gmdd_21d_curv_v081_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - _max(g, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d drawdown of own gm from rolling peak
def f46pp_f46_semi_pricing_power_signal_gmdd_63d_curv_v082_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - _max(g, 63)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d drawdown of own gm from rolling peak
def f46pp_f46_semi_pricing_power_signal_gmdd_126d_curv_v083_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - _max(g, 126)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d drawdown of own gm from rolling peak
def f46pp_f46_semi_pricing_power_signal_gmdd_252d_curv_v084_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - _max(g, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d drawdown of own gm from rolling peak
def f46pp_f46_semi_pricing_power_signal_gmdd_504d_curv_v085_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - _max(g, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d run-up of own gm above rolling trough
def f46pp_f46_semi_pricing_power_signal_gmru_21d_curv_v086_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - _min(g, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d run-up of own gm above rolling trough
def f46pp_f46_semi_pricing_power_signal_gmru_63d_curv_v087_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - _min(g, 63)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d run-up of own gm above rolling trough
def f46pp_f46_semi_pricing_power_signal_gmru_126d_curv_v088_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - _min(g, 126)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d run-up of own gm above rolling trough
def f46pp_f46_semi_pricing_power_signal_gmru_252d_curv_v089_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - _min(g, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d run-up of own gm above rolling trough
def f46pp_f46_semi_pricing_power_signal_gmru_504d_curv_v090_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = g - _min(g, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d own gm position in rolling range
def f46pp_f46_semi_pricing_power_signal_gmpos_21d_curv_v091_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    lo = _min(g, 21)
    hi = _max(g, 21)
    base = (g - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d own gm position in rolling range
def f46pp_f46_semi_pricing_power_signal_gmpos_63d_curv_v092_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    lo = _min(g, 63)
    hi = _max(g, 63)
    base = (g - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d own gm position in rolling range
def f46pp_f46_semi_pricing_power_signal_gmpos_126d_curv_v093_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    lo = _min(g, 126)
    hi = _max(g, 126)
    base = (g - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d own gm position in rolling range
def f46pp_f46_semi_pricing_power_signal_gmpos_252d_curv_v094_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    lo = _min(g, 252)
    hi = _max(g, 252)
    base = (g - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d own gm position in rolling range
def f46pp_f46_semi_pricing_power_signal_gmpos_504d_curv_v095_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    lo = _min(g, 504)
    hi = _max(g, 504)
    base = (g - lo) / (hi - lo).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d std of own gm change
def f46pp_f46_semi_pricing_power_signal_gmvol_21d_curv_v096_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = _std(g - g.shift(21), 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d std of own gm change
def f46pp_f46_semi_pricing_power_signal_gmvol_63d_curv_v097_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = _std(g - g.shift(63), 63)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d std of own gm change
def f46pp_f46_semi_pricing_power_signal_gmvol_126d_curv_v098_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = _std(g - g.shift(126), 126)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d std of own gm change
def f46pp_f46_semi_pricing_power_signal_gmvol_252d_curv_v099_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = _std(g - g.shift(252), 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d std of own gm change
def f46pp_f46_semi_pricing_power_signal_gmvol_504d_curv_v100_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    base = _std(g - g.shift(504), 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d ratio own gm change std to basket gm change std
def f46pp_f46_semi_pricing_power_signal_gmvolr_21d_curv_v101_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    base = _std(g - g.shift(21), 21) / _std(b - b.shift(21), 21).replace(0, np.nan)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d ratio own gm change std to basket gm change std
def f46pp_f46_semi_pricing_power_signal_gmvolr_63d_curv_v102_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    base = _std(g - g.shift(63), 63) / _std(b - b.shift(63), 63).replace(0, np.nan)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d ratio own gm change std to basket gm change std
def f46pp_f46_semi_pricing_power_signal_gmvolr_126d_curv_v103_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    base = _std(g - g.shift(126), 126) / _std(b - b.shift(126), 126).replace(0, np.nan)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d ratio own gm change std to basket gm change std
def f46pp_f46_semi_pricing_power_signal_gmvolr_252d_curv_v104_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    base = _std(g - g.shift(252), 252) / _std(b - b.shift(252), 252).replace(0, np.nan)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d ratio own gm change std to basket gm change std
def f46pp_f46_semi_pricing_power_signal_gmvolr_504d_curv_v105_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    base = _std(g - g.shift(504), 504) / _std(b - b.shift(504), 504).replace(0, np.nan)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d ema crossover of own gm (short=max(2,W/4) vs long=W)
def f46pp_f46_semi_pricing_power_signal_gmema_21d_curv_v106_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    short = max(2, 21 // 4)
    base = g.ewm(span=short, adjust=False).mean() - g.ewm(span=21, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d ema crossover of own gm (short=max(2,W/4) vs long=W)
def f46pp_f46_semi_pricing_power_signal_gmema_63d_curv_v107_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    short = max(2, 63 // 4)
    base = g.ewm(span=short, adjust=False).mean() - g.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d ema crossover of own gm (short=max(2,W/4) vs long=W)
def f46pp_f46_semi_pricing_power_signal_gmema_126d_curv_v108_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    short = max(2, 126 // 4)
    base = g.ewm(span=short, adjust=False).mean() - g.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d ema crossover of own gm (short=max(2,W/4) vs long=W)
def f46pp_f46_semi_pricing_power_signal_gmema_252d_curv_v109_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    short = max(2, 252 // 4)
    base = g.ewm(span=short, adjust=False).mean() - g.ewm(span=252, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d ema crossover of own gm (short=max(2,W/4) vs long=W)
def f46pp_f46_semi_pricing_power_signal_gmema_504d_curv_v110_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    short = max(2, 504 // 4)
    base = g.ewm(span=short, adjust=False).mean() - g.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d ema crossover of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmspema_21d_curv_v111_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    short = max(2, 21 // 4)
    base = s.ewm(span=short, adjust=False).mean() - s.ewm(span=21, adjust=False).mean()
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d ema crossover of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmspema_63d_curv_v112_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    short = max(2, 63 // 4)
    base = s.ewm(span=short, adjust=False).mean() - s.ewm(span=63, adjust=False).mean()
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d ema crossover of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmspema_126d_curv_v113_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    short = max(2, 126 // 4)
    base = s.ewm(span=short, adjust=False).mean() - s.ewm(span=126, adjust=False).mean()
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d ema crossover of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmspema_252d_curv_v114_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    short = max(2, 252 // 4)
    base = s.ewm(span=short, adjust=False).mean() - s.ewm(span=252, adjust=False).mean()
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d ema crossover of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmspema_504d_curv_v115_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    short = max(2, 504 // 4)
    base = s.ewm(span=short, adjust=False).mean() - s.ewm(span=504, adjust=False).mean()
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d acceleration of own gm (second diff over 21d)
def f46pp_f46_semi_pricing_power_signal_gmacc_21d_curv_v116_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(21)
    base = dg - dg.shift(21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d acceleration of own gm (second diff over 63d)
def f46pp_f46_semi_pricing_power_signal_gmacc_63d_curv_v117_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(63)
    base = dg - dg.shift(63)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d acceleration of own gm (second diff over 126d)
def f46pp_f46_semi_pricing_power_signal_gmacc_126d_curv_v118_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(126)
    base = dg - dg.shift(126)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d acceleration of own gm (second diff over 252d)
def f46pp_f46_semi_pricing_power_signal_gmacc_252d_curv_v119_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(252)
    base = dg - dg.shift(252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d acceleration of own gm (second diff over 504d)
def f46pp_f46_semi_pricing_power_signal_gmacc_504d_curv_v120_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(504)
    base = dg - dg.shift(504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d acceleration of basket gm (second diff over 21d)
def f46pp_f46_semi_pricing_power_signal_bgmacc_21d_curv_v121_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    db = b - b.shift(21)
    base = db - db.shift(21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d acceleration of basket gm (second diff over 63d)
def f46pp_f46_semi_pricing_power_signal_bgmacc_63d_curv_v122_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    db = b - b.shift(63)
    base = db - db.shift(63)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d acceleration of basket gm (second diff over 126d)
def f46pp_f46_semi_pricing_power_signal_bgmacc_126d_curv_v123_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    db = b - b.shift(126)
    base = db - db.shift(126)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d acceleration of basket gm (second diff over 252d)
def f46pp_f46_semi_pricing_power_signal_bgmacc_252d_curv_v124_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    db = b - b.shift(252)
    base = db - db.shift(252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d acceleration of basket gm (second diff over 504d)
def f46pp_f46_semi_pricing_power_signal_bgmacc_504d_curv_v125_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    db = b - b.shift(504)
    base = db - db.shift(504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d acceleration of gm spread own vs basket (second diff over 21d)
def f46pp_f46_semi_pricing_power_signal_gmspracc_21d_curv_v126_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    ds = s - s.shift(21)
    base = ds - ds.shift(21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d acceleration of gm spread own vs basket (second diff over 63d)
def f46pp_f46_semi_pricing_power_signal_gmspracc_63d_curv_v127_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    ds = s - s.shift(63)
    base = ds - ds.shift(63)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d acceleration of gm spread own vs basket (second diff over 126d)
def f46pp_f46_semi_pricing_power_signal_gmspracc_126d_curv_v128_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    ds = s - s.shift(126)
    base = ds - ds.shift(126)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d acceleration of gm spread own vs basket (second diff over 252d)
def f46pp_f46_semi_pricing_power_signal_gmspracc_252d_curv_v129_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    ds = s - s.shift(252)
    base = ds - ds.shift(252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d acceleration of gm spread own vs basket (second diff over 504d)
def f46pp_f46_semi_pricing_power_signal_gmspracc_504d_curv_v130_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    ds = s - s.shift(504)
    base = ds - ds.shift(504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d composite strength: z(spread) + z(own gm) + z(Wd own gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp1_21d_curv_v131_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    cg = g - g.shift(21)
    base = _z(s, 21) + _z(g, 21) + _z(cg, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d composite strength: z(spread) + z(own gm) + z(Wd own gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp1_63d_curv_v132_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    cg = g - g.shift(63)
    base = _z(s, 63) + _z(g, 63) + _z(cg, 63)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d composite strength: z(spread) + z(own gm) + z(Wd own gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp1_126d_curv_v133_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    cg = g - g.shift(126)
    base = _z(s, 126) + _z(g, 126) + _z(cg, 126)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d composite strength: z(spread) + z(own gm) + z(Wd own gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp1_252d_curv_v134_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    cg = g - g.shift(252)
    base = _z(s, 252) + _z(g, 252) + _z(cg, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d composite strength: z(spread) + z(own gm) + z(Wd own gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp1_504d_curv_v135_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    cg = g - g.shift(504)
    base = _z(s, 504) + _z(g, 504) + _z(cg, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d composite pricing power: z(spread) minus z(corr own/basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp2_21d_curv_v136_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(21)
    db = b - b.shift(21)
    c = dg.rolling(21, min_periods=max(2, 21 // 2)).corr(db)
    base = _z(s, 21) - _z(c, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d composite pricing power: z(spread) minus z(corr own/basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp2_63d_curv_v137_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(63)
    db = b - b.shift(63)
    c = dg.rolling(63, min_periods=max(2, 63 // 2)).corr(db)
    base = _z(s, 63) - _z(c, 63)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d composite pricing power: z(spread) minus z(corr own/basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp2_126d_curv_v138_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(126)
    db = b - b.shift(126)
    c = dg.rolling(126, min_periods=max(2, 126 // 2)).corr(db)
    base = _z(s, 126) - _z(c, 126)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d composite pricing power: z(spread) minus z(corr own/basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp2_252d_curv_v139_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(252)
    db = b - b.shift(252)
    c = dg.rolling(252, min_periods=max(2, 252 // 2)).corr(db)
    base = _z(s, 252) - _z(c, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d composite pricing power: z(spread) minus z(corr own/basket gm change)
def f46pp_f46_semi_pricing_power_signal_gmcomp2_504d_curv_v140_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(504)
    db = b - b.shift(504)
    c = dg.rolling(504, min_periods=max(2, 504 // 2)).corr(db)
    base = _z(s, 504) - _z(c, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d composite expansion: z(own gm) + z(spread) - z(basket gm)
def f46pp_f46_semi_pricing_power_signal_gmcomp3_21d_curv_v141_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    base = _z(g, 21) + _z(s, 21) - _z(b, 21)
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d composite expansion: z(own gm) + z(spread) - z(basket gm)
def f46pp_f46_semi_pricing_power_signal_gmcomp3_63d_curv_v142_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    base = _z(g, 63) + _z(s, 63) - _z(b, 63)
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d composite expansion: z(own gm) + z(spread) - z(basket gm)
def f46pp_f46_semi_pricing_power_signal_gmcomp3_126d_curv_v143_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    base = _z(g, 126) + _z(s, 126) - _z(b, 126)
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d composite expansion: z(own gm) + z(spread) - z(basket gm)
def f46pp_f46_semi_pricing_power_signal_gmcomp3_252d_curv_v144_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    base = _z(g, 252) + _z(s, 252) - _z(b, 252)
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d composite expansion: z(own gm) + z(spread) - z(basket gm)
def f46pp_f46_semi_pricing_power_signal_gmcomp3_504d_curv_v145_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    base = _z(g, 504) + _z(s, 504) - _z(b, 504)
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d curvature of 21d quality index: mean gm spread times hit ratio own gm change beats basket over 21d
def f46pp_f46_semi_pricing_power_signal_gmqi_21d_curv_v146_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(21)
    db = b - b.shift(21)
    hit = (dg > db).astype(float).rolling(21, min_periods=max(2, 21 // 2)).mean()
    base = _mean(s, 21) * hit
    result = _curvature(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 15d curvature of 63d quality index: mean gm spread times hit ratio own gm change beats basket over 63d
def f46pp_f46_semi_pricing_power_signal_gmqi_63d_curv_v147_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(63)
    db = b - b.shift(63)
    hit = (dg > db).astype(float).rolling(63, min_periods=max(2, 63 // 2)).mean()
    base = _mean(s, 63) * hit
    result = _curvature(base, 15)
    return result.replace([np.inf, -np.inf], np.nan)


# 31d curvature of 126d quality index: mean gm spread times hit ratio own gm change beats basket over 126d
def f46pp_f46_semi_pricing_power_signal_gmqi_126d_curv_v148_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(126)
    db = b - b.shift(126)
    hit = (dg > db).astype(float).rolling(126, min_periods=max(2, 126 // 2)).mean()
    base = _mean(s, 126) * hit
    result = _curvature(base, 31)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d curvature of 252d quality index: mean gm spread times hit ratio own gm change beats basket over 252d
def f46pp_f46_semi_pricing_power_signal_gmqi_252d_curv_v149_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(252)
    db = b - b.shift(252)
    hit = (dg > db).astype(float).rolling(252, min_periods=max(2, 252 // 2)).mean()
    base = _mean(s, 252) * hit
    result = _curvature(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d curvature of 504d quality index: mean gm spread times hit ratio own gm change beats basket over 504d
def f46pp_f46_semi_pricing_power_signal_gmqi_504d_curv_v150_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    dg = g - g.shift(504)
    db = b - b.shift(504)
    hit = (dg > db).astype(float).rolling(504, min_periods=max(2, 504 // 2)).mean()
    base = _mean(s, 504) * hit
    result = _curvature(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)

