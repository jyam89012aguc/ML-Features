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


# 21d own gm centered by 21d mean
def f46pp_f46_semi_pricing_power_signal_gmlvl_21d_base_v001_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - _mean(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own gm centered by 63d mean
def f46pp_f46_semi_pricing_power_signal_gmlvl_63d_base_v002_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - _mean(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own gm centered by 126d mean
def f46pp_f46_semi_pricing_power_signal_gmlvl_126d_base_v003_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - _mean(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own gm centered by 252d mean
def f46pp_f46_semi_pricing_power_signal_gmlvl_252d_base_v004_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - _mean(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own gm centered by 504d mean
def f46pp_f46_semi_pricing_power_signal_gmlvl_504d_base_v005_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - _mean(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gm spread own vs basket centered by 21d mean
def f46pp_f46_semi_pricing_power_signal_gmspr_21d_base_v006_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    result = s - _mean(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gm spread own vs basket centered by 63d mean
def f46pp_f46_semi_pricing_power_signal_gmspr_63d_base_v007_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    result = s - _mean(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d gm spread own vs basket centered by 126d mean
def f46pp_f46_semi_pricing_power_signal_gmspr_126d_base_v008_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    result = s - _mean(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gm spread own vs basket centered by 252d mean
def f46pp_f46_semi_pricing_power_signal_gmspr_252d_base_v009_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    result = s - _mean(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gm spread own vs basket centered by 504d mean
def f46pp_f46_semi_pricing_power_signal_gmspr_504d_base_v010_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    result = s - _mean(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmsprz_21d_base_v011_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    result = _z(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmsprz_63d_base_v012_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    result = _z(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmsprz_126d_base_v013_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    result = _z(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmsprz_252d_base_v014_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    result = _z(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of gm spread own vs basket
def f46pp_f46_semi_pricing_power_signal_gmsprz_504d_base_v015_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    result = _z(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z (median/MAD) of gm spread
def f46pp_f46_semi_pricing_power_signal_gmsprrz_21d_base_v016_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    med = s.rolling(21, min_periods=max(2, 21 // 2)).median()
    mad = (s - med).abs().rolling(21, min_periods=max(2, 21 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    # fall back to rolling std to keep signal alive when mad is zero (quarterly step data)
    sd = _std(s, 21).replace(0, np.nan)
    result = (s - med) / denom.where(denom.notna(), sd)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z (median/MAD) of gm spread
def f46pp_f46_semi_pricing_power_signal_gmsprrz_63d_base_v017_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    med = s.rolling(63, min_periods=max(2, 63 // 2)).median()
    mad = (s - med).abs().rolling(63, min_periods=max(2, 63 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    # fall back to rolling std to keep signal alive when mad is zero (quarterly step data)
    sd = _std(s, 63).replace(0, np.nan)
    result = (s - med) / denom.where(denom.notna(), sd)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z (median/MAD) of gm spread
def f46pp_f46_semi_pricing_power_signal_gmsprrz_126d_base_v018_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    med = s.rolling(126, min_periods=max(2, 126 // 2)).median()
    mad = (s - med).abs().rolling(126, min_periods=max(2, 126 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    # fall back to rolling std to keep signal alive when mad is zero (quarterly step data)
    sd = _std(s, 126).replace(0, np.nan)
    result = (s - med) / denom.where(denom.notna(), sd)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z (median/MAD) of gm spread
def f46pp_f46_semi_pricing_power_signal_gmsprrz_252d_base_v019_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    med = s.rolling(252, min_periods=max(2, 252 // 2)).median()
    mad = (s - med).abs().rolling(252, min_periods=max(2, 252 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    # fall back to rolling std to keep signal alive when mad is zero (quarterly step data)
    sd = _std(s, 252).replace(0, np.nan)
    result = (s - med) / denom.where(denom.notna(), sd)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z (median/MAD) of gm spread
def f46pp_f46_semi_pricing_power_signal_gmsprrz_504d_base_v020_signal(gp, revenue, semi_basket_gm, closeadj):
    s = _f46pp_gm_spread_daily(gp, revenue, semi_basket_gm, closeadj)
    med = s.rolling(504, min_periods=max(2, 504 // 2)).median()
    mad = (s - med).abs().rolling(504, min_periods=max(2, 504 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    # fall back to rolling std to keep signal alive when mad is zero (quarterly step data)
    sd = _std(s, 504).replace(0, np.nan)
    result = (s - med) / denom.where(denom.notna(), sd)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of own gm
def f46pp_f46_semi_pricing_power_signal_gmz_21d_base_v021_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = _z(g, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of own gm
def f46pp_f46_semi_pricing_power_signal_gmz_63d_base_v022_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = _z(g, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of own gm
def f46pp_f46_semi_pricing_power_signal_gmz_126d_base_v023_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = _z(g, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of own gm
def f46pp_f46_semi_pricing_power_signal_gmz_252d_base_v024_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = _z(g, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of own gm
def f46pp_f46_semi_pricing_power_signal_gmz_504d_base_v025_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = _z(g, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d robust z (median/MAD) of own gm
def f46pp_f46_semi_pricing_power_signal_gmrz_21d_base_v026_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    med = g.rolling(21, min_periods=max(2, 21 // 2)).median()
    mad = (g - med).abs().rolling(21, min_periods=max(2, 21 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    sd = _std(g, 21).replace(0, np.nan)
    result = (g - med) / denom.where(denom.notna(), sd)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d robust z (median/MAD) of own gm
def f46pp_f46_semi_pricing_power_signal_gmrz_63d_base_v027_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    med = g.rolling(63, min_periods=max(2, 63 // 2)).median()
    mad = (g - med).abs().rolling(63, min_periods=max(2, 63 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    sd = _std(g, 63).replace(0, np.nan)
    result = (g - med) / denom.where(denom.notna(), sd)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d robust z (median/MAD) of own gm
def f46pp_f46_semi_pricing_power_signal_gmrz_126d_base_v028_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    med = g.rolling(126, min_periods=max(2, 126 // 2)).median()
    mad = (g - med).abs().rolling(126, min_periods=max(2, 126 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    sd = _std(g, 126).replace(0, np.nan)
    result = (g - med) / denom.where(denom.notna(), sd)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d robust z (median/MAD) of own gm
def f46pp_f46_semi_pricing_power_signal_gmrz_252d_base_v029_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    med = g.rolling(252, min_periods=max(2, 252 // 2)).median()
    mad = (g - med).abs().rolling(252, min_periods=max(2, 252 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    sd = _std(g, 252).replace(0, np.nan)
    result = (g - med) / denom.where(denom.notna(), sd)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d robust z (median/MAD) of own gm
def f46pp_f46_semi_pricing_power_signal_gmrz_504d_base_v030_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    med = g.rolling(504, min_periods=max(2, 504 // 2)).median()
    mad = (g - med).abs().rolling(504, min_periods=max(2, 504 // 2)).median()
    denom = (1.4826 * mad).replace(0, np.nan)
    sd = _std(g, 504).replace(0, np.nan)
    result = (g - med) / denom.where(denom.notna(), sd)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d change in own gm
def f46pp_f46_semi_pricing_power_signal_gmchg_21d_base_v031_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - g.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d change in own gm
def f46pp_f46_semi_pricing_power_signal_gmchg_63d_base_v032_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - g.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in own gm
def f46pp_f46_semi_pricing_power_signal_gmchg_126d_base_v033_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - g.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in own gm
def f46pp_f46_semi_pricing_power_signal_gmchg_252d_base_v034_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - g.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d change in own gm
def f46pp_f46_semi_pricing_power_signal_gmchg_504d_base_v035_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    result = g - g.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d change in basket gm
def f46pp_f46_semi_pricing_power_signal_bgmchg_21d_base_v036_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    result = b - b.shift(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d change in basket gm
def f46pp_f46_semi_pricing_power_signal_bgmchg_63d_base_v037_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    result = b - b.shift(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d change in basket gm
def f46pp_f46_semi_pricing_power_signal_bgmchg_126d_base_v038_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    result = b - b.shift(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d change in basket gm
def f46pp_f46_semi_pricing_power_signal_bgmchg_252d_base_v039_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    result = b - b.shift(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d change in basket gm
def f46pp_f46_semi_pricing_power_signal_bgmchg_504d_base_v040_signal(gp, revenue, semi_basket_gm, closeadj):
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    result = b - b.shift(504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d relative gm change own vs basket
def f46pp_f46_semi_pricing_power_signal_gmrel_21d_base_v041_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    result = (g - g.shift(21)) - (b - b.shift(21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d relative gm change own vs basket
def f46pp_f46_semi_pricing_power_signal_gmrel_63d_base_v042_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    result = (g - g.shift(63)) - (b - b.shift(63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d relative gm change own vs basket
def f46pp_f46_semi_pricing_power_signal_gmrel_126d_base_v043_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    result = (g - g.shift(126)) - (b - b.shift(126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d relative gm change own vs basket
def f46pp_f46_semi_pricing_power_signal_gmrel_252d_base_v044_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    result = (g - g.shift(252)) - (b - b.shift(252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d relative gm change own vs basket
def f46pp_f46_semi_pricing_power_signal_gmrel_504d_base_v045_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    result = (g - g.shift(504)) - (b - b.shift(504))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d negative cov of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcov_21d_base_v046_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(21)
    db = b - b.shift(21)
    result = -dg.rolling(21, min_periods=max(2, 21 // 2)).cov(db)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d negative cov of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcov_63d_base_v047_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(63)
    db = b - b.shift(63)
    result = -dg.rolling(63, min_periods=max(2, 63 // 2)).cov(db)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d negative cov of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcov_126d_base_v048_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(126)
    db = b - b.shift(126)
    result = -dg.rolling(126, min_periods=max(2, 126 // 2)).cov(db)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d negative cov of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcov_252d_base_v049_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(252)
    db = b - b.shift(252)
    result = -dg.rolling(252, min_periods=max(2, 252 // 2)).cov(db)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d negative cov of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcov_504d_base_v050_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(504)
    db = b - b.shift(504)
    result = -dg.rolling(504, min_periods=max(2, 504 // 2)).cov(db)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d negative corr of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcorr_21d_base_v051_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(21)
    db = b - b.shift(21)
    result = -dg.rolling(21, min_periods=max(2, 21 // 2)).corr(db)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d negative corr of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcorr_63d_base_v052_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(63)
    db = b - b.shift(63)
    result = -dg.rolling(63, min_periods=max(2, 63 // 2)).corr(db)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d negative corr of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcorr_126d_base_v053_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(126)
    db = b - b.shift(126)
    result = -dg.rolling(126, min_periods=max(2, 126 // 2)).corr(db)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d negative corr of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcorr_252d_base_v054_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(252)
    db = b - b.shift(252)
    result = -dg.rolling(252, min_periods=max(2, 252 // 2)).corr(db)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d negative corr of own gm change vs basket gm change
def f46pp_f46_semi_pricing_power_signal_gmcorr_504d_base_v055_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(504)
    db = b - b.shift(504)
    result = -dg.rolling(504, min_periods=max(2, 504 // 2)).corr(db)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d rolling beta of own gm change on basket gm change
def f46pp_f46_semi_pricing_power_signal_gmbeta_21d_base_v056_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(21)
    db = b - b.shift(21)
    cov = dg.rolling(21, min_periods=max(2, 21 // 2)).cov(db)
    var = db.rolling(21, min_periods=max(2, 21 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d rolling beta of own gm change on basket gm change
def f46pp_f46_semi_pricing_power_signal_gmbeta_63d_base_v057_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(63)
    db = b - b.shift(63)
    cov = dg.rolling(63, min_periods=max(2, 63 // 2)).cov(db)
    var = db.rolling(63, min_periods=max(2, 63 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d rolling beta of own gm change on basket gm change
def f46pp_f46_semi_pricing_power_signal_gmbeta_126d_base_v058_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(126)
    db = b - b.shift(126)
    cov = dg.rolling(126, min_periods=max(2, 126 // 2)).cov(db)
    var = db.rolling(126, min_periods=max(2, 126 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d rolling beta of own gm change on basket gm change
def f46pp_f46_semi_pricing_power_signal_gmbeta_252d_base_v059_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(252)
    db = b - b.shift(252)
    cov = dg.rolling(252, min_periods=max(2, 252 // 2)).cov(db)
    var = db.rolling(252, min_periods=max(2, 252 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d rolling beta of own gm change on basket gm change
def f46pp_f46_semi_pricing_power_signal_gmbeta_504d_base_v060_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(504)
    db = b - b.shift(504)
    cov = dg.rolling(504, min_periods=max(2, 504 // 2)).cov(db)
    var = db.rolling(504, min_periods=max(2, 504 // 2)).var()
    result = cov / var.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d own gm change when basket gm falling over 21d
def f46pp_f46_semi_pricing_power_signal_gmexpfall_21d_base_v061_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(21)
    db = b - b.shift(21)
    result = dg.where(db < 0)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own gm change when basket gm falling over 63d
def f46pp_f46_semi_pricing_power_signal_gmexpfall_63d_base_v062_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(63)
    db = b - b.shift(63)
    result = dg.where(db < 0)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own gm change when basket gm falling over 126d
def f46pp_f46_semi_pricing_power_signal_gmexpfall_126d_base_v063_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(126)
    db = b - b.shift(126)
    result = dg.where(db < 0)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own gm change when basket gm falling over 252d
def f46pp_f46_semi_pricing_power_signal_gmexpfall_252d_base_v064_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(252)
    db = b - b.shift(252)
    result = dg.where(db < 0)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own gm change when basket gm falling over 504d
def f46pp_f46_semi_pricing_power_signal_gmexpfall_504d_base_v065_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(504)
    db = b - b.shift(504)
    result = dg.where(db < 0)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d own gm change when basket gm rising over 21d
def f46pp_f46_semi_pricing_power_signal_gmexpris_21d_base_v066_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(21)
    db = b - b.shift(21)
    result = dg.where(db > 0)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d own gm change when basket gm rising over 63d
def f46pp_f46_semi_pricing_power_signal_gmexpris_63d_base_v067_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(63)
    db = b - b.shift(63)
    result = dg.where(db > 0)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d own gm change when basket gm rising over 126d
def f46pp_f46_semi_pricing_power_signal_gmexpris_126d_base_v068_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(126)
    db = b - b.shift(126)
    result = dg.where(db > 0)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d own gm change when basket gm rising over 252d
def f46pp_f46_semi_pricing_power_signal_gmexpris_252d_base_v069_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(252)
    db = b - b.shift(252)
    result = dg.where(db > 0)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d own gm change when basket gm rising over 504d
def f46pp_f46_semi_pricing_power_signal_gmexpris_504d_base_v070_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    b = _f46pp_basket_gm_daily(semi_basket_gm, closeadj)
    dg = g - g.shift(504)
    db = b - b.shift(504)
    result = dg.where(db > 0)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d expansion streak (rolling sum of sign of own gm change)
def f46pp_f46_semi_pricing_power_signal_gmexpstr_21d_base_v071_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(21)
    result = pd.Series(np.sign(dg), index=dg.index).rolling(21, min_periods=max(2, 21 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d expansion streak (rolling sum of sign of own gm change)
def f46pp_f46_semi_pricing_power_signal_gmexpstr_63d_base_v072_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(63)
    result = pd.Series(np.sign(dg), index=dg.index).rolling(63, min_periods=max(2, 63 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d expansion streak (rolling sum of sign of own gm change)
def f46pp_f46_semi_pricing_power_signal_gmexpstr_126d_base_v073_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(126)
    result = pd.Series(np.sign(dg), index=dg.index).rolling(126, min_periods=max(2, 126 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d expansion streak (rolling sum of sign of own gm change)
def f46pp_f46_semi_pricing_power_signal_gmexpstr_252d_base_v074_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(252)
    result = pd.Series(np.sign(dg), index=dg.index).rolling(252, min_periods=max(2, 252 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d expansion streak (rolling sum of sign of own gm change)
def f46pp_f46_semi_pricing_power_signal_gmexpstr_504d_base_v075_signal(gp, revenue, semi_basket_gm, closeadj):
    g = _f46pp_gm_daily(gp, revenue, closeadj)
    dg = g - g.shift(504)
    result = pd.Series(np.sign(dg), index=dg.index).rolling(504, min_periods=max(2, 504 // 2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

